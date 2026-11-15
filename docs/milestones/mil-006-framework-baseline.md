# MIL-006 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [PP-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether Pomodoro Timer has the baseline of the framework: the adopted framework release, the wiki in English, Danish and Malay in the framework's shape (language line first, one sidebar, a Project Documents page), the README in the framework template with its appendix, complete licence metadata, a traceability matrix that covers every document and reviewed documents, merged to the default branch with a green build. The work is delivered on the branch `mil-006-baseline` and one pull request.

## Deliverable

A merged pull request that holds: the updated Business Case, Stakeholder Analysis, Project Plan, Domain Dictionary, milestones MIL-001 to MIL-005 and Traceability Matrix with their review records; the wiki in English, Danish and Malay in `docs/wiki/`; the README in the framework template; `pyproject.toml` with complete licence metadata; and the framework release adopted by the project. The program and its tests do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001, DICT-001, MIL-001 to MIL-005 and MIL-006 each have an `Accepted` Version History row and a review record with the verdict `Go` | All of them | Any missing or `Go-with-conditions` |
| 2 | `python -m pytest` runs | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Install, Usage and Project-Documents in en, da and ms | 12 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license`, `license-files`, the authors and the project URLs for the documentation and the issue tracker | All set | Any missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |
| 7 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] accepted | Documents and baselines the finished program, its tests and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 to O6 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| O7 | Criteria 1, 3, 4, 5 and 7 (documents, wiki, README, licence and issues) |
| Success criterion 8 | Criteria 1 and 6 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case assumption requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills and hooks, add `.editorconfig`, track `.env.example` and ignore the local prompt logs, so the project follows the same rules as the other projects of the portfolio. | No | O7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, add concern IDs to the Stakeholder Analysis, set the domain of the dictionary and the earlier milestones and put the dictionary rows in order, extend the traceability matrix and review each changed document against its QC checklist, so the plan-first gate is met. | No | O7 |
| 3 | Bring the wiki to the framework's shape | Rename the Danish and Malay pages to the framework's file names, put the language line first in the framework's form on every page, write the sidebar in the framework shape and add the Project-Documents page in English, Danish and Malay. | No | O7 |
| 4 | Bring the README to the framework template | Keep the original text of the README under the template's sections, add the table of contents, the links and the appendix of project documents, so the README is complete and checkable. | No | O7 |
| 5 | Complete the licence metadata | Set the licence expression, `license-files`, the authors and the project URLs in `pyproject.toml` (and the build requirement that the licence expression needs), so package tools can read them. | No | O7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-005]: ./mil-005-workflow-static-test.md
