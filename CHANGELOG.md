# Changelog

All notable changes to this project are documented in this file. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project follows
[Semantic Versioning](https://semver.org/). Each entry names the milestone (MIL) that
delivered it; the milestones are in [docs/milestones/](docs/milestones/).

## Unreleased

## 1.0.0 - 2026-10-13

First complete version: the Day 28 Pomodoro assignment of *100 Days of Code*, with tests,
documentation and continuous integration.

### Added

- Pomodoro window built with Tkinter: tomato canvas with the countdown text, `Timer` title
  label, Start and Reset buttons and a check-mark label in a grid; started with
  `python -m pomodoro` (MIL-002).
- Countdown and Pomodoro cycle with the assignment's names `start_timer`, `count_down` and
  `reset_timer`: work (25 min), short break (5 min) and a long break (20 min) after four work
  sessions, `M:SS` display and one check mark per completed work session (MIL-003).
- Pure timer rules in `timer_rules.py`, free of Tkinter, tested without a display (MIL-003).
- Project scaffold: `pyproject.toml` (Python 3.13 or later, no runtime dependencies), Python
  `.gitignore`, `constants.py`, `Doxyfile` for the source documentation (MIL-001).
- Continuous integration workflow for Gitea Actions running ruff, `mypy --strict` and pytest
  with coverage under a virtual display (MIL-001, MIL-003).
- Static test of the workflow files: valid YAML without duplicate keys, required keys,
  explicit permissions, runner and timeout per job, pinned actions and the inline-script limit
  (MIL-005).
- README with set-up for Windows PowerShell, Linux Debian and macOS, screenshots, and a wiki in
  English, Danish and Bahasa Melayu (MIL-004).
- Project documents under `docs/`: business case, stakeholder analysis, project plan,
  milestones, domain dictionary, traceability matrix and review records.

### Changed

- CI installs `libtk8.6` and `xvfb` at pinned versions on the `ubuntu-24.04` runner image
  (condition of the workflow review).

### Fixed

- A second click on Start while a session runs is ignored; the lecture version started two
  overlapping countdowns (MIL-003).
