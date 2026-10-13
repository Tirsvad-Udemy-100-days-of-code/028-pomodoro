# Usage

English | [Dansk](Home.da) | [Bahasa Melayu](Home.ms)

> This page is kept in the repository under `docs/wiki/`. The English page is the source; the Danish and Bahasa Melayu pages are translations.

## Run the timer

With the virtual environment active:

```bash
python -m pomodoro
```

![The idle window](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-idle.png)

- **Start** begins the next session. The timer then rolls on by itself.
- **Reset** stops the timer, clears the check marks and returns to `00:00`.
- A second click on **Start** while a session runs is ignored.

![A break with one check mark](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-break.png)

## Run the tests

```bash
python -m pytest
```

The window tests are skipped when Tkinter or a display is not available. On Linux without a display use `xvfb-run -a python -m pytest`.

## Build the source documentation

```bash
doxygen Doxyfile
```

The HTML is written to `docs/doxygen/html/index.html`.

## Continuous integration

`.gitea/workflows/ci.yml` runs `ruff`, `mypy --strict` and `pytest` on every pull request to `main`.

## The code in short

| File | Purpose |
| --- | --- |
| `constants.py` | Colours, font, durations and window values |
| `timer_rules.py` | The cycle: which session comes next, the `M:SS` text, the check marks |
| `app.py` | The window and `start_timer`, `count_down`, `reset_timer` |
| `main.py` | Entry point for `python -m pomodoro` |
