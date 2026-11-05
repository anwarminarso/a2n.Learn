"""Tes modul 6a.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
VERSI_PENDEK = "3" + ".14"
# Disusun dari huruf terpisah supaya berkas tes tidak memuat kata yang dilarang.
TERLARANG_KATA = re.compile(
    "".join(["s", "m", "p"]) + "|" + "".join(["a", "n", "t", "a", "m"]),
    re.IGNORECASE,
)


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
        if "random_state=" in teks:
            assert "random_state=SEED" in teks
        if "default_rng(" in teks:
            assert "default_rng(SEED)" in teks


def test_sel_kode_punya_satu_ide():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        for cell in nb["cells"][1:]:
            if cell["cell_type"] != "code":
                continue
            assert "Satu ide" in _sumber(cell)


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama)
        for pola in terlarang:
            assert pola not in teks


def test_latihan_tanpa_output_tersimpan():
    nb = _baca_notebook("latihan.ipynb")
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        assert cell.get("outputs", []) == []
        assert cell.get("execution_count") is None


def test_empat_gelas_dan_liter():
    gelas = np.array([200, 50, 180, 40])
    assert int(gelas.sum()) == 470
    assert float(gelas.mean()) == 117.5
    assert (gelas / 1000).tolist() == [0.2, 0.05, 0.18, 0.04]


def test_encoding_hanya_dari_latih():
    suhu = pd.DataFrame({"suhu": ["dingin", "panas", "dingin", "panas"]})
    pengkode = OneHotEncoder(sparse_output=False)
    hasil_latih = pengkode.fit_transform(suhu.iloc[:3])
    hasil_uji = pengkode.transform(suhu.iloc[3:])
    assert pengkode.get_feature_names_out(["suhu"]).tolist() == [
        "suhu_dingin",
        "suhu_panas",
    ]
    assert hasil_latih[0].tolist() == [1.0, 0.0]
    assert hasil_uji[0].tolist() == [0.0, 1.0]


def test_penskalaan_latih_berbeda_dari_semua():
    gelas = np.array([200, 50, 180, 40], dtype=float).reshape(-1, 1)
    latih = StandardScaler().fit(gelas[:3])
    semua = StandardScaler().fit(gelas)
    assert float(latih.mean_[0]) != float(semua.mean_[0])
    assert float(semua.mean_[0]) == 117.5


def test_kasus_sintetis_tanpa_jawaban_di_fitur():
    seed = 42
    rng = np.random.default_rng(seed)
    n = 12
    gelas_ml = rng.integers(30, 220, size=n)
    suhu = np.where(rng.random(n) < 0.5, "dingin", "panas")
    kembali = np.where(gelas_ml < 100, "ya", "tidak")
    kasus = pd.DataFrame(
        {"gelas_ml": gelas_ml, "suhu": suhu, "kembali": kembali}
    )
    X = kasus[["gelas_ml", "suhu"]]
    y = kasus["kembali"]
    assert "kembali" not in X.columns
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.25, random_state=seed
    )
    assert len(X_latih) == 9
    assert len(X_uji) == 3
    penimbang = StandardScaler().fit(X_latih[["gelas_ml"]])
    assert float(penimbang.mean_[0]) != float(kasus["gelas_ml"].mean())
    assert len(y_latih) == len(X_latih)
    assert len(y_uji) == len(X_uji)


def test_latihan_angka_lain():
    gelas = np.array([100, 20, 80, 60])
    assert int(gelas.sum()) == 260
    assert float(gelas.mean()) == 65.0
    assert float(gelas[:3].mean()) != float(gelas.mean())
    assert 100 / 1000 == 0.1
    suhu = pd.DataFrame({"suhu": ["panas", "dingin", "panas", "dingin"]})
    pengkode = OneHotEncoder(sparse_output=False)
    hasil = pengkode.fit_transform(suhu)
    assert hasil[0].tolist() == [0.0, 1.0]


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
    for istilah in ("fitur", "encoding", "penskalaan"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert PATCH_ANGKA.search(teks) is None
    assert VERSI_PENDEK not in teks
    assert "uv adalah" in teks.split("uv sync --frozen")[0]
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]


def test_pyproject_dan_lock_di_root():
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()
    assert (REPO / "pyproject.toml").exists()
    assert (REPO / "uv.lock").exists()
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == VERSI_PENDEK


def test_berkas_modul_tanpa_nomor_patch_dan_kata_terlarang():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path
        assert VERSI_PENDEK not in teks, path
        assert TERLARANG_KATA.search(teks) is None, path
        assert TERLARANG_KATA.search(path.name) is None, path


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


def test_kamus_tiga_istilah_modul_6a():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("fitur", "encoding", "penskalaan"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "6a"
        assert batas
