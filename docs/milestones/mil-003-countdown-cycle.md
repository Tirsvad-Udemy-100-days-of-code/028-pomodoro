# MIL-003 Countdown and Pomodoro cycle

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-006 | pending |

---

## Purpose

Decide whether the timer works as a Pomodoro timer: it counts down in `MM:SS`, alternates work and breaks as the technique prescribes, marks completed work sessions and can be reset.

## Deliverable

The timer rules module and the wired user interface: `start_timer`, `count_down` and `reset_timer`, with tests for the rules and the controller.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The countdown text shows `M:SS` with a leading zero for seconds below ten (`4:05`, `0:00`, `25:00`) | Met | Not met |
| 2 | Eight consecutive sessions are work, short break, work, short break, work, short break, work, long break, and the title label shows `Work` (GREEN), `Break` (PINK) or `Break` (RED) accordingly | Met | Not met |
| 3 | A check mark is added after each completed work session | Met | Not met |
| 4 | Reset cancels the pending `after` call, clears the check marks, sets `00:00`, restores the title `Timer` and sets the repetition counter to zero | Met | Not met |
| 5 | The timer-rules module has 100 % test coverage and no Tkinter import | Met | Not met |
| 6 | `pytest` passes | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Needs the window and its widgets |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 (countdown, cycle, check marks, reset) | [BC-001] |
| O2 (function names) | [BC-001] |
| O3 (rules tested without display) | [BC-001] |
| Success criteria 2 and 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-18 — inside the one-week duration of [BC-001] (finished by 2026-10-20).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the timer rules module | Pure functions for the `MM:SS` text, the session kind and length for a repetition number (the modulo rules of the lecture) and the check-mark text, with no Tkinter import so they are tested without a display (objective O3). | No | |
| 2 | Implement start_timer and count_down | `start_timer` picks the session from the repetition counter, sets the title label and starts `count_down`; `count_down` updates the canvas text each second through `after` and starts the next session at zero, as in the lectures. | No | |
| 3 | Implement reset_timer and the check marks | `reset_timer` cancels the pending `after`, clears the check marks and timer text, restores the title and resets the repetition counter (the bug fix of the final lecture); check marks are shown after completed work sessions. | No | |
| 4 | Test the rules and the controller | pytest tests for the rules module and for the controller with a fake scheduler, so the cycle is tested without waiting for real time. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-timer-ui.md
