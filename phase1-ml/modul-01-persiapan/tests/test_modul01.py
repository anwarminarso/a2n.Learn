"""Tes sederhana modul 1.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
# Dua potong, supaya berkas ini tidak memuat penanda patch sebagai teks utuh.
PENANDA_PATCH = "3" + ".14."


def _sumber(cell):
    src = cell["source"]
    if isinstance(src, list):
        return "".join(src)
    return src


def _baca_notebook(nama):
    return json.loads((ROOT / nama).read_text(encoding="utf-8"))


def _seluruh_sumber(nama):
    nb = _baca_notebook(nama)
    return "\n".join(_sumber(cell) for cell in nb["cells"])


def test_sel_pertama_adalah_seed():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        assert nb["cells"][0]["cell_type"] == "code"
        assert "SEED = 42" in _sumber(nb["cells"][0])


def test_pemanggilan_acak_memakai_seed():
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama).replace(" ", "")
        assert "random_state=42" not in teks
        assert "default_rng(42)" not in teks
        assert "random_state=SEED" in teks


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama)
        for pola in terlarang:
            assert pola not in teks


def test_jumlah_dan_rata_rata_empat_tinggi():
    tinggi = np.array([5, 7, 6, 6])
    assert int(tinggi.sum()) == 24
    assert float(tinggi.mean()) == 6.0


def test_latihan_halaman():
    halaman = np.array([3, 5, 4, 8])
    assert int(halaman.sum()) == 20
    assert float(halaman.mean()) == 5.0
    buku = pd.DataFrame(
        {
            "hari": ["senin", "selasa", "rabu", "kamis"],
            "halaman": [3, 5, 4, 8],
        }
    )
    assert float(buku["halaman"].mean()) == 5.0


def test_sample_dengan_seed_sama():
    seed = 42
    iris = load_iris()
    tabel = pd.DataFrame(iris.data, columns=iris.feature_names)
    a = tabel.sample(n=5, random_state=seed)
    b = tabel.sample(n=5, random_state=seed)
    pd.testing.assert_frame_equal(a, b)


def test_iris_bawaan_sklearn():
    iris = load_iris()
    assert iris.data.shape[1] == len(iris.feature_names) == 4
    assert iris.data.shape[0] == len(iris.target) == 150


def test_readme_punya_bagian_wajib_dan_batas_analogi():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    for judul in (
        "Cerita pembuka",
        "Coba sendiri dulu, baru kode",
        "Kesalahan yang paling sering terjadi",
        "Cek pemahaman",
        "Kunci jawaban",
        "Sumber",
    ):
        assert judul in teks
    for istilah in ("venv", "array", "DataFrame"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert PENANDA_PATCH not in teks


def test_pyproject_python_tanpa_nomor_patch():
    teks = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = ">=3.14,<3.15"' in teks
    assert PENANDA_PATCH not in teks


def test_berkas_modul_tanpa_nomor_patch_python():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name == "uv.lock" or ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        assert PENANDA_PATCH not in teks, path


def test_readme_menyalin_keluaran_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for nama in ("notebook.ipynb", "latihan-kunci.ipynb"):
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            for keluaran in cell.get("outputs", []):
                if keluaran.get("output_type") != "stream":
                    continue
                raw = keluaran.get("text", "")
                if isinstance(raw, list):
                    raw = "".join(raw)
                for baris in raw.splitlines():
                    assert baris.strip() in readme, baris


def test_kamus_tiga_istilah_modul_1():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("venv", "array", "DataFrame"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "1"
        assert batas
