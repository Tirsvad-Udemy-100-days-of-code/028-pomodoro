# Traceability Matrix: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [DICT-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | AI for S01 | AI as stand-in for S01 | Added the MIL-005 row (RC-017) | [faf143b] |
| 2026-10-13 | Deprecated | AI for S01 | AI as stand-in for S01 | Added the MIL-005 test and the delta review rows (RC-018, RC-019) | [2566601] |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline milestone, the wiki row, the new review records, the review of the plan, the concern coverage and the domain education; reviewed in autonomous mode, not independent | [3da20f5] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the delta review RC-031 of the workflow after the xvfb pin update; reviewed in autonomous mode, not independent | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability can be measured. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [DICT-001], [MIL-001], [MIL-006] | [RC-020] (Go, re-review of the whole document), [RC-001] |
| [SA-001] | SA | en | education | [BC-001] | [PP-001], [DICT-001] | [RC-021] (Go, re-review of the whole document), [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-022] (Go, review of the whole document) |
| [DICT-001] | DICT | en | education | [BC-001], [SA-001] | - | [RC-023] (Go, re-review after the domain change and the new row order), [RC-003] |
| [MIL-001] | MIL | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-024] (Go, re-review after the metadata change), [RC-004] |
| [MIL-002] | MIL | en | education | [BC-001], [MIL-001] | [MIL-003] | [RC-025] (Go, re-review after the metadata change), [RC-005] |
| [MIL-003] | MIL | en | education | [BC-001], [MIL-002] | [MIL-004] | [RC-026] (Go, re-review after the metadata change), [RC-006] |
| [MIL-004] | MIL | en | education | [BC-001], [MIL-003] | - | [RC-027] (Go, re-review after the metadata change), [RC-007] |
| [PY-MIL-001] | PY | - | - | [MIL-001] | - | [RC-008] |
| [WF-MIL-001] | WF | - | - | [MIL-001] | - | [RC-009] |
| [YML-MIL-001] | YML | - | - | [MIL-001] | - | [RC-010] |
| [PY-MIL-002] | PY | - | - | [MIL-002] | - | [RC-011] |
| [PY-MIL-003] | PY | - | - | [MIL-003] | - | [RC-012] |
| [WF-MIL-003] | WF | - | - | [MIL-003] | - | [RC-013] |
| [YML-MIL-003] | YML | - | - | [MIL-003] | - | [RC-014] |
| [WF-CI-PIN] | WF | - | - | [MIL-003] | - | [RC-015] |
| [YML-CI-PIN] | YML | - | - | [MIL-003] | - | [RC-016] |
| [MIL-005] | MIL | en | education | [BC-001], [MIL-004] | [MIL-006] | [RC-028] (Go, re-review after the metadata change), [RC-017] |
| [PY-MIL-005] | PY | - | - | [MIL-005] | - | [RC-018] |
| [WF-CI] | WF | - | - | [MIL-003] | [PY-MIL-005] | [RC-031] (Go, delta re-review of criteria 17 and 22), [RC-019] |
| [MIL-006] | MIL | en | education | [BC-001], [PP-001], [MIL-005] | - | [RC-029] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-006] | - | [RC-030] (Go-with-conditions) |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002], [MIL-003] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-003], [MIL-005], [MIL-006] | - | - | Covered |
| CN-003 | [MIL-002], [MIL-003] | - | - | Covered |
| CN-004 | [MIL-004] | - | - | Covered |
| CN-005 | [MIL-004] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |
| CN-007 | [MIL-006] | - | - | Covered |

## Coverage Notes

- Types with no instance yet: KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, GOV, ADR. They are not used by this single-screen exercise (see the Open Issues of [PP-001]).
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no `RC-*` exists.
- Source code (`PY`) rows are added when a milestone's code is reviewed against `QC-PY-001`.
- The domain of every artifact is `education` since [MIL-006]; the earlier review records state the former domain `it` as it was at the time.
- [PP-001] is reviewed against `QC-PP-001`, which the framework added after the plan was written ([RC-022]).
- The source code and the workflow are reviewed in the records RC-008 to RC-019 and not again in [MIL-006], which changes no source file.
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

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
[PY-MIL-003]: ../../src/pomodoro/timer_rules.py
[RC-012]: ./reviews/rc-012-mil-003-python.md
[WF-MIL-003]: ../../.gitea/workflows/ci.yml
[YML-MIL-003]: ../../.gitea/workflows/ci.yml
[RC-013]: ./reviews/rc-013-mil-003-workflow.md
[RC-014]: ./reviews/rc-014-mil-003-yaml.md
[WF-CI-PIN]: ../../.gitea/workflows/ci.yml
[YML-CI-PIN]: ../../.gitea/workflows/ci.yml
[RC-015]: ./reviews/rc-015-ci-apt-pins-workflow.md
[RC-016]: ./reviews/rc-016-ci-apt-pins-yaml.md
[MIL-005]: ../milestones/mil-005-workflow-static-test.md
[RC-017]: ./reviews/rc-017-mil-005.md
[faf143b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/faf143bd8c5ca511c76053c7bcd2c5984a4c9cfc
[PY-MIL-005]: ../../tests/test_workflows.py
[WF-CI]: ../../.gitea/workflows/ci.yml
[RC-018]: ./reviews/rc-018-mil-005-python.md
[RC-019]: ./reviews/rc-019-mil-005-workflow-delta.md
[2566601]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/256660172a1741f5cd3651bcb7d0696f8775f52d
[MIL-006]: ../milestones/mil-006-framework-baseline.md
[RC-020]: ./reviews/rc-020-business-case-baseline.md
[RC-021]: ./reviews/rc-021-stakeholder-analysis-baseline.md
[RC-022]: ./reviews/rc-022-project-plan-baseline.md
[RC-023]: ./reviews/rc-023-dictionary-baseline.md
[RC-024]: ./reviews/rc-024-milestone-001-baseline.md
[RC-025]: ./reviews/rc-025-milestone-002-baseline.md
[RC-026]: ./reviews/rc-026-milestone-003-baseline.md
[RC-027]: ./reviews/rc-027-milestone-004-baseline.md
[RC-028]: ./reviews/rc-028-milestone-005-baseline.md
[RC-029]: ./reviews/rc-029-milestone-006.md
[RC-030]: ./reviews/rc-030-wiki.md
[3da20f5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/3da20f512ebb3297bac84d8e9146b55bd1a30098
[RC-031]: ./reviews/rc-031-ci-xvfb-pin-workflow-delta.md
