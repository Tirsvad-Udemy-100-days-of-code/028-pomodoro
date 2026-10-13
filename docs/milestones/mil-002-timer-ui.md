# MIL-002 Timer user interface

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-005 | pending |

---

## Purpose

Decide whether the window of the Pomodoro timer matches the Day 28 lectures (canvas with tomato, countdown text, title label, buttons and check-mark label in a grid) and can be started from the command line.

## Deliverable

The `pomodoro` package opens a Tkinter window with the tomato canvas, the `00:00` timer text, the `Timer` title label, Start and Reset buttons and an empty check-mark label, started with `python -m pomodoro`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pomodoro` opens a window titled `Pomodoro` | Met | Not met |
| 2 | The window shows the tomato image on a canvas with the text `00:00` on it, and the canvas has no border (`highlightthickness=0`) | Met | Not met |
| 3 | The window shows a title label `Timer` in `GREEN`, a Start button, a Reset button and an empty check-mark label in a grid layout | Met | Not met |
| 4 | Colours and font come from `constants.py` only | Met | Not met |
| 5 | The window test passes, or is skipped with a stated reason when no display exists | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the package layout, constants and tomato image |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 (user interface of the lectures) | [BC-001] |
| Success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — inside the one-week duration of [BC-001] (finished by 2026-10-20).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Build the window and canvas with tomato and timer text | Create the window, the canvas sized to the tomato image, `create_image` with a `PhotoImage` kept in a variable and the `create_text` countdown, as in the "UI Setup" lecture, with background colours and padding from the constants. | No | |
| 2 | Add title label, buttons and check-mark label in a grid | Add the `Timer` label, the Start and Reset buttons and the check-mark label with the grid layout the lecture suggests; the callbacks are wired in the next milestone. | No | |
| 3 | Add the entry point | `python -m pomodoro` and a `main()` function build the window and run the main loop, so the program is started the same way on every platform. | No | |
| 4 | Test the window construction | A pytest test that builds the window and checks its widgets and texts; it is skipped when Tkinter or a display is unavailable, so continuous integration stays green. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-scaffold.md
