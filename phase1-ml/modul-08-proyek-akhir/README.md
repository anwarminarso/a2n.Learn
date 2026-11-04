# Modul 8: Proyek akhir

**Topik:** data sintetis ala tambang, ekspor ONNX, panggil dari .NET
**Tujuan:** Proyek ujung-ke-ujung dengan data sintetis ala tambang, ekspor model ke ONNX, dan memanggilnya dari .NET.
**Tingkat:** pro
**Status:** belum dimulai
**Issue:** #8

Isi folder ini nanti (ditulis Pyra), lihat [module-template](../../docs/module-template.md):
`README.md` (teori 1 halaman), `notebook.ipynb`, `latihan.ipynb`, `latihan-kunci.ipynb`, `tests/`, `pyproject.toml`, `uv.lock`, `requirements.txt` (`uv export`). `SEED = 42` di sel pertama tiap notebook. Python 3.12, CPU only.

**Toleransi .NET vs Python:** Toleransi ditulis di dokumen, bukan "sama persis": probabilitas `atol=1e-5` (dibuktikan lewat uji), label kelas harus identik; versi skl2onnx, onnxruntime, dan opset dikunci dan ditulis.
