# Stakeholder Analysis: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-002 | [75fa7ed] |

---

## Purpose

This analysis identifies who has influence over, or interest in, the Pomodoro Timer project, so that the Business Case, the plan and the reviews address the right people. It follows the power/interest grid and gives every stakeholder a stable ID that other artifacts use for ownership, review and RACI.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A complete, correct solution of the Day 28 assignment that is easy to maintain and to show |
| S02 | Udemy coursists | Fellow participants of the course | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code that keeps the assignment's function names, with README instructions to run it, so they can compare solutions |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, reviews and accepts every artifact; every objective of the Business Case is S01's.
- **Keep Informed (S02):** S02 cannot change the project but depends on the result and will compare it with their own; they need the instructions and the assignment's names.
- **Monitor (S03):** S03 reads the repository occasionally; the repository front page (description, topics, README) is enough.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | The timer behaves as the lectures describe | Functionality |
| S01 | Rules are tested and the process is reviewed | Reliability |
| S02 | Code is readable and keeps the assignment's function names | Supportability (+ Design constraint) |
| S02 | Instructions to run the program and the tests on their platform | Usability |
| S03 | The repository explains itself: description, topics, README | Usability |
| S03 | No runtime dependencies to install | Implementation constraint (+ Supportability) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Pull request with closed issues and review records | Every milestone |
| S02 | README and wiki | Once, then on change | Run and test instructions in three languages | Documentation milestone |
| S03 | Repository page | Once, then on change | Description, topics, README with screenshot | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's single-script shape and names; S01 wants tested rules separated from the user interface | S01, S02 | Keep `start_timer`, `reset_timer` and `count_down` as functions of the user-interface module, and put only the pure rules in a separate module |
| S03 wants no dependencies; testing needs pytest | S03, S01 | pytest is a development dependency only; the runtime dependency list is empty |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Timer behaves as in the lectures | O1 in [BC-001] |
| S01 | Rules are tested | O3 in [BC-001] |
| S02 | Assignment's function names and constants | O2 in [BC-001] |
| S02 | Instructions to run, in their language | O4 and O5 in [BC-001] |
| S03 | Description, topics, README | O5 and O6 in [BC-001] |
| S03 | No runtime dependencies | O4 in [BC-001] |

## Sign-Off

| Role | Stakeholder ID | Status |
| --- | --- | --- |
| Product Owner | S01 | Pending review |

---

[BC-001]: ./business-case.md
[75fa7ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/75fa7ed494597311f4cf762cf2e83ac36e22d153
