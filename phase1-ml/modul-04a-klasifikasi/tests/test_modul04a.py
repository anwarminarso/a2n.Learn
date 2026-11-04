"""Tes modul 4a.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import contextlib
import io
import json
import re
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
SEED = 42


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


def _siapkan():
    iris = load_iris()
    tabel = pd.DataFrame(iris.data, columns=iris.feature_names)
    tabel["spesies"] = iris.target_names[iris.target]
    dua = tabel.loc[tabel["spesies"] != "setosa"].copy()
    ukuran = dua[list(iris.feature_names)]
    golongan = dua["spesies"]
    return train_test_split(
        ukuran,
        golongan,
        test_size=0.25,
        random_state=SEED,
        stratify=golongan,
    )


def _salah(model, ukuran, golongan):
    return int((model.predict(ukuran) != golongan.to_numpy()).sum())


def _jalankan_sumber(nama):
    """Jalankan sumber sel. Keluaran tersimpan tidak dibaca."""
    nb = _baca_notebook(nama)
    ruang = {"__name__": "__main__"}
    potong = []
    for nomor, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(compile(_sumber(cell), f"{nama}:{nomor}", "exec"), ruang)
        potong.append(buf.getvalue())
    return "".join(potong)


def test_sel_pertama_adalah_seed():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        assert nb["cells"][0]["cell_type"] == "code"
        assert "SEED = 42" in _sumber(nb["cells"][0])


def test_sel_kode_satu_ide():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        kode = [c for c in nb["cells"] if c["cell_type"] == "code"]
        assert "Satu ide:" not in _sumber(kode[0])
        for cell in kode[1:]:
            assert _sumber(cell).count("Satu ide:") == 1


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


def test_latihan_tanpa_output_tersimpan():
    nb = _baca_notebook("latihan.ipynb")
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        assert cell.get("outputs", []) == []
        assert cell.get("execution_count") in (None,)


def test_latihan_tidak_menghitung_jawaban():
    teks = _seluruh_sumber("latihan.ipynb")
    assert "LogisticRegression" not in teks
    assert "DecisionTree" not in teks
    assert "salah_uji" not in teks


def test_iris_dua_spesies_dan_model():
    ukuran_latih, ukuran_uji, golongan_latih, golongan_uji = _siapkan()
    assert len(golongan_latih) == 75
    assert len(golongan_uji) == 25
    baseline = DummyClassifier(strategy="most_frequent", random_state=SEED)
    baseline.fit(ukuran_latih, golongan_latih)
    logistik = LogisticRegression(random_state=SEED)
    logistik.fit(ukuran_latih, golongan_latih)
    pohon = DecisionTreeClassifier(max_depth=2, random_state=SEED)
    pohon.fit(ukuran_latih, golongan_latih)
    pohon_dalam = DecisionTreeClassifier(random_state=SEED)
    pohon_dalam.fit(ukuran_latih, golongan_latih)
    salah_uji_baseline = _salah(baseline, ukuran_uji, golongan_uji)
    salah_uji_logistik = _salah(logistik, ukuran_uji, golongan_uji)
    salah_latih_pohon = _salah(pohon, ukuran_latih, golongan_latih)
    salah_uji_pohon = _salah(pohon, ukuran_uji, golongan_uji)
    salah_latih_dalam = _salah(pohon_dalam, ukuran_latih, golongan_latih)
    salah_uji_dalam = _salah(pohon_dalam, ukuran_uji, golongan_uji)
    assert salah_uji_baseline == 13
    assert salah_uji_logistik == 2
    assert salah_uji_logistik < salah_uji_baseline
    assert salah_latih_pohon == 1
    assert salah_uji_pohon == 3
    assert salah_latih_dalam == 0
    assert salah_uji_dalam == 4
    assert salah_uji_dalam > salah_uji_pohon


def test_kunci_dijalankan_dari_sumber():
    """Mutasi di sel kunci menggagalkan tes ini.

    Sumber sel dijalankan, jadi assert di dalam notebook ikut terpicu.
    Angka pembanding dihitung ulang di tes, bukan diambil dari keluaran tersimpan.
    """
    ukuran_latih, ukuran_uji, golongan_latih, golongan_uji = _siapkan()
    baseline = DummyClassifier(strategy="most_frequent", random_state=SEED)
    logistik = LogisticRegression(random_state=SEED)
    pohon = DecisionTreeClassifier(max_depth=2, random_state=SEED)
    pohon_dalam = DecisionTreeClassifier(random_state=SEED)
    baseline.fit(ukuran_latih, golongan_latih)
    logistik.fit(ukuran_latih, golongan_latih)
    pohon.fit(ukuran_latih, golongan_latih)
    pohon_dalam.fit(ukuran_latih, golongan_latih)
    teks = _jalankan_sumber("latihan-kunci.ipynb")
    assert f"salah_uji_baseline {_salah(baseline, ukuran_uji, golongan_uji)}" in teks
    assert f"salah_uji_logistik {_salah(logistik, ukuran_uji, golongan_uji)}" in teks
    assert f"salah_latih_pohon {_salah(pohon, ukuran_latih, golongan_latih)}" in teks
    assert f"salah_uji_pohon {_salah(pohon, ukuran_uji, golongan_uji)}" in teks
    assert (
        f"salah_latih_pohon_dalam {_salah(pohon_dalam, ukuran_latih, golongan_latih)}"
        in teks
    )
    assert (
        f"salah_uji_pohon_dalam {_salah(pohon_dalam, ukuran_uji, golongan_uji)}"
        in teks
    )
    assert "assert " in _seluruh_sumber("latihan-kunci.ipynb")


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
    for istilah in ("klasifikasi", "regresi logistik", "pohon keputusan"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert "3.14" not in teks
    assert PATCH_ANGKA.search(teks) is None
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]


def test_pyproject_dan_lock_di_root():
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()
    versi = (REPO / ".python-version").read_text(encoding="utf-8").strip()
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert f'requires-python = "=={versi}.*"' in teks


def test_berkas_modul_tanpa_nomor_patch_python():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path


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


def test_kamus_tiga_istilah_modul_4a():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("klasifikasi", "regresi logistik", "pohon keputusan"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "4a"
        assert batas
