# Review Record: Python source of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | AI for S01 | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-002] (src/pomodoro/app.py, main.py, __main__.py, constants.py and tests/test_app.py, tests/test_constants.py)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Module snake_case, class PomodoroApp PascalCase, constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (title_label, check_label, timer_text, tomato_image). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format --check pass (ruff 0.17.0), no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function annotated incl. -> None; mypy --strict passes on 7 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling in source; tests skip on tk.TclError through a fixture, no bare except. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (window: tk.Tk | None = None); no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files are opened in code; the image is loaded by Tkinter from a path. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, class and public method docstrings with Doxygen @brief/@param. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging or printing. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists (single-screen exercise, PP-001); the class is the one the lectures describe. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 10 window tests plus constants tests, named for behaviour, no network, no order dependence; fixture skips without Tk. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict passes; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Runtime dependencies none; dev tools pinned in pyproject.toml. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Colours, sizes and texts are defined once in constants.py and imported. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | app.py imports tkinter and constants only; main.py is the composition root; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | PomodoroApp has one reason to change (the window layout); timer rules will be a separate module in MIL-003. |

## Overall Verdict

Go — every Mandatory criterion of QC-PY-001 passes or is not applicable with the reason stated. The window tests skip on this machine in about one run in three (Tcl cannot find tk.tcl on a Microsoft Store Python); the skip is environmental, passes are 28 or 29 of 29.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Investigate the intermittent Tcl initialisation error of the Microsoft Store Python if the skips matter | S01 | not scheduled |

---

[PY-MIL-002]: ../../../src/pomodoro/app.py
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
