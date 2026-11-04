"""Tes modul 6b.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

SEED = 42
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
VERSI_PENDEK = "3" + ".14"
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


def _rantai():
    return Pipeline(
        steps=[
            (
                "praolah",
                ColumnTransformer(
                    transformers=[
                        ("angka", StandardScaler(), ["gelas_ml"]),
                        (
                            "kategori",
                            OneHotEncoder(sparse_output=False),
                            ["suhu"],
                        ),
                    ],
                    remainder="drop",
                ),
            ),
            ("model", LogisticRegression(random_state=SEED)),
        ]
    )


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


def test_rata_tiga_gelas_latih():
    latih = np.array([200, 50, 180])
    assert int(latih.sum()) == 430
    assert float(latih.mean()) == float(np.mean([200, 50, 180]))


def _kasus_main():
    rng = np.random.default_rng(SEED)
    n = 40
    gelas_ml = rng.integers(30, 220, size=n)
    suhu = np.where(rng.random(n) < 0.5, "dingin", "panas")
    kembali = np.where(gelas_ml < 100, "ya", "tidak")
    return pd.DataFrame(
        {
            "gelas_ml": gelas_ml,
            "suhu": suhu,
            "catatan_pinggir": "gelas",
            "kembali": kembali,
        }
    )


def test_pipeline_stabil_dan_tanpa_bocor_rata_rata():
    kasus = _kasus_main()
    X = kasus[["gelas_ml", "suhu", "catatan_pinggir"]]
    y = kasus["kembali"]
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.25, random_state=SEED
    )
    pipa = _rantai()
    pipa.fit(X_latih, y_latih)
    tebakan_1 = pipa.predict(X_uji)
    pipa.fit(X_latih, y_latih)
    tebakan_2 = pipa.predict(X_uji)
    assert tebakan_1.tolist() == tebakan_2.tolist()
    nama = pipa.named_steps["praolah"].get_feature_names_out().tolist()
    assert not any("catatan_pinggir" in item for item in nama)
    rata_dalam = float(
        pipa.named_steps["praolah"].named_transformers_["angka"].mean_[0]
    )
    assert rata_dalam != float(kasus["gelas_ml"].mean())
    assert int((tebakan_1 == y_uji.to_numpy()).sum()) == len(y_uji) == 10


def test_kunci_latihan_tidak_selalu_cocok():
    gelas = np.array([10, 30, 50, 70, 90, 110, 130, 150])
    assert int(gelas[:3].sum()) == 90
    assert float(gelas[:3].mean()) == 30.0
    assert float(gelas[:3].mean()) != float(gelas[:4].mean())
    suhu = [
        "panas",
        "dingin",
        "panas",
        "dingin",
        "panas",
        "dingin",
        "panas",
        "dingin",
    ]
    tabel = pd.DataFrame(
        {
            "gelas_ml": gelas,
            "suhu": suhu,
            "catatan_pinggir": "gelas",
            "kembali": ["ya" if nilai < 100 else "tidak" for nilai in gelas],
        }
    )
    X = tabel[["gelas_ml", "suhu", "catatan_pinggir"]]
    y = tabel["kembali"]
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.25, random_state=SEED
    )
    pipa = _rantai()
    pipa.fit(X_latih, y_latih)
    tebakan = pipa.predict(X_uji)
    assert tebakan.tolist() == ["ya", "ya"]
    assert int((tebakan == y_uji.to_numpy()).sum()) == 1
    assert len(y_uji) == 2
    pengkode = pipa.named_steps["praolah"].named_transformers_["kategori"]
    gagal = False
    try:
        pengkode.transform(pd.DataFrame({"suhu": ["hangat"]}))
    except ValueError:
        gagal = True
    assert gagal


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
    for istilah in ("Pipeline", "ColumnTransformer"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 2
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


def test_kamus_dua_istilah_modul_6b():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("Pipeline", "ColumnTransformer"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "6b"
        assert batas
