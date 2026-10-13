# MIL-004 Documentation and repository presentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-007 | pending |

---

## Purpose

Decide whether the project is documented well enough for S02 and S03 to run it and understand it, and whether the repository presents itself clearly on the git host.

## Deliverable

`README.md` built from the project's template with a screenshot, wiki pages in English, Danish and Bahasa Malaysia with screenshots, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `README.md` has every section of the project's README template, in order, with commands for Windows PowerShell, Linux Debian and macOS | Met | Not met |
| 2 | The README documents creating and using a local `.venv` and `python -m pip install --upgrade pip` | Met | Not met |
| 3 | The README and each wiki language contain a screenshot of the running application | Met | Not met |
| 4 | Wiki pages exist in English, Danish and Bahasa Malaysia | Met | Not met |
| 5 | `doxygen` builds the source documentation with 0 warnings | Met | Not met |
| 6 | The repository has a description and at least 5 topics on the git host | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | Documents and screenshots the finished application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4 and O5 (set-up, README, Doxygen, wiki) | [BC-001] |
| O6 (description and topics) | [BC-001] |
| Success criteria 4, 6 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-20 — inside the one-week duration of [BC-001] (finished by 2026-10-20).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Take screenshots of the application | Run the finished application and capture a screenshot of the idle window and of a running work session, saved under `docs/images/` for the README and the wiki. | No | |
| 2 | Write README.md | Fill the Product Owner's README template: requirements, set-up on Windows PowerShell, Linux Debian and macOS with `.venv` and `pip install --upgrade pip`, run, tests, continuous integration, Doxygen build, project layout, license. | No | |
| 3 | Write the wiki in three languages | Home, Install and Usage pages in English, Danish and Bahasa Malaysia, following the example wiki of the TirSystem github-action repository, each with a screenshot. | No | |
| 4 | Set repository description and topics | Set a description and topics on the git host repository through its API, using the personal token from the local `.env` file, which the project never imports. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-countdown-cycle.md
