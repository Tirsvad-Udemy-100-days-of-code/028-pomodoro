# Domain Dictionary: Pomodoro Timer

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | AI for S01 | AI as stand-in for S01 | Initial version; Go in RC-003 | [75fa7ed] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the Pomodoro timer to its professional IT term. PO language: en. Domain: it. The dictionary covers the words of the Pomodoro technique as the Business Case and the milestones use them, and the names the source code gives them.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| work session | en | work repetition | A period of focused work, 25 minutes by default. | BC, SA, PP, MIL | PY |
| break | en | break repetition | A period of rest between work sessions, short (5 minutes) or long (20 minutes). | BC, SA, PP, MIL | PY |
| check mark | en | check-mark label text | The symbol shown for each completed work session. | BC, SA, PP, MIL | PY |
| countdown | en | count_down | The display of the remaining time in `M:SS` that ticks once per second. | BC, SA, PP, MIL | PY |
| reset | en | reset_timer | The action that stops the timer and returns the application to its start state. | BC, SA, PP, MIL | PY |

## Rules

- PO terms are used in the Business Case, Stakeholder Analysis, Project Plan and milestones; IT terms are used in source code and its tests.
- One IT term per PO term and one PO term per IT term; a new concept gets its row in the same change.
- No Domain Model, Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists in this project (single-screen exercise, see [PP-001]), so those types are not listed as users of any term.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[75fa7ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/commit/75fa7ed494597311f4cf762cf2e83ac36e22d153
