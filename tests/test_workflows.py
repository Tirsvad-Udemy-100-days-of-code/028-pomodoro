"""Static test of the repository's continuous integration workflow files.

Every file in ``.gitea/workflows/`` is parsed with a strict, safe YAML loader
and checked against the workflow rules of the project (MIL-005, QC-WF-001).
The rules are small pure functions that return a list of problems; a
self-test feeds each one a deliberately broken workflow to prove it can fail.
"""

import copy
import re
from collections.abc import Callable, Hashable
from pathlib import Path
from typing import Any

import pytest
import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode, Node

# A parsed workflow is arbitrary YAML: keys may be booleans (YAML 1.1 reads
# `on` as True) and values have no fixed type, so `Any` is unavoidable here.
Workflow = dict[Any, Any]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_FILES = sorted((PROJECT_ROOT / ".gitea" / "workflows").glob("*.y*ml"))

REQUIRED_KEYS = ("name", "on", "jobs")
REQUIRED_JOB_KEYS = ("runs-on", "timeout-minutes")
MAX_RUN_LINES = 5
PINNED_REFERENCE = re.compile(
    r"[\w.-]+/[\w.-]+(?:/[\w./-]+)?@(?:v?\d+\.\d+\.\d+|[0-9a-f]{40})"
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects a mapping with a duplicate key."""

    def construct_mapping(self, node: Node, deep: bool = False) -> dict[Hashable, Any]:
        if not isinstance(node, MappingNode):
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "expected a mapping node",
                node.start_mark,
            )
        self.flatten_mapping(node)
        seen: set[Hashable] = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if isinstance(key, Hashable) and key in seen:
                raise ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


def load_workflow(text: str) -> Workflow:
    """Parse workflow text; raise on invalid YAML or a duplicate key."""
    document = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(document, dict):
        raise ValueError("a workflow must be a YAML mapping")
    return document


def triggers(workflow: Workflow) -> Any:
    """Return the `on` section; PyYAML (YAML 1.1) loads the key `on` as True."""
    return workflow.get("on", workflow.get(True))


def jobs_of(workflow: Workflow) -> dict[str, Workflow]:
    """Return the jobs mapping, or an empty one when it is missing or wrong."""
    jobs = workflow.get("jobs")
    if not isinstance(jobs, dict):
        return {}
    return {str(name): job for name, job in jobs.items() if isinstance(job, dict)}


def steps_of(job: Workflow) -> list[Workflow]:
    """Return the step mappings of a job."""
    steps = job.get("steps")
    if not isinstance(steps, list):
        return []
    return [step for step in steps if isinstance(step, dict)]


def check_required_keys(workflow: Workflow) -> list[str]:
    """Report missing top-level keys and an empty jobs section."""
    problems = [
        f"missing top-level key '{key}'"
        for key in REQUIRED_KEYS
        if key != "on" and key not in workflow
    ]
    if triggers(workflow) is None:
        problems.append("missing top-level key 'on'")
    if "jobs" in workflow and not jobs_of(workflow):
        problems.append("'jobs' is empty")
    return problems


def check_jobs(workflow: Workflow) -> list[str]:
    """Report jobs without a runner or a timeout."""
    return [
        f"job '{name}' is missing '{key}'"
        for name, job in jobs_of(workflow).items()
        for key in REQUIRED_JOB_KEYS
        if key not in job
    ]


def check_permissions(workflow: Workflow) -> list[str]:
    """Report jobs that have no explicit permissions at any level."""
    if "permissions" in workflow:
        return []
    return [
        f"job '{name}' has no 'permissions' and the workflow declares none"
        for name, job in jobs_of(workflow).items()
        if "permissions" not in job
    ]


def is_pinned(reference: str) -> bool:
    """Tell whether a `uses:` value is local, an exact tag or a commit SHA."""
    return reference.startswith("./") or bool(PINNED_REFERENCE.fullmatch(reference))


def check_pinned_actions(workflow: Workflow) -> list[str]:
    """Report `uses:` references not pinned to an exact tag or commit SHA."""
    problems: list[str] = []
    for name, job in jobs_of(workflow).items():
        for holder in [job, *steps_of(job)]:
            reference = holder.get("uses")
            if reference is not None and not is_pinned(str(reference)):
                problems.append(
                    f"job '{name}' uses '{reference}': pin to an exact tag or SHA"
                )
    return problems


def check_inline_scripts(workflow: Workflow) -> list[str]:
    """Report `run:` blocks longer than the allowed number of lines."""
    problems: list[str] = []
    for name, job in jobs_of(workflow).items():
        for step in steps_of(job):
            script = step.get("run")
            if not isinstance(script, str):
                continue
            lines = [line for line in script.splitlines() if line.strip()]
            if len(lines) > MAX_RUN_LINES:
                problems.append(
                    f"job '{name}' has a run block of {len(lines)} lines "
                    f"(max {MAX_RUN_LINES})"
                )
    return problems


type Check = Callable[[Workflow], list[str]]

CHECKS: list[Check] = [
    check_required_keys,
    check_jobs,
    check_permissions,
    check_pinned_actions,
    check_inline_scripts,
]


def valid_workflow() -> Workflow:
    """Return a minimal workflow that passes every check."""
    return {
        "name": "CI",
        "on": {"push": {"branches": ["main"]}},
        "permissions": {"contents": "read"},
        "jobs": {
            "test": {
                "runs-on": "ubuntu-24.04",
                "timeout-minutes": 10,
                "steps": [
                    {"uses": "actions/checkout@v4.2.2"},
                    {"uses": "./.gitea/actions/local"},
                    {"run": "python -m pytest"},
                ],
            }
        },
    }


def broken(mutate: Callable[[Workflow], object]) -> Workflow:
    """Return a copy of the valid workflow changed by `mutate` (in place)."""
    workflow = copy.deepcopy(valid_workflow())
    mutate(workflow)
    return workflow


def job_of(workflow: Workflow) -> Workflow:
    job: Workflow = workflow["jobs"]["test"]
    return job


# --- the real workflow files -------------------------------------------------


def test_workflow_files_exist() -> None:
    assert WORKFLOW_FILES, "no workflow file found in .gitea/workflows/"


@pytest.fixture(params=WORKFLOW_FILES, ids=lambda path: path.name)
def workflow(request: pytest.FixtureRequest) -> Workflow:
    return load_workflow(request.param.read_text(encoding="utf-8"))


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda path: path.name)
def test_workflow_is_valid_yaml_without_duplicate_keys(path: Path) -> None:
    assert load_workflow(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("check", CHECKS, ids=lambda check: check.__name__)
def test_workflow_passes_check(workflow: Workflow, check: Check) -> None:
    problems = check(workflow)
    assert problems == []


# --- self-test: each check can fail ------------------------------------------


def test_valid_sample_passes_all_checks() -> None:
    workflow = valid_workflow()
    assert [problem for check in CHECKS for problem in check(workflow)] == []


def test_loader_rejects_duplicate_key() -> None:
    text = "name: CI\nname: Again\non: push\njobs: {}\n"
    with pytest.raises(ConstructorError, match="duplicate key"):
        load_workflow(text)


def test_loader_rejects_invalid_yaml() -> None:
    with pytest.raises(yaml.YAMLError):
        load_workflow("name: [unclosed\n")


def test_triggers_reads_on_key_loaded_as_boolean() -> None:
    assert triggers(load_workflow("name: CI\non: push\njobs: {}\n")) == "push"


def test_missing_name_is_reported() -> None:
    workflow = broken(lambda w: w.pop("name"))
    assert check_required_keys(workflow) == ["missing top-level key 'name'"]


def test_missing_triggers_are_reported() -> None:
    workflow = broken(lambda w: w.pop("on"))
    assert check_required_keys(workflow) == ["missing top-level key 'on'"]


def test_empty_jobs_are_reported() -> None:
    workflow = broken(lambda w: w.update(jobs={}))
    assert check_required_keys(workflow) == ["'jobs' is empty"]


@pytest.mark.parametrize("key", REQUIRED_JOB_KEYS)
def test_job_without_required_key_is_reported(key: str) -> None:
    workflow = broken(lambda w: job_of(w).pop(key))
    assert check_jobs(workflow) == [f"job 'test' is missing '{key}'"]


def test_missing_permissions_are_reported() -> None:
    workflow = broken(lambda w: w.pop("permissions"))
    assert len(check_permissions(workflow)) == 1


def test_job_level_permissions_are_accepted() -> None:
    def move_permissions(w: Workflow) -> None:
        job_of(w)["permissions"] = w.pop("permissions")

    assert check_permissions(broken(move_permissions)) == []


@pytest.mark.parametrize(
    "reference",
    [
        "actions/checkout@main",
        "actions/checkout@master",
        "actions/checkout@v4",
        "actions/checkout",
        "actions/checkout@abc123",
        "docker://alpine:3.20",
    ],
)
def test_unpinned_action_is_reported(reference: str) -> None:
    workflow = broken(lambda w: job_of(w)["steps"].append({"uses": reference}))
    assert len(check_pinned_actions(workflow)) == 1


@pytest.mark.parametrize(
    "reference",
    [
        "actions/checkout@v4.2.2",
        "actions/checkout@4.2.2",
        "actions/checkout@" + "a" * 40,
        "./.gitea/actions/local",
    ],
)
def test_pinned_action_is_accepted(reference: str) -> None:
    workflow = broken(lambda w: job_of(w)["steps"].append({"uses": reference}))
    assert check_pinned_actions(workflow) == []


def test_long_run_block_is_reported() -> None:
    script = "\n".join(f"echo {number}" for number in range(MAX_RUN_LINES + 1))
    workflow = broken(lambda w: job_of(w)["steps"].append({"run": script + "\n"}))
    assert len(check_inline_scripts(workflow)) == 1


def test_run_block_at_the_limit_is_accepted() -> None:
    script = "\n\n".join(f"echo {number}" for number in range(MAX_RUN_LINES))
    workflow = broken(lambda w: job_of(w)["steps"].append({"run": script}))
    assert check_inline_scripts(workflow) == []
