# Brug

[English](Home) | Dansk | [Bahasa Melayu](Home.ms)

> Denne side ligger i repositoryet under `docs/wiki/`. Den engelske side er kilden; den danske og den malajiske side er oversættelser.

## Kør timeren

Når det virtuelle miljø er aktivt:

```bash
python -m pomodoro
```

![Vinduet i hvile](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-idle.png)

- **Start** begynder den næste session. Derefter kører timeren videre af sig selv.
- **Reset** stopper timeren, fjerner fluebenene og går tilbage til `00:00`.
- Et ekstra klik på **Start**, mens en session kører, bliver ignoreret.

![En pause med ét flueben](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-break.png)

## Kør testene

```bash
python -m pytest
```

Vinduestestene springes over, når Tkinter eller en skærm ikke er tilgængelig. På Linux uden skærm bruges `xvfb-run -a python -m pytest`.

## Byg kildedokumentationen

```bash
doxygen Doxyfile
```

HTML skrives til `docs/doxygen/html/index.html`.

## Kontinuerlig integration

`.gitea/workflows/ci.yml` kører `ruff`, `mypy --strict` og `pytest` ved hver pull request til `main`.

## Koden kort fortalt

| Fil | Formål |
| --- | --- |
| `constants.py` | Farver, skrifttype, varigheder og vinduesværdier |
| `timer_rules.py` | Cyklussen: hvilken session der kommer næst, teksten `M:SS` og fluebenene |
| `app.py` | Vinduet samt `start_timer`, `count_down`, `reset_timer` |
| `main.py` | Indgang for `python -m pomodoro` |
