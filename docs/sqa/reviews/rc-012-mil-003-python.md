# Review Record: Python source of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Initial version | [5b3d012] |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-003] (src/pomodoro/timer_rules.py, app.py, constants.py and tests/test_timer_rules.py, tests/test_app.py)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case functions and modules, PascalCase SessionKind and Scheduler, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (session_kind, format_time, check_marks); assignment names start_timer, count_down, reset_timer, reps, timer kept. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format --check pass (ruff 0.17.0), no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function annotated incl. -> None; mypy --strict passes on 9 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Rules raise ValueError for out-of-range input; no bare except, none swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtins shadowed (parameter id_ for the after id). |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections in code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings with Doxygen @brief/@param/@return/@throws on public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging or printing. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists (PP-001); classes follow the lecture, the Scheduler protocol is the one added port. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 24 rule tests and controller tests with a fake scheduler; behaviour-named, no network, no real time, no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict passes; Callable[..., object] and object args need no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; dev tools pinned. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Session lengths, titles, modulo numbers and check mark are constants defined once; kind-to-length and kind-to-title mappings are single module-level tables. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | timer_rules.py imports only enum and constants (asserted by a test with ast); app.py depends on the Scheduler protocol, not on a concrete clock. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Rules and window are separate modules with one reason to change each; the cycle is a table, not an isinstance chain; Scheduler is a one-port protocol received by the app. |

## Overall Verdict

Go — every Mandatory criterion of QC-PY-001 passes or is not applicable with the reason stated. Tests: 61 to 62 pass and 1 to 2 skip per run; the skips are the known environmental Tk initialisation failure of this Microsoft Store Python and land on different tests each run. timer_rules.py and app.py have 100 % coverage.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review in the pull request if it looks wrong | S01 | at the pull request review |

---

[PY-MIL-003]: ../../../src/pomodoro/timer_rules.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[5b3d012]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/5b3d01272307e42dee6f55467fd18ad9e83937fa
