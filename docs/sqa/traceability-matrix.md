# Traceability Matrix: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Added the MIL-002 source row (RC-011) | [dec1e6b] |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Added the MIL-003 source row (RC-012) | [5b3d012] |

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
| [PY-MIL-001] | PY | - | - | [MIL-001] | - | [RC-008] |
| [WF-MIL-001] | WF | - | - | [MIL-001] | - | [RC-009] |
| [YML-MIL-001] | YML | - | - | [MIL-001] | - | [RC-010] |
| [PY-MIL-002] | PY | - | - | [MIL-002] | - | [RC-011] |
| [PY-MIL-003] | PY | - | - | [MIL-003] | - | [RC-012] |

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
[PY-MIL-001]: ../../src/pomodoro/constants.py
[WF-MIL-001]: ../../.gitea/workflows/ci.yml
[YML-MIL-001]: ../../.gitea/workflows/ci.yml
[RC-008]: ./reviews/rc-008-mil-001-python.md
[RC-009]: ./reviews/rc-009-mil-001-workflow.md
[RC-010]: ./reviews/rc-010-mil-001-yaml.md
[PY-MIL-002]: ../../src/pomodoro/app.py
[RC-011]: ./reviews/rc-011-mil-002-python.md
[dec1e6b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/dec1e6b5b0fa5a56e787755b2e62a78208e28eb5
[PY-MIL-003]: ../../src/pomodoro/timer_rules.py
[RC-012]: ./reviews/rc-012-mil-003-python.md
[5b3d012]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/5b3d01272307e42dee6f55467fd18ad9e83937fa
