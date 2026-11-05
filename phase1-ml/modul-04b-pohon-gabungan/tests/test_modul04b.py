"""Tes modul 4b.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import contextlib
import io
import json
import re
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
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
    anggur = load_wine()
    tabel = pd.DataFrame(anggur.data, columns=anggur.feature_names)
    tabel["golongan"] = anggur.target_names[anggur.target]
    ukuran = tabel[list(anggur.feature_names)]
    golongan = tabel["golongan"]
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
    assert "RandomForest" not in teks
    assert "GradientBoosting" not in teks
    assert "DecisionTree" not in teks
    assert "salah_uji" not in teks
    assert "most_common" not in teks


def test_anggur_dan_tiga_model():
    anggur = load_wine()
    assert anggur.data.shape == (178, 13)
    ukuran_latih, ukuran_uji, golongan_latih, golongan_uji = _siapkan()
    assert len(golongan_uji) == 45
    pohon = DecisionTreeClassifier(random_state=SEED)
    hutan = RandomForestClassifier(random_state=SEED)
    boosting = GradientBoostingClassifier(random_state=SEED)
    pohon.fit(ukuran_latih, golongan_latih)
    hutan.fit(ukuran_latih, golongan_latih)
    boosting.fit(ukuran_latih, golongan_latih)
    salah_latih_pohon = _salah(pohon, ukuran_latih, golongan_latih)
    salah_uji_pohon = _salah(pohon, ukuran_uji, golongan_uji)
    salah_uji_hutan = _salah(hutan, ukuran_uji, golongan_uji)
    salah_uji_boosting = _salah(boosting, ukuran_uji, golongan_uji)
    assert salah_latih_pohon == 0
    assert salah_uji_pohon == 2
    assert salah_uji_hutan == 0
    assert salah_uji_boosting == 1
    assert salah_uji_hutan < salah_uji_pohon
    assert salah_uji_boosting < salah_uji_pohon
    assert float(boosting.learning_rate) == 0.1
    assert int(hutan.n_estimators) == 100


def test_kunci_dijalankan_dari_sumber():
    """Mutasi di sel kunci menggagalkan tes ini.

    Sumber sel dijalankan, jadi assert di dalam notebook ikut terpicu.
    Angka pembanding dihitung ulang di tes, bukan diambil dari keluaran tersimpan.
    """
    ukuran_latih, ukuran_uji, golongan_latih, golongan_uji = _siapkan()
    pohon = DecisionTreeClassifier(random_state=SEED)
    hutan = RandomForestClassifier(random_state=SEED)
    boosting = GradientBoostingClassifier(random_state=SEED)
    pohon.fit(ukuran_latih, golongan_latih)
    hutan.fit(ukuran_latih, golongan_latih)
    boosting.fit(ukuran_latih, golongan_latih)
    teks = _jalankan_sumber("latihan-kunci.ipynb")
    assert f"salah_latih_pohon {_salah(pohon, ukuran_latih, golongan_latih)}" in teks
    salah_pohon = _salah(pohon, ukuran_uji, golongan_uji)
    salah_hutan = _salah(hutan, ukuran_uji, golongan_uji)
    salah_boosting = _salah(boosting, ukuran_uji, golongan_uji)
    assert f"salah_uji_pohon {salah_pohon}" in teks
    assert f"salah_uji_hutan {salah_hutan}" in teks
    assert f"salah_uji_boosting {salah_boosting}" in teks
    pasangan = {
        "pohon": salah_pohon,
        "hutan_acak": salah_hutan,
        "gradient_boosting": salah_boosting,
    }
    assert f"paling_sedikit_salah_uji {min(pasangan, key=pasangan.get)}" in teks
    assert "assert " in _seluruh_sumber("latihan-kunci.ipynb")


def test_notebook_utama_dijalankan_dari_sumber():
    """Mutasi di notebook utama menggagalkan tes ini.

    Sumber sel dijalankan, jadi assert di dalam notebook ikut terpicu.
    """
    _jalankan_sumber("notebook.ipynb")


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
    for istilah in ("hutan acak", "gradient boosting"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 2
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


def test_kamus_dua_istilah_modul_4b():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("hutan acak", "gradient boosting"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "4b"
        assert batas
