"""Tes sederhana modul 3.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes, make_regression
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = (
    "notebook.ipynb",
    "latihan.ipynb",
    "latihan-kunci.ipynb",
    "ujian.ipynb",
    "ujian-kunci.ipynb",
)
TANPA_KELUARAN = ("latihan.ipynb", "ujian.ipynb")
# Angka setelah titik ketiga menandai patch. Bentuk dengan bintang tidak kena.
PATCH_ANGKA = re.compile(r"3\.14\.\d")
# Disambung supaya berkas ini tidak memuat penanda sebagai teks utuh.
TERLARANG = (
    "ri" + "dge",
    "la" + "sso",
    "lea" + "kage",
    "cross-" + "validation",
    "cross_" + "val",
    "validasi " + "silang",
    "s" + "mp",
    "an" + "tam",
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


def _baris_stream(nama):
    nb = _baca_notebook(nama)
    baris = []
    for cell in nb["cells"]:
        for keluaran in cell.get("outputs", []):
            if keluaran.get("output_type") != "stream":
                continue
            raw = keluaran.get("text", "")
            if isinstance(raw, list):
                raw = "".join(raw)
            baris.extend(raw.splitlines())
    return baris


def _cetak(wadah, *args):
    wadah.append(" ".join(str(a) for a in args))


def _garis_notebook():
    garis = []
    jarak_latih = np.array([1, 2, 3], dtype=float)
    menit_latih = np.array([4, 6, 9], dtype=float)
    tebakan_coba = 2 + 2 * jarak_latih
    kuadrat = (menit_latih - tebakan_coba) ** 2
    _cetak(garis, "tangan_tebakan", tebakan_coba.tolist())
    _cetak(garis, "tangan_kuadrat", kuadrat.tolist())
    _cetak(garis, "tangan_fungsi_kerugian", float(kuadrat.mean()))
    _cetak(garis, "tangan_baseline", float(menit_latih.mean()))
    jarak_amplop = np.array([4.0])
    menit_amplop = np.array([12.0])
    tebakan_amplop_coba = 2 + 2 * jarak_amplop
    mae_coba = float(mean_absolute_error(menit_amplop, tebakan_amplop_coba))
    mae_base = float(mean_absolute_error(menit_amplop, np.full(1, menit_latih.mean())))
    _cetak(garis, "tangan_mae_garis_coba", mae_coba)
    _cetak(garis, "tangan_mae_baseline", mae_base)
    _cetak(garis, "tangan_coba_lebih_dekat", mae_coba < mae_base)

    garis_tangan = LinearRegression()
    garis_tangan.fit(jarak_latih.reshape(-1, 1), menit_latih)
    _cetak(garis, "tangan_awal", float(garis_tangan.intercept_))
    _cetak(garis, "tangan_pengali", float(garis_tangan.coef_[0]))
    tebakan_pas = garis_tangan.predict(jarak_latih.reshape(-1, 1))
    kerugian_pas = float(np.mean((menit_latih - tebakan_pas) ** 2))
    _cetak(garis, "tangan_fungsi_kerugian_pas", kerugian_pas)
    _cetak(garis, "tangan_pas_lebih_kecil", kerugian_pas < float(kuadrat.mean()))
    tebakan_amplop_pas = garis_tangan.predict(jarak_amplop.reshape(-1, 1))
    mae_pas = float(mean_absolute_error(menit_amplop, tebakan_amplop_pas))
    _cetak(garis, "tangan_mae_pas", mae_pas)
    _cetak(garis, "tangan_pas_mengalahkan_baseline", mae_pas < mae_base)

    bahan = load_diabetes(as_frame=True, scaled=True)
    tabel = pd.DataFrame({"bmi": bahan.frame["bmi"], "target": bahan.frame["target"]})
    _cetak(garis, "kasus_baris", int(tabel.shape[0]))
    _cetak(garis, "kasus_kolom", int(tabel.shape[1]))
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    _cetak(garis, "kasus_baris_latih", int(len(latih)))
    _cetak(garis, "kasus_baris_uji", int(len(uji)))
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(latih[["bmi"]], latih["target"])
    _cetak(garis, "kasus_baseline", float(latih["target"].mean()))
    model = LinearRegression()
    model.fit(latih[["bmi"]], latih["target"])
    _cetak(garis, "kasus_awal", float(model.intercept_))
    _cetak(garis, "kasus_pengali", float(model.coef_[0]))
    mae_uji_baseline = float(mean_absolute_error(uji["target"], baseline.predict(uji[["bmi"]])))
    mae_uji_garis = float(mean_absolute_error(uji["target"], model.predict(uji[["bmi"]])))
    _cetak(garis, "kasus_mae_uji_baseline", mae_uji_baseline)
    _cetak(garis, "kasus_mae_uji_garis", mae_uji_garis)
    _cetak(garis, "kasus_garis_mengalahkan_baseline", mae_uji_garis < mae_uji_baseline)
    mae_latih_garis = float(mean_absolute_error(latih["target"], model.predict(latih[["bmi"]])))
    mae_latih_hafal = float(mean_absolute_error(latih["target"], latih["target"]))
    _cetak(garis, "kasus_mae_latih_garis", mae_latih_garis)
    _cetak(garis, "kasus_mae_latih_hafal", mae_latih_hafal)

    petunjuk, jawaban = make_regression(
        n_samples=24,
        n_features=20,
        n_informative=1,
        noise=50,
        random_state=42,
    )
    _cetak(garis, "lentur_petunjuk", int(petunjuk.shape[1]))
    petunjuk_latih, petunjuk_uji, jawaban_latih, jawaban_uji = train_test_split(
        petunjuk, jawaban, test_size=0.25, random_state=42
    )
    _cetak(garis, "lentur_baris_latih", int(len(jawaban_latih)))
    garis_lentur = LinearRegression()
    garis_lentur.fit(petunjuk_latih, jawaban_latih)
    baseline_lentur = DummyRegressor(strategy="mean")
    baseline_lentur.fit(petunjuk_latih, jawaban_latih)
    lentur_mae_latih = float(
        mean_absolute_error(jawaban_latih, garis_lentur.predict(petunjuk_latih))
    )
    lentur_mae_uji = float(mean_absolute_error(jawaban_uji, garis_lentur.predict(petunjuk_uji)))
    lentur_mae_base = float(
        mean_absolute_error(jawaban_uji, baseline_lentur.predict(petunjuk_uji))
    )
    _cetak(garis, "lentur_mae_latih", lentur_mae_latih)
    _cetak(garis, "lentur_mae_uji", lentur_mae_uji)
    _cetak(garis, "lentur_mae_uji_baseline", lentur_mae_base)
    _cetak(garis, "lentur_latih_lebih_kecil", lentur_mae_latih < lentur_mae_uji)
    _cetak(garis, "lentur_uji_lebih_buruk", lentur_mae_uji > lentur_mae_base)

    _latih_lagi, uji_lagi = train_test_split(tabel, test_size=0.25, random_state=42)
    _cetak(garis, "kasus_indeks_pertama", int(uji.index[0]))
    _cetak(garis, "kasus_indeks_pertama_lagi", int(uji_lagi.index[0]))
    _cetak(garis, "kasus_sama", uji.index.tolist() == uji_lagi.index.tolist())
    return garis


def _garis_kunci():
    garis = []
    jarak_latih = np.array([1, 2, 4], dtype=float)
    menit_latih = np.array([3, 5, 8], dtype=float)
    jarak_uji = np.array([3.0])
    menit_uji = np.array([10.0])
    tebakan_latih = 1 + 2 * jarak_latih
    kerugian = float(np.mean((menit_latih - tebakan_latih) ** 2))
    baseline = float(menit_latih.mean())
    mae_garis = float(mean_absolute_error(menit_uji, 1 + 2 * jarak_uji))
    mae_baseline = float(mean_absolute_error(menit_uji, np.full(1, baseline)))
    _cetak(garis, "kunci_fungsi_kerugian", kerugian)
    _cetak(garis, "kunci_baseline", baseline)
    _cetak(garis, "kunci_mae_garis", mae_garis)
    _cetak(garis, "kunci_mae_baseline", mae_baseline)
    _cetak(garis, "kunci_garis_lebih_dekat", mae_garis < mae_baseline)

    bahan = load_diabetes(as_frame=True, scaled=True)
    tabel = pd.DataFrame({"bp": bahan.frame["bp"], "target": bahan.frame["target"]})
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    model_baseline = DummyRegressor(strategy="mean")
    model_baseline.fit(latih[["bp"]], latih["target"])
    model = LinearRegression()
    model.fit(latih[["bp"]], latih["target"])
    nilai_baseline = float(latih["target"].mean())
    mae_uji_baseline = float(
        mean_absolute_error(uji["target"], model_baseline.predict(uji[["bp"]]))
    )
    mae_uji_garis = float(mean_absolute_error(uji["target"], model.predict(uji[["bp"]])))
    _cetak(garis, "kunci_baris_latih", int(len(latih)))
    _cetak(garis, "kunci_baris_uji", int(len(uji)))
    _cetak(garis, "kunci_baseline_bp", nilai_baseline)
    _cetak(garis, "kunci_mae_uji_baseline", mae_uji_baseline)
    _cetak(garis, "kunci_mae_uji_garis", mae_uji_garis)
    _cetak(garis, "kunci_garis_mengalahkan", mae_uji_garis < mae_uji_baseline)
    return garis


def _garis_ujian():
    garis = []
    petunjuk, jawaban = make_regression(
        n_samples=80,
        n_features=1,
        n_informative=1,
        noise=15,
        random_state=42,
    )
    petunjuk_latih, petunjuk_uji, jawaban_latih, jawaban_uji = train_test_split(
        petunjuk, jawaban, test_size=0.25, random_state=42
    )
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(petunjuk_latih, jawaban_latih)
    model = LinearRegression()
    model.fit(petunjuk_latih, jawaban_latih)
    mae_baseline = float(mean_absolute_error(jawaban_uji, baseline.predict(petunjuk_uji)))
    mae_garis = float(mean_absolute_error(jawaban_uji, model.predict(petunjuk_uji)))
    _cetak(garis, "ujian_baris_latih", int(len(jawaban_latih)))
    _cetak(garis, "ujian_baris_uji", int(len(jawaban_uji)))
    _cetak(garis, "ujian_mae_baseline", mae_baseline)
    _cetak(garis, "ujian_mae_garis", mae_garis)
    _cetak(garis, "ujian_lulus", mae_garis < mae_baseline)
    return garis


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


def test_latihan_dan_ujian_tanpa_keluaran_tersimpan():
    for nama in TANPA_KELUARAN:
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            assert not cell.get("outputs"), nama


def test_garis_mengalahkan_baseline_pada_diabetes_dan_ujian():
    bahan = load_diabetes(as_frame=True, scaled=True)
    tabel = pd.DataFrame({"bmi": bahan.frame["bmi"], "target": bahan.frame["target"]})
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    assert len(latih) == 331
    assert len(uji) == 111
    baseline = DummyRegressor(strategy="mean").fit(latih[["bmi"]], latih["target"])
    model = LinearRegression().fit(latih[["bmi"]], latih["target"])
    mae_base = mean_absolute_error(uji["target"], baseline.predict(uji[["bmi"]]))
    mae_garis = mean_absolute_error(uji["target"], model.predict(uji[["bmi"]]))
    assert mae_garis < mae_base
    assert float(mean_absolute_error(latih["target"], latih["target"])) == 0.0

    baris_ujian = _garis_ujian()
    assert "ujian_lulus True" in baris_ujian
    assert "ujian_baris_latih 60" in baris_ujian
    assert "ujian_baris_uji 20" in baris_ujian


def test_keluaran_notebook_sama_dengan_hitung_ulang():
    assert _baris_stream("notebook.ipynb") == _garis_notebook()
    assert _baris_stream("latihan-kunci.ipynb") == _garis_kunci()
    assert _baris_stream("ujian-kunci.ipynb") == _garis_ujian()


def test_readme_punya_bagian_wajib_dan_batas_analogi():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    for judul in (
        "Cerita pembuka",
        "Coba sendiri dulu, baru kode",
        "Kesalahan yang paling sering terjadi",
        "Cek pemahaman",
        "Kunci jawaban",
        "Sumber",
        "Ujian tingkat beginner",
        "Kriteria lulus",
    ):
        assert judul in teks
    for istilah in ("regresi linear", "fungsi kerugian", "overfitting"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert "uv sync --frozen" in teks
    assert "uv run pytest" in teks
    assert "uv run pytest --nbmake" in teks
    assert "bukan dari folder modul" in teks
    assert "3.14" not in teks
    assert PATCH_ANGKA.search(teks) is None


def test_pyproject_dan_lock_hanya_di_root():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = "==3.14.*"' in teks
    assert "phase1-ml/modul-03-regresi" in teks
    assert PATCH_ANGKA.search(teks) is None
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == "3.14"
    assert (REPO / "uv.lock").is_file()
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()


def test_berkas_modul_tanpa_nomor_patch_python():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path


def test_modul_tidak_memuat_kata_terlarang():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8").lower()
        for kata in TERLARANG:
            assert kata not in teks, (path, kata)


def test_readme_menyalin_keluaran_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for nama in ("notebook.ipynb", "latihan-kunci.ipynb", "ujian-kunci.ipynb"):
        for baris in _baris_stream(nama):
            assert baris.strip() in readme, baris


def _kolom_kamus(kamus, istilah):
    baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
    assert len(baris) == 1, istilah
    kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
    assert len(kolom) == 5, kolom
    return kolom


def test_kamus_tiga_istilah_modul_3():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for istilah in ("regresi linear", "fungsi kerugian", "overfitting"):
        _nama, arti, perumpamaan, modul, batas = _kolom_kamus(kamus, istilah)
        assert arti
        assert perumpamaan
        assert modul == "3"
        assert batas
        assert arti in readme
    assert _kolom_kamus(kamus, "rata-rata selisih mutlak")[3] == "2"
    assert _kolom_kamus(kamus, "baseline")[3] == "2"
    assert "mean_absolute_error" in _kolom_kamus(kamus, "rata-rata selisih mutlak")[1]
    arti_overfitting = _kolom_kamus(kamus, "overfitting")[1]
    assert arti_overfitting.startswith("Model terlalu menyesuaikan diri dengan data latih")
