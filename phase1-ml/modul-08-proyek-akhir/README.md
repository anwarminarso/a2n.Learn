# Modul 8: Proyek akhir

**Topik:** data sintetis ala tambang, ekspor ONNX, panggil dari .NET
**Tujuan:** Proyek ujung-ke-ujung dengan data sintetis ala tambang, ekspor model ke ONNX, dan memanggilnya dari .NET.
**Tingkat:** pro
**Status:** belum dimulai
**Issue:** #8

Isi folder ini nanti (ditulis Pyra), lihat [module-template](../../docs/module-template.md):
`README.md` (teori 1 halaman), `notebook.ipynb`, `latihan.ipynb`, `latihan-kunci.ipynb`, `tests/`, `pyproject.toml`, `uv.lock`, `requirements.txt` (`uv export`). `SEED = 42` di sel pertama tiap notebook. Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only.

**Toleransi .NET vs Python:** Toleransi ditulis di dokumen, bukan "sama persis": probabilitas `atol=1e-5` (dibuktikan lewat uji), label kelas harus identik; versi skl2onnx dan onnxruntime dikunci di `uv.lock`, opset ditulis.

**Catatan:** Menurut cek cepat Pyra (Python 3.14, Linux, opset 22): label kelas identik dan selisih probabilitas maksimum sekitar 1.2e-07. Ini belum diverifikasi tim; `target_opset` dipin secara eksplisit, dan Ursa tetap memverifikasi dari `uv sync` pada lock yang di-commit.
