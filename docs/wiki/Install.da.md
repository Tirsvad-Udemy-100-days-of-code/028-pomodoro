# Installation

[English](Home) | Dansk | [Bahasa Melayu](Home.ms)

> Denne side ligger i repositoryet under `docs/wiki/`. Den engelske side er kilden; den danske og den malajiske side er oversættelser.

## Krav

- Python 3.13 eller nyere, med Tkinter
- `venv` og `pip` (følger med Python)
- Valgfrit: Doxygen til kildedokumentationen

## Hent koden

```text
git clone ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/028-pomodoro.git
cd 028-pomodoro
```

Mappen `framework/` er et git-submodul med projektets kvalitetsproces. Den skal ikke bruges for at køre programmet.

## Windows PowerShell

Installer Python 3.13 eller nyere fra python.org (Tkinter er med), og kør derefter:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

```bash
sudo apt install python3 python3-venv python3-tk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## macOS

```bash
brew install python@3.13 python-tk@3.13
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør `deactivate` for at forlade det virtuelle miljø.

Næste: [Brug](Usage.da).
