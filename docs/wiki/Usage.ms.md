# Penggunaan

[English](Home) | [Dansk](Home.da) | Bahasa Melayu

> Halaman ini disimpan dalam repositori di bawah `docs/wiki/`. Halaman Inggeris ialah sumber; halaman Denmark dan Bahasa Melayu ialah terjemahan.

## Jalankan pemasa

Dengan persekitaran maya aktif:

```bash
python -m pomodoro
```

![Tetingkap semasa rehat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-idle.png)

- **Start** memulakan sesi seterusnya. Selepas itu pemasa berjalan sendiri.
- **Reset** menghentikan pemasa, mengosongkan tanda semak dan kembali ke `00:00`.
- Klik kedua pada **Start** semasa sesi berjalan diabaikan.

![Rehat dengan satu tanda semak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/028-pomodoro/raw/branch/main/docs/images/screenshot-break.png)

## Jalankan ujian

```bash
python -m pytest
```

Ujian tetingkap dilangkau apabila Tkinter atau paparan tidak tersedia. Pada Linux tanpa paparan gunakan `xvfb-run -a python -m pytest`.

## Bina dokumentasi kod sumber

```bash
doxygen Doxyfile
```

HTML ditulis ke `docs/doxygen/html/index.html`.

## Integrasi berterusan

`.gitea/workflows/ci.yml` menjalankan `ruff`, `mypy --strict` dan `pytest` pada setiap pull request ke `main`.

## Kod secara ringkas

| Fail | Tujuan |
| --- | --- |
| `constants.py` | Warna, fon, tempoh dan nilai tetingkap |
| `timer_rules.py` | Kitaran: sesi seterusnya, teks `M:SS` dan tanda semak |
| `app.py` | Tetingkap serta `start_timer`, `count_down`, `reset_timer` |
| `main.py` | Titik masuk untuk `python -m pomodoro` |
