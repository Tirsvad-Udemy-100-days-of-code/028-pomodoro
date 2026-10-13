# Business Case: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-001 | pending |

---

## Executive Summary

The project builds a desktop Pomodoro timer in Python with Tkinter, as the Day 28 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp". The timer alternates 25 minutes of work with 5-minute breaks and a longer break after four work sessions, shows a tomato image, and counts completed work sessions with check marks. The result is published as a readable, runnable repository with instructions, tests, source documentation and a three-language wiki, so that other course participants and visitors can learn from it. The project proceeds.

## Methodological and Standards Foundation

- Process: the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed).
- Quality model: ISO/IEC 25010:2023 characteristics, as every QC criterion is tagged.
- Design: Larman, *Applying UML and Patterns*, kept proportionate to a one-screen application: the timer rules are separated from the user interface (Clean Architecture, dependencies point inward).
- Code: PEP 8 (Python Enhancement Proposal 8), type hints, `QC-PY-001` for Python source code.

## Problem Statement

The assignment is a set of lectures that ends with a working Pomodoro timer, but a course participant is left with a single script and no tests, no reproducible set-up and no documentation. Solutions shared between participants are hard to run and compare because the set-up differs and the function names drift from the assignment.

## Business Opportunity

A complete, tested and documented solution gives the Product Owner a reference result of the course day, gives other participants a solution that runs the same way on Windows, Linux and macOS, and gives repository visitors a worked example of a small Tkinter application with a quality process around it.

## Objectives

1. **O1** Deliver a Tkinter Pomodoro timer that follows the Day 28 lectures: tomato canvas, title label, `MM:SS` countdown, start and reset buttons, check marks.
2. **O2** Keep the assignment's function names (`start_timer`, `reset_timer`, `count_down`) and constants (`PINK`, `RED`, `GREEN`, `YELLOW`, `FONT_NAME`, `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`) so that participants can compare solutions.
3. **O3** Separate the timer rules from the user interface so the rules are tested with pytest without a display.
4. **O4** Make the project reproducible: Python 3.13 or later, a local `.venv`, `pyproject.toml`, no runtime dependency beyond the standard library.
5. **O5** Document it: README from the project template, Doxygen source documentation, and a wiki in English, Danish and Bahasa Malaysia, with screenshots.
6. **O6** Present the repository clearly on the git host: description and topics.

## Scope

### In Scope

- The timer application and its tests under `src/` and `tests/`.
- `pyproject.toml`, `constants.py`, Python `.gitignore`, `Doxyfile`, continuous integration workflow.
- README, wiki (English, Danish, Bahasa Malaysia) and screenshots.
- Repository description and topics on the git host.
- Planning documents under `docs/` and one pull request per milestone.

### Out of Scope

- Sound or desktop notifications, configurable durations in the user interface, persistence of statistics.
- Packaging for PyPI, executable bundles, or a web or mobile version.
- Runtime dependencies other than the Python standard library.
- Languages other than English, Danish and Bahasa Malaysia for the wiki.

## Expected Benefits

### Tangible Benefits

- A runnable application and a passing automated test suite.
- A README that lets a new reader run the application and the tests in minutes.
- A wiki in three languages and generated source documentation.

### Intangible Benefits

- A worked example of the framework's plan-first, reviewed workflow on a small project.
- A shared reference that eases comparison between course participants.

## Strategic Alignment

The project supports the Product Owner's learning goal in the 100 Days of Code course and the practice of delivering even small exercises with documented requirements, tests and review, as the framework prescribes.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Application follows the lectures | All of O1 present: tomato canvas, title label, `MM:SS` countdown, start and reset buttons, check marks | Manual check against the milestone's Go criteria, with a screenshot |
| 2 | Cycle logic is correct | 8 sessions follow the order work, short, work, short, work, short, work, long; a check mark is added per completed work session | Automated tests pass |
| 3 | Tests | 100 % of the timer-rules module covered by passing tests; the full suite passes on Python 3.13 | `pytest` exit code 0; coverage report |
| 4 | Reproducible set-up | A fresh clone runs the application and the tests following the README alone, on Windows PowerShell | The documented commands run without error |
| 5 | Runtime dependencies | 0 packages other than the standard library | `pyproject.toml` has an empty `dependencies` list |
| 6 | Documentation | README sections of the project template, Doxygen build with 0 warnings, 3 wiki languages each with a screenshot | `doxygen` output; wiki page list |
| 7 | Repository presentation | A description and at least 5 topics set on the git host | Repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Tkinter is missing on some Linux installs (Debian splits it into `python3-tk`) | A reader cannot run the application | The README names the package per platform; the rules module has no Tkinter import so tests run without it |
| User-interface tests need a display, which continuous integration runners lack | Flaky or failing continuous integration | Test the rules module headless; the user-interface test skips when no display is available |
| The framework's review rules need a person for the language criteria, which an autonomous run cannot supply | A document stays on Go-with-conditions | The verdict is recorded as such and listed in the run summary for S01 to confirm |
| Secrets in `.env` leak into the repository | Credential exposure | `.env` is ignored by git, never imported by the project and never printed |
| The wiki repository is not enabled on the git host | Wiki pages cannot be published | Keep the pages as files in the repository and report the blocker |

## Assumptions

- The Product Owner's language is English and the domain is IT (confirmed by S01 in chat on 2026-10-13).
- The git host is Gitea at `git.tirsystem.com`, the repository exists and a personal access token is available in a local `.env` file used only for personal tooling.
- "Python greater than 3.13" is read as Python 3.13 or later (`requires-python = ">=3.13"`).
- Tkinter ships with the Python installation of the target platforms.

## Constraints

- Python 3.13 or later, `venv` for the environment, `pytest` for tests, `pyproject.toml` for configuration.
- Constants live in `constants.py`; source comments use Doxygen syntax.
- Folder structure `src/`, `tests/`, `docs/`.
- Avoid runtime dependencies unless needed.
- Work on branches and pull requests, one per milestone; nothing under `src/` or `tests/` before its milestone is accepted with a Go review.
- Duration: finished within one week, by 2026-10-20.

## Cost–Benefit Assessment

A qualitative assessment is justified: the project is a learning exercise with no revenue and no external budget.

| Costs | Benefits |
| --- | --- |
| About two days of effort by S01 and the AI assistant | A reusable, reviewed reference solution (O1 to O6) |
| Maintenance of three wiki languages | Readable documentation for S02 and S03 in their own language |
| Review effort per artifact | A repeatable quality process on a small example |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a complete, correct solution |
| S02 | Receives readable, runnable code with the assignment's function names and run instructions |
| S03 | Receives a clear repository description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the cost is low and every objective is verifiable with tests, a documented set-up and a screenshot.

---

[SA-001]: ./stakeholder-analysis.md
