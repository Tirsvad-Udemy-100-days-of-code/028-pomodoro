# Traceability Matrix: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability can be measured. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [DICT-001], [MIL-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [DICT-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [BC-001], [MIL-003] | - | [RC-007] |

## Coverage Notes

- Types with no instance yet: KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, GOV, ADR. They are not used by this single-screen exercise (see the Open Issues of [PP-001]).
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no `RC-*` exists. [PP-001] has no QC checklist in the framework, so it has no review record.
- Source code (`PY`) rows are added when a milestone's code is reviewed against `QC-PY-001`.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[MIL-001]: ../milestones/mil-001-project-scaffold.md
[MIL-002]: ../milestones/mil-002-timer-ui.md
[MIL-003]: ../milestones/mil-003-countdown-cycle.md
[MIL-004]: ../milestones/mil-004-documentation.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-dictionary.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
