# Install

English | [Dansk](Home.da) | [Bahasa Melayu](Home.ms)

> This page is kept in the repository under `docs/wiki/`. The English page is the source; the Danish and Bahasa Melayu pages are translations.

## Requirements

- Python 3.13 or later, with Tkinter
- `venv` and `pip` (they come with Python)
- Optional: Doxygen for the source documentation

## Get the code

```text
git clone ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/028-pomodoro.git
cd 028-pomodoro
```

The `framework/` folder is a git submodule with the project's quality process. It is not needed to run the program.

## Windows PowerShell

Install Python 3.13 or later from python.org (it includes Tkinter), then:

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

Run `deactivate` to leave the virtual environment.

Next: [Usage](Usage).
