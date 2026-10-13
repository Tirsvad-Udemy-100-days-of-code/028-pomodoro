# MIL-005 Workflow static test

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-017 | [faf143b] |

---

## Purpose

Decide whether the repository's continuous integration workflow is checked by an automated test on every pull request, so that a broken or unsafe workflow file is found by the test suite and not by a failed run. This closes the optional criterion 24 of `QC-WF-001` left open in the review records of the workflow.

## Deliverable

`tests/test_workflows.py`, which reads every file in `.gitea/workflows/` with a safe YAML loader and asserts the workflow rules of the project, with the loader and its type stubs added as pinned development dependencies.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` lists PyYAML and its type stubs, pinned, in the `dev` extra only; the runtime `dependencies` list is still empty | Met | Not met |
| 2 | The test parses each file in `.gitea/workflows/` with `yaml.safe_load` and fails on a file that is not valid YAML or has a duplicate key | Met | Not met |
| 3 | The test asserts that every workflow has `name`, `on` and `jobs`, and that every job has `runs-on` and `timeout-minutes` | Met | Not met |
| 4 | The test asserts that `permissions` is declared explicitly, at workflow level or on every job | Met | Not met |
| 5 | The test asserts that every `uses:` reference is pinned to an exact release tag or a commit SHA, never a branch | Met | Not met |
| 6 | The test asserts that no `run:` block is longer than five lines | Met | Not met |
| 7 | A deliberately broken workflow in the test data makes the matching assertion fail (the test tests itself) | Met | Not met |
| 8 | `ruff`, `mypy --strict` and `pytest` pass locally and in the continuous integration run | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The workflow, the README and the review records the test and its documentation refer to exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3 (checks that run without a display) and O4 (reproducible set-up) | [BC-001] |
| Success criterion 5 (no runtime dependency) | [BC-001] |
| Optional criterion 24 of `QC-WF-001` | Review records of the workflow |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — inside the one-week duration of [BC-001] (finished by 2026-10-20).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add PyYAML as a pinned development dependency | Add `PyYAML` and `types-PyYAML` with exact versions to the `dev` extra of `pyproject.toml`, so the test can use a safe YAML loader under `mypy --strict`. The runtime dependency list stays empty (Business Case success criterion 5). | No | |
| 2 | Write the workflow static test | `tests/test_workflows.py` parses the files in `.gitea/workflows/` and asserts valid YAML without duplicate keys, the required keys, explicit permissions, a runner and a timeout per job, pinned actions and no inline script above five lines; a broken sample proves each assertion can fail. | No | |
| 3 | Document the test | Name the workflow test in the README's "Run the tests" section and record the closed criterion 24 in the review record of the workflow. | No | |

---

[BC-001]: ../business-case.md
[MIL-004]: ./mil-004-documentation.md
[faf143b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/faf143bd8c5ca511c76053c7bcd2c5984a4c9cfc
