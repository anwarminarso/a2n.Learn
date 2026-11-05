# Modul 6: Rekayasa fitur dan Pipeline

**Tingkat:** advanced
**Status:** dipecah menjadi dua modul pendek
**Issue:** #6

Modul ini butuh lima istilah baru. Batasnya tiga istilah per modul, jadi isinya dipecah dua. Iris yang memperbarui penomoran, issue, dan tabel roadmap.

- [Bagian A. Rekayasa fitur](../modul-06a-rekayasa-fitur/): fitur, encoding, dan penskalaan.
- [Bagian B. Pipeline](../modul-06b-pipeline/): Pipeline dan ColumnTransformer.

`pyproject.toml`, `uv.lock`, dan `requirements.txt` tetap di root repo. `SEED = 42` di sel pertama tiap notebook. uv adalah perkakas yang memasang paket sesuai berkas kunci. Paket adalah kumpulan kode siap pakai. Perintah dijalankan dari root repo, bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```
