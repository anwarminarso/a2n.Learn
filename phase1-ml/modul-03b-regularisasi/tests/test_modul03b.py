"""Tes modul 3b.

Sifat model dihitung ulang di sini. Membandingkan teks keluaran bukan satu-satunya pemeriksaan.
"""

import json
import re
from pathlib import Path

import numpy as np
from sklearn.datasets import make_regression
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
ANGKA_VERSI = "3" + ".14"
LEWATI = {".venv", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
LARANG = ("S" + "MP", "AN" + "TAM")
KALIMAT_TEKNIS = {
    "petunjuk": "Petunjuk adalah angka yang dibaca untuk menyusun tebakan.",
    "koefisien": "Koefisien adalah angka pengali pada satu petunjuk di garis tebakan.",
    "penalti": "Penalti adalah tambahan yang membesar bila koefisien membesar.",
    "simpangan baku": "Simpangan baku mengukur sebaran angka di sekitar rata-ratanya.",
    "regresi linear": (
        "Regresi linear menebak jawaban angka sebagai jumlah petunjuk yang "
        "masing-masing dikalikan koefisien, ditambah satu bilangan geser."
    ),
    "intercept_": "intercept_ adalah nama tempat scikit-learn menyimpan bilangan geser.",
    "coef_": "coef_ adalah nama tempat scikit-learn menyimpan koefisien.",
    "fungsi kerugian": (
        "Fungsi kerugian adalah angka kesalahan yang diperkecil saat model belajar; "
        "pada regresi linear tanpa penalti, angka itu adalah jumlah kuadrat selisih "
        "antara tebakan dan jawaban."
    ),
    "fit": "fit adalah langkah saat model belajar dari data yang diberikan kepadanya.",
    "overfitting": (
        "Overfitting berarti model terlalu menyesuaikan diri dengan data latih, "
        "termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih "
        "tetapi buruk di data baru."
    ),
    "baseline": (
        "Baseline adalah cara menebak paling sederhana (misalnya selalu menebak "
        "rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; "
        "model yang baik harus mengalahkannya."
    ),
    "rata-rata selisih mutlak": (
        "Rata-rata selisih mutlak adalah rata-rata jarak antara tebakan dan jawaban, "
        "jarak berarti selisih yang tanda minusnya dibuang, jumlah jarak dibagi banyak "
        "baris yang diukur, semakin kecil semakin dekat, nilai terbaik adalah nol, "
        "dan fungsi scikit-learn untuk hitungan yang sama bernama mean_absolute_error."
    ),
    "alpha": (
        "alpha adalah angka yang mengalikan penalti; makin besar nilainya, "
        "makin kuat penalti itu."
    ),
    "standardscaler": (
        "StandardScaler menggeser tiap petunjuk supaya rata-ratanya nol dan "
        "simpangan bakunya satu, memakai rata-rata dan simpangan baku data yang "
        "dipelajari saat fit; transform memakai angka itu pada data lain."
    ),
    "pustaka": "Pustaka adalah kumpulan fungsi siap pakai yang dipanggil dari kode.",
    "array": "Array adalah kumpulan nilai sejenis dengan bentuk yang tetap, yang dihitung sekaligus.",
    "numpy": "NumPy adalah pustaka untuk hitungan pada array.",
    "derau": "Derau adalah gangguan acak pada jawaban.",
    "gauss": (
        "Gauss pada derau ini adalah sebaran berbentuk lonceng: nilai kecil lebih "
        "sering daripada nilai besar."
    ),
    "noise": (
        "Parameter noise pada make_regression adalah simpangan baku derau Gauss "
        "yang ditambahkan ke jawaban."
    ),
    "bias": (
        "Parameter bias pada make_regression adalah geseran tetap, yaitu bilangan "
        "geser pada model linear yang membuat jawaban."
    ),
    "linearregression": "LinearRegression adalah regresi linear tanpa penalti pada fungsi kerugian.",
}


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


def _bahan(seed=42):
    X, y = make_regression(
        n_samples=50,
        n_features=30,
        n_informative=5,
        noise=15.0,
        bias=2.5,
        random_state=seed,
    )
    X = X.copy()
    X[:, 0] = X[:, 0] * 50
    indeks = np.arange(X.shape[0])
    X_latih, X_uji, y_latih, y_uji, _indeks_latih, indeks_uji = train_test_split(
        X, y, indeks, test_size=0.25, random_state=seed
    )
    return X, y, X_latih, X_uji, y_latih, y_uji, indeks, indeks_uji


def _pipa(model, X_latih, y_latih, X_uji, y_uji):
    pipa = Pipeline([("skala", StandardScaler()), ("model", model)])
    pipa.fit(X_latih, y_latih)
    mae_uji = float(mean_absolute_error(y_uji, pipa.predict(X_uji)))
    mae_latih = float(mean_absolute_error(y_latih, pipa.predict(X_latih)))
    koef = pipa.named_steps["model"].coef_
    return pipa, mae_uji, mae_latih, koef


def _garis_notebook():
    garis = []
    calon_a = np.array([2.0, 2.0])
    calon_b = np.array([3.0, 0.0])
    kuadrat_a = float(np.sum(calon_a**2))
    kuadrat_b = float(np.sum(calon_b**2))
    mutlak_a = float(np.sum(np.abs(calon_a)))
    mutlak_b = float(np.sum(np.abs(calon_b)))
    _cetak(garis, "tangan_kuadrat_a", kuadrat_a)
    _cetak(garis, "tangan_kuadrat_b", kuadrat_b)
    _cetak(garis, "tangan_mutlak_a", mutlak_a)
    _cetak(garis, "tangan_mutlak_b", mutlak_b)
    _cetak(garis, "tangan_kuadrat_a_lebih_kecil", kuadrat_a < kuadrat_b)
    _cetak(garis, "tangan_mutlak_b_lebih_kecil", mutlak_b < mutlak_a)

    X, _y, X_latih, X_uji, y_latih, y_uji, indeks, indeks_uji = _bahan()
    _cetak(garis, "kasus_baris", int(X.shape[0]))
    _cetak(garis, "kasus_kolom", int(X.shape[1]))
    _cetak(garis, "kasus_baris_latih", int(len(y_latih)))
    _cetak(garis, "kasus_baris_uji", int(len(y_uji)))
    basis = DummyRegressor(strategy="mean")
    basis.fit(X_latih, y_latih)
    _cetak(
        garis,
        "kasus_mae_basis",
        float(mean_absolute_error(y_uji, basis.predict(X_uji))),
    )
    _pipa_tanpa, mae_uji_tanpa, mae_latih_tanpa, _koef_tanpa = _pipa(
        LinearRegression(), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kasus_mae_uji_tanpa", mae_uji_tanpa)
    _cetak(garis, "kasus_mae_latih_tanpa", mae_latih_tanpa)
    pipa_ridge, mae_uji_ridge, mae_latih_ridge, koef_ridge = _pipa(
        Ridge(alpha=5.0), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kasus_mae_uji_ridge", mae_uji_ridge)
    _cetak(garis, "kasus_mae_latih_ridge", mae_latih_ridge)
    _cetak(garis, "kasus_nol_ridge", int(np.sum(koef_ridge == 0.0)))
    _cetak(garis, "kasus_ridge_lebih_baik", mae_uji_ridge < mae_uji_tanpa)
    _pipa_lasso, mae_uji_lasso, mae_latih_lasso, koef_lasso = _pipa(
        Lasso(alpha=0.5), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kasus_mae_uji_lasso", mae_uji_lasso)
    _cetak(garis, "kasus_mae_latih_lasso", mae_latih_lasso)
    _cetak(garis, "kasus_nol_lasso", int(np.sum(koef_lasso == 0.0)))
    _cetak(
        garis,
        "kasus_skala_latih",
        bool(np.allclose(pipa_ridge.named_steps["skala"].mean_, X_latih.mean(axis=0))),
    )
    _indeks_latih_lagi, indeks_uji_lagi = train_test_split(
        indeks, test_size=0.25, random_state=42
    )
    _cetak(garis, "kasus_indeks_uji", indeks_uji.tolist())
    _cetak(garis, "kasus_indeks_uji_lagi", indeks_uji_lagi.tolist())
    _cetak(garis, "kasus_sama", indeks_uji.tolist() == indeks_uji_lagi.tolist())
    return garis


def _garis_kunci():
    garis = []
    calon_a = np.array([4.0, 4.0])
    calon_b = np.array([6.0, 0.0])
    kuadrat_a = float(np.sum(calon_a**2))
    kuadrat_b = float(np.sum(calon_b**2))
    mutlak_a = float(np.sum(np.abs(calon_a)))
    mutlak_b = float(np.sum(np.abs(calon_b)))
    _cetak(garis, "kunci_kuadrat_a", kuadrat_a)
    _cetak(garis, "kunci_kuadrat_b", kuadrat_b)
    _cetak(garis, "kunci_kuadrat_a_lebih_kecil", kuadrat_a < kuadrat_b)
    _cetak(garis, "kunci_mutlak_a", mutlak_a)
    _cetak(garis, "kunci_mutlak_b", mutlak_b)
    _cetak(garis, "kunci_mutlak_b_lebih_kecil", mutlak_b < mutlak_a)
    X, _y, X_latih, X_uji, y_latih, y_uji, _indeks, _indeks_uji = _bahan()
    _cetak(garis, "kunci_baris", int(X.shape[0]))
    _cetak(garis, "kunci_kolom", int(X.shape[1]))
    _cetak(garis, "kunci_baris_latih", int(len(y_latih)))
    _cetak(garis, "kunci_baris_uji", int(len(y_uji)))
    _pipa_tanpa, mae_uji_tanpa, _mae_latih_tanpa, _koef_tanpa = _pipa(
        LinearRegression(), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kunci_mae_uji_tanpa", mae_uji_tanpa)
    pipa_ridge, mae_uji_ridge, _mae_latih_ridge, koef_ridge = _pipa(
        Ridge(alpha=2.0), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kunci_mae_uji_ridge", mae_uji_ridge)
    _cetak(garis, "kunci_nol_ridge", int(np.sum(koef_ridge == 0.0)))
    _cetak(garis, "kunci_ridge_lebih_baik", mae_uji_ridge < mae_uji_tanpa)
    _pipa_lasso, mae_uji_lasso, _mae_latih_lasso, koef_lasso = _pipa(
        Lasso(alpha=1.0), X_latih, y_latih, X_uji, y_uji
    )
    _cetak(garis, "kunci_mae_uji_lasso", mae_uji_lasso)
    _cetak(garis, "kunci_nol_lasso", int(np.sum(koef_lasso == 0.0)))
    _cetak(
        garis,
        "kunci_skala_latih",
        bool(np.allclose(pipa_ridge.named_steps["skala"].mean_, X_latih.mean(axis=0))),
    )
    return garis


def _jalankan_sumber(nama):
    ruang = {"__name__": "modul_03b"}
    for cell in _baca_notebook(nama)["cells"]:
        if cell["cell_type"] != "code":
            continue
        exec(_sumber(cell), ruang, ruang)
    return ruang


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


def test_penalti_tangan_memisahkan_ridge_dan_lasso():
    calon_a = np.array([2.0, 2.0])
    calon_b = np.array([3.0, 0.0])
    assert float(np.sum(calon_a**2)) == 8.0
    assert float(np.sum(calon_b**2)) == 9.0
    assert float(np.sum(np.abs(calon_a))) == 4.0
    assert float(np.sum(np.abs(calon_b))) == 3.0
    assert float(np.sum(calon_a**2)) < float(np.sum(calon_b**2))
    assert float(np.sum(np.abs(calon_b))) < float(np.sum(np.abs(calon_a)))


def test_latihan_tangan():
    calon_a = np.array([4.0, 4.0])
    calon_b = np.array([6.0, 0.0])
    assert float(np.sum(calon_a**2)) < float(np.sum(calon_b**2))
    assert float(np.sum(np.abs(calon_b))) < float(np.sum(np.abs(calon_a)))


def test_ridge_mengalahkan_regresi_tanpa_penalti_dan_lasso_punya_nol():
    _X, _y, X_latih, X_uji, y_latih, y_uji, _indeks, _indeks_uji = _bahan()
    pipa_tanpa, mae_tanpa, mae_latih_tanpa, _koef_tanpa = _pipa(
        LinearRegression(), X_latih, y_latih, X_uji, y_uji
    )
    pipa_ridge, mae_ridge, _mae_latih_ridge, koef_ridge = _pipa(
        Ridge(alpha=5.0), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_lasso, _mae_lasso, _mae_latih_lasso, koef_lasso = _pipa(
        Lasso(alpha=0.5), X_latih, y_latih, X_uji, y_uji
    )
    assert mae_ridge < mae_tanpa
    assert mae_latih_tanpa < mae_tanpa
    assert int(np.sum(koef_ridge == 0.0)) == 0
    assert np.any(koef_lasso == 0.0)
    assert np.allclose(pipa_ridge.named_steps["skala"].mean_, X_latih.mean(axis=0))
    assert not np.allclose(pipa_tanpa.named_steps["skala"].mean_, _X.mean(axis=0))


def test_alpha_nol_tidak_lebih_kecil_dan_bukan_nol_lasso():
    _X, _y, X_latih, X_uji, y_latih, y_uji, _indeks, _indeks_uji = _bahan()
    _pipa_tanpa, mae_tanpa, _mae_latih, _koef_tanpa = _pipa(
        LinearRegression(), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_nol, mae_nol, _latih_nol, koef_ridge_nol = _pipa(
        Ridge(alpha=0.0), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_lasso_nol, _mae_lasso_nol, _latih_lasso_nol, koef_lasso_nol = _pipa(
        Lasso(alpha=0.0, max_iter=10000), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_ridge, _mae_ridge, _latih_ridge, koef_ridge = _pipa(
        Ridge(alpha=5.0), X_latih, y_latih, X_uji, y_uji
    )
    assert not (mae_nol < mae_tanpa), "Alpha nol tidak boleh lebih baik daripada regresi tanpa penalti."
    selisih_ridge_nol = float(np.max(np.abs(_pipa_nol.predict(X_uji) - _pipa_tanpa.predict(X_uji))))
    assert selisih_ridge_nol < 1e-8, (
        "Ridge dengan alpha 0 harus sama dengan regresi linear dalam toleransi 1e-8."
    )
    assert int(np.sum(koef_ridge_nol == 0.0)) == 0, "Koefisien Ridge alpha nol tidak boleh tepat nol."
    assert int(np.sum(koef_lasso_nol == 0.0)) == 0
    assert int(np.sum(koef_ridge == 0.0)) == 0


def test_kunci_alpha_berbeda_tetap_memenuhi_syarat():
    _X, _y, X_latih, X_uji, y_latih, y_uji, _indeks, _indeks_uji = _bahan()
    _pipa_tanpa, mae_tanpa, _latih, _koef = _pipa(
        LinearRegression(), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_ridge, mae_ridge, _latih_ridge, koef_ridge = _pipa(
        Ridge(alpha=2.0), X_latih, y_latih, X_uji, y_uji
    )
    _pipa_lasso, _mae_lasso, _latih_lasso, koef_lasso = _pipa(
        Lasso(alpha=1.0), X_latih, y_latih, X_uji, y_uji
    )
    assert mae_ridge < mae_tanpa
    assert int(np.sum(koef_ridge == 0.0)) == 0
    assert np.any(koef_lasso == 0.0)


def test_menukar_ridge_ke_tempat_lasso_kehilangan_nol():
    _X, _y, X_latih, X_uji, y_latih, y_uji, _indeks, _indeks_uji = _bahan()
    _pipa_ridge, _mae, _latih, koef = _pipa(
        Ridge(alpha=0.5), X_latih, y_latih, X_uji, y_uji
    )
    assert not np.any(koef == 0.0)


def test_mutasi_hapus_skala_memicu_assert():
    """Menghapus StandardScaler harus gagal pada assert, bukan KeyError."""
    ruang = {"__name__": "modul_03b"}
    kena = False
    for cell in _baca_notebook("notebook.ipynb")["cells"]:
        if cell["cell_type"] != "code":
            continue
        src = _sumber(cell).replace("StandardScaler().fit(X_latih)", "None")
        for nama in ("skala_tanpa", "skala_ridge", "skala_nol", "skala_lasso"):
            src = src.replace(f"{nama}.transform(X_latih)", "X_latih")
            src = src.replace(f"{nama}.transform(X_uji)", "X_uji")
        try:
            exec(src, ruang, ruang)
        except AssertionError:
            kena = True
            break
        except KeyError as salah:
            raise AssertionError("hapus StandardScaler hanya memicu KeyError") from salah
    assert kena, "Mutasi hapus StandardScaler tidak memicu assert."


def test_notebook_dijalankan_dan_assert_di_sel_lulus():
    ruang = _jalankan_sumber("notebook.ipynb")
    assert ruang["mae_uji_ridge"] < ruang["mae_uji_tanpa"]
    assert np.any(ruang["koef_lasso"] == 0.0)
    assert int(np.sum(ruang["koef_ridge"] == 0.0)) == 0
    kunci = _jalankan_sumber("latihan-kunci.ipynb")
    assert kunci["mae_uji_ridge"] < kunci["mae_uji_tanpa"]
    assert np.any(kunci["koef_lasso"] == 0.0)
    _jalankan_sumber("latihan.ipynb")


def test_sel_kunci_memuat_assert():
    teks = _seluruh_sumber("notebook.ipynb")
    assert "assert mae_uji_ridge < mae_uji_tanpa" in teks
    assert "assert int(np.sum(koef_ridge == 0.0)) == 0" in teks
    assert "assert np.any(koef_lasso == 0.0)" in teks
    assert "Ridge(alpha=5.0)" in teks
    assert "Lasso(alpha=0.5)" in teks
    kunci = _seluruh_sumber("latihan-kunci.ipynb")
    assert "assert mae_uji_ridge < mae_uji_tanpa" in kunci
    assert "assert np.any(koef_lasso == 0.0)" in kunci
    assert "Ridge(alpha=2.0)" in kunci
    assert "Lasso(alpha=1.0)" in kunci


def test_keluaran_notebook_sama_dengan_hitung_ulang():
    assert _baris_stream("notebook.ipynb") == _garis_notebook()
    assert _baris_stream("latihan.ipynb") == []
    assert _baris_stream("latihan-kunci.ipynb") == _garis_kunci()


def test_latihan_tanpa_output_tersimpan():
    nb = _baca_notebook("latihan.ipynb")
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        assert cell.get("outputs") == []
        assert cell.get("execution_count") is None


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
    for istilah in ("regularisasi", "Ridge", "Lasso"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert PATCH_ANGKA.search(teks) is None
    assert ANGKA_VERSI not in teks
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "uv sync" not in teks.replace("uv sync --frozen", "")
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]
    assert "ujian tingkat" in teks.lower()
    assert "tidak menutup tingkat" in teks.lower()


def test_pyproject_dan_lock_di_root():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    syarat = 'requires-python = "==' + ANGKA_VERSI + '.*"'
    assert syarat in teks
    assert PATCH_ANGKA.search(teks) is None
    assert "phase1-ml/modul-03b-regularisasi/tests" in teks
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == ANGKA_VERSI
    kunci = (REPO / "uv.lock").read_text(encoding="utf-8")
    assert syarat in kunci
    assert PATCH_ANGKA.search(kunci) is None
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()


def test_berkas_modul_tanpa_angka_versi_dan_kata_larang():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if LEWATI.intersection(path.parts):
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path
        assert ANGKA_VERSI not in teks, path
        rendah = teks.lower()
        for kata in LARANG:
            assert kata.lower() not in rendah, path


def test_readme_menyalin_keluaran_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for nama in ("notebook.ipynb", "latihan-kunci.ipynb"):
        for baris in _baris_stream(nama):
            assert baris.strip() in readme, baris


def test_kata_teknis_dijelaskan_sebelum_dipakai():
    berkas = [(ROOT / "README.md").read_text(encoding="utf-8")]
    berkas.extend(_seluruh_sumber(nama) for nama in NOTEBOOKS)
    for teks in berkas:
        rendah = teks.lower()
        for kata, kalimat in KALIMAT_TEKNIS.items():
            posisi = rendah.find(kata)
            if posisi < 0:
                continue
            awal = rendah.find(kalimat.lower())
            assert awal != -1 and awal <= posisi, kata


def _kolom_kamus(kamus, istilah):
    baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
    assert len(baris) == 1, istilah
    kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
    assert len(kolom) == 5, kolom
    return kolom


def test_kamus_tiga_istilah_modul_3b():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    baris = kamus.splitlines()
    indeks = [i for i, b in enumerate(baris) if b.startswith("|")]
    assert indeks[-1] - indeks[0] + 1 == len(indeks)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for istilah in ("regularisasi", "Ridge", "Lasso"):
        _nama, arti, perumpamaan, modul, batas = _kolom_kamus(kamus, istilah)
        assert arti
        assert perumpamaan
        assert modul == "3b"
        assert batas
        assert f"Artinya: {arti[0].lower()}{arti[1:]}" in readme
    assert _kolom_kamus(kamus, "over" + "fitting")[3] == "3"
    assert _kolom_kamus(kamus, "data " + "lea" + "kage")[3] == "5a"
