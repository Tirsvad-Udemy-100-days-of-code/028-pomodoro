# Review Record: CI workflow after pinning the apt packages (full re-review of RC-013)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Initial version | [f5f2575] |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001] (.gitea/workflows/ci.yml)
- Checklist used: [QC-WF-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | Meets QC-YML-001; see the review record of the YAML checklist for the same file. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | Only in `.gitea/workflows/`, extension `.yml`; no copy in `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | Declares `name`, `on` (push to main, pull_request to main with paths, workflow_dispatch) and `jobs`. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers, inputs, secrets (none), changes outside the repository (none) and the milestone. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Every step has a unique descriptive `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | actionlint 1.7.12 (actionlint-py 1.7.12.25) reports no finding; version stated in the header. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | `permissions: contents: read` at workflow level; no job needs more. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | actions/checkout@v4.2.2 and actions/setup-python@v5.3.0, exact release tags. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secret used or written. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No event field or input is interpolated into a `run:` script; `github.ref` appears only in `concurrency.group`. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | Uses `pull_request`, not `pull_request_target` or `workflow_run`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | N-A | The workflow changes nothing outside the runner. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | No token is used beyond the default read-only one. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-24.04` (an explicit image, not `latest`) and `timeout-minutes: 10`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group per ref with `cancel-in-progress: true` (a check, not a publisher). |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Pull requests are filtered by `branches` and `paths`; push only on main. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Python 3.13, pip 26.2.1, dev tools (pyproject.toml), `libtk8.6=8.6.14-1build1` and `xvfb=2:21.1.12-1ubuntu1.8` are pinned, with the values in one `env` block; the header says what to do when the archive drops a version. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | The install takes seconds; a cache would add moving parts. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | Each step is one tool; the test step prints the pytest summary (63 passed observed). |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | The longest `run:` block is four lines (apt-get update and a two-line apt-get install). |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | N-A | A single workflow; nothing is shared between workflows or repositories. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run observed on Gitea 1.27.3 (pull_request) on the `ubuntu-24.04` label: pinned packages installed (log: `Setting up libtk8.6 (8.6.14-1build1)`, `xvfb (2:21.1.12-1ubuntu1.8)`), 63 tests passed. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Fail | No repository test of the workflow files; actionlint was run by hand. Optional criterion, deferred. |

## Overall Verdict

Go — every Mandatory criterion of QC-WF-001 passes or is not applicable with the reason stated. Condition 17 of RC-013 is closed: the apt packages and the runner image are pinned and the run on Gitea 1.27.3 passed 63 tests. Only the direct packages are pinned; their dependencies follow the pinned Ubuntu 24.04 archive.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether a static test of the workflow files is worth adding (optional criterion 24) | S01 | not scheduled |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[f5f2575]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/f5f2575c4a4aa2837c85631624383c8d7dcab2d3
