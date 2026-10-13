# MIL-001 Project scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-004 | [75fa7ed] |

---

## Purpose

Decide whether the repository has the project structure, configuration, constants, source documentation set-up and continuous integration that the later milestones build on, before any feature code is written.

## Deliverable

A repository branch with `pyproject.toml`, a Python `.gitignore`, the `src/pomodoro/` and `tests/` layout, `constants.py` holding the assignment's constants, the tomato image, a `Doxyfile` and a continuous integration workflow, with `pytest` running and passing on the layout.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python = ">=3.13"`, an empty runtime `dependencies` list and `pytest` as a development dependency | Met | Not met |
| 2 | `.gitignore` ignores `.venv/`, `.env`, Python caches and the Doxygen output | Met | Not met |
| 3 | `src/pomodoro/constants.py` defines `PINK`, `RED`, `GREEN`, `YELLOW`, `FONT_NAME`, `WORK_MIN`, `SHORT_BREAK_MIN` and `LONG_BREAK_MIN` with the values of the course starting file | Met | Not met |
| 4 | `pytest` runs from a fresh `.venv` and exits 0 | Met | Not met |
| 5 | `doxygen Doxyfile` runs with 0 warnings | Met | Not met |
| 6 | The workflow file has explicit permissions, pinned actions and timeouts | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase after the baseline documents |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2 (constants), O4 (reproducible set-up), O5 (Doxygen) | [BC-001] |
| Success criteria 4 and 5 | [BC-001] |

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
| 1 | Add pyproject.toml and .gitignore | Project metadata with `requires-python >=3.13`, an empty runtime dependency list, a `dev` extra with pytest and the pytest `pythonpath` setting for `src`; a Python `.gitignore` that also ignores `.venv/` and `.env`. Satisfies the configuration constraints of the Business Case. | No | |
| 2 | Create the package layout and constants.py | Create `src/pomodoro/` and `tests/`, add the tomato image as package data, and put the course's colour, font and duration constants into `constants.py` unchanged so participants can compare solutions (objective O2). | No | |
| 3 | Add a Doxyfile | Doxygen configuration for `src/` with Doxygen-style comments (objective O5); output goes to a git-ignored folder and the build must have no warnings. | No | |
| 4 | Add the continuous integration workflow | A Gitea Actions workflow that installs the project into a venv on Python 3.13 and runs pytest, following the workflow checklist (least privilege, pinned actions, timeouts, concurrency). | No | |

---

[BC-001]: ../business-case.md
[75fa7ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/75fa7ed494597311f4cf762cf2e83ac36e22d153
