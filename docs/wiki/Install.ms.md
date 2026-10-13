# Pemasangan

[English](Home) | [Dansk](Home.da) | Bahasa Melayu

> Halaman ini disimpan dalam repositori di bawah `docs/wiki/`. Halaman Inggeris ialah sumber; halaman Denmark dan Bahasa Melayu ialah terjemahan.

## Keperluan

- Python 3.13 atau lebih baharu, dengan Tkinter
- `venv` dan `pip` (disertakan dengan Python)
- Pilihan: Doxygen untuk dokumentasi kod sumber

## Dapatkan kod

```text
git clone ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/028-pomodoro.git
cd 028-pomodoro
```

Folder `framework/` ialah submodul git yang mengandungi proses kualiti projek. Ia tidak diperlukan untuk menjalankan atur cara ini.

## Windows PowerShell

Pasang Python 3.13 atau lebih baharu dari python.org (Tkinter disertakan), kemudian:

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

Jalankan `deactivate` untuk keluar daripada persekitaran maya.

Seterusnya: [Penggunaan](Usage.ms).
