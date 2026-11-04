# Modul 4: Klasifikasi

**Topik:** logistic regression, decision tree, random forest, gradient boosting
**Tujuan:** Membangun dan membandingkan model klasifikasi utama.
**Tingkat:** intermediate
**Status:** dipecah menjadi dua modul pendek
**Issue:** #4

Issue ini menyebut empat model. Bersama istilah klasifikasi, itu lebih dari tiga istilah baru. Isi yang dikerjakan ada di dua folder pendek pada branch yang sama:

- [modul-04a-klasifikasi](../modul-04a-klasifikasi/): klasifikasi, regresi logistik, pohon keputusan
- [modul-04b-pohon-gabungan](../modul-04b-pohon-gabungan/): hutan acak, gradient boosting

Penomoran, issue, dan tabel roadmap tidak diubah di sini. Iris yang menomori ulang.

uv adalah perkakas yang memasang paket sesuai berkas kunci di root repo. Paket adalah bundel kode siap pakai. `pyproject.toml`, `uv.lock`, dan `requirements.txt` ada di root, bukan di folder modul.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```
