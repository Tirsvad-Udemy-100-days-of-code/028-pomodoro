# Stakeholder Analysis: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-006] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-002 | [75fa7ed] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table and a conflict about the stand-in reviewer; spelled out FURPS+; set the domain to education; reviewed in autonomous mode, not independent | pending |

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

FURPS+ stands for Functionality, Usability, Reliability, Performance and Supportability, plus design, implementation, interface and physical constraints.

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The timer behaves as the lectures describe | Functionality |
| CN-002 | S01 | Rules are tested and the process is reviewed | Reliability |
| CN-003 | S02 | Code is readable and keeps the assignment's function names | Supportability (+ Design constraint) |
| CN-004 | S02 | Instructions to run the program and the tests on their platform | Usability |
| CN-005 | S03 | The repository explains itself: description, topics, README | Usability |
| CN-006 | S03 | No runtime dependencies to install | Implementation constraint (+ Supportability) |
| CN-007 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's shape | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Pull request with closed issues and review records | Every milestone |
| S02 | README and wiki | Once, then on change | Run and test instructions in three languages | Documentation milestone |
| S03 | Repository page | Once, then on change | Description, topics, README with screenshot | Documentation milestone |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-006] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's single-script shape and names; S01 wants tested rules separated from the user interface | S01, S02 | Keep `start_timer`, `reset_timer` and `count_down` as functions of the user-interface module, and put only the pure rules in a separate module |
| S03 wants no dependencies; testing needs pytest | S03, S01 | pytest is a development dependency only; the runtime dependency list is empty |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Timer behaves as in the lectures (CN-001) | O1 in [BC-001] |
| S01 | Rules are tested and the process is reviewed (CN-002) | O3 in [BC-001] |
| S02 | Assignment's function names and constants (CN-003) | O2 in [BC-001] |
| S02 | Instructions to run, in their language (CN-004) | O4 and O5 in [BC-001] |
| S03 | Description, topics, README (CN-005) | O5 and O6 in [BC-001] |
| S03 | No runtime dependencies (CN-006) | O4 in [BC-001] |
| S01 | The project follows the common baseline of the framework (CN-007) | O7 in [BC-001] |

## Sign-Off

| Role | Stakeholder ID | Status |
| --- | --- | --- |
| Product Owner | S01 | Pending review |

The changes of the baseline milestone were reviewed by the AI stand-in for S01 in the review record of this document (Go), autonomous, not independent; the Sign-Off row stays Pending review until S01 confirms.

---

[BC-001]: ./business-case.md
[75fa7ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/75fa7ed494597311f4cf762cf2e83ac36e22d153
[MIL-006]: ./milestones/mil-006-framework-baseline.md
