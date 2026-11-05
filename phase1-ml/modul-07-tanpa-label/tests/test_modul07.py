"""Tes modul 7.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, make_blobs
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = (
    "notebook.ipynb",
    "latihan.ipynb",
    "latihan-kunci.ipynb",
    "ujian.ipynb",
    "ujian-kunci.ipynb",
)
DENGAN_KELUARAN = ("notebook.ipynb", "latihan-kunci.ipynb", "ujian-kunci.ipynb")
TANPA_KELUARAN = ("latihan.ipynb", "ujian.ipynb")
VERSI = "3." + "14"
PATCH_ANGKA = re.compile(re.escape(VERSI))
PATCH_TITIK = re.compile(re.escape(VERSI) + r"\.\d")


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


def _kode(nama):
    nb = _baca_notebook(nama)
    return "\n".join(
        _sumber(cell) for cell in nb["cells"] if cell["cell_type"] == "code"
    )


def _iris_angka():
    iris = load_iris()
    return iris.data, list(iris.feature_names)


def _enam():
    return np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [8, 8],
            [8, 9],
            [20, 0],
        ]
    )


def _pipa_ujian():
    return Pipeline(
        [
            ("skala", StandardScaler()),
            ("kelompok", KMeans(n_clusters=3, n_init=10, random_state=42)),
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
        assert "random_state=SEED" in teks


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama)
        for pola in terlarang:
            assert pola not in teks


def test_satu_sel_satu_ide():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = _sumber(cell).lstrip()
            assert src.startswith("# Angka tetap") or src.startswith("# Satu ide"), nama
            assert src.count("# Satu ide") <= 1


def test_latihan_dan_ujian_tanpa_output_tersimpan():
    for nama in TANPA_KELUARAN:
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            assert cell.get("outputs", []) == [], nama
            assert cell.get("execution_count") in (None,), nama


def test_latihan_tidak_menghitung_jawaban():
    teks = _kode("latihan.ipynb")
    for potongan in ("fit_predict", "IsolationForest", "PCA(", "explained_variance"):
        assert potongan not in teks


def test_ujian_tidak_membocorkan_solusi():
    teks = _kode("ujian.ipynb")
    for potongan in ("Pipeline", "KMeans", "StandardScaler", "lulus_"):
        assert potongan not in teks


def test_empat_titik_dua_kelompok():
    titik = np.array([[1, 1], [1, 2], [8, 8], [9, 8]])
    label = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(titik)
    label_lagi = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(titik)
    assert label[0] == label[1]
    assert label[2] == label[3]
    assert label[0] != label[2]
    assert label.tolist() == label_lagi.tolist()
    assert int(np.sum((titik[0] - titik[1]) ** 2)) == 1
    assert int(np.sum((titik[0] - titik[2]) ** 2)) == 98


def test_enam_titik_clustering_menelan_yang_jauh():
    label = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(_enam())
    assert label[0] == label[1] == label[2]
    assert label[3] == label[4]
    assert label[5] == label[3]


def test_enam_titik_anomali_satu_baris():
    hutan = IsolationForest(
        n_estimators=100,
        contamination=1 / 6,
        max_samples=6,
        random_state=42,
    )
    label = hutan.fit_predict(_enam())
    assert int(np.where(label == -1)[0][0]) == 5
    assert int(np.sum(label == -1)) == 1


def test_iris_tanpa_spesies_dan_pca_menjaga_baris():
    angka, nama = _iris_angka()
    assert nama == [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
    assert "spesies" not in nama
    pipa = Pipeline(
        [
            ("skala", StandardScaler()),
            ("ringkas", PCA(n_components=2, random_state=42)),
        ]
    )
    ringkas = pipa.fit_transform(angka)
    assert ringkas.shape == (angka.shape[0], 2)
    rasio = pipa.named_steps["ringkas"].explained_variance_ratio_
    assert 0 < float(rasio.sum()) < 1
    assert float(rasio[0]) > float(rasio[1])


def test_iris_clustering_memakai_empat_kolom():
    angka, _nama = _iris_angka()
    pipa = Pipeline(
        [
            ("skala", StandardScaler()),
            ("kelompok", KMeans(n_clusters=2, n_init=10, random_state=42)),
        ]
    )
    label = pipa.fit_predict(angka)
    assert angka.shape == (150, 4)
    assert len(label) == 150
    assert int(pipa.named_steps["skala"].n_samples_seen_) == 150


def test_ujian_tiga_syarat():
    X, _nomor = make_blobs(
        n_samples=120, centers=3, n_features=2, random_state=42
    )
    X_latih, X_uji = train_test_split(X, test_size=0.25, random_state=42)
    pipa = _pipa_ujian()
    pipa_lagi = _pipa_ujian()
    pipa.fit(X_latih)
    pipa_lagi.fit(X_latih)
    assert list(pipa.named_steps) == ["skala", "kelompok"]
    assert int(pipa.n_features_in_) == 2
    assert int(pipa.named_steps["skala"].n_samples_seen_) == len(X_latih)
    assert pipa.predict(X_uji).tolist() == pipa_lagi.predict(X_uji).tolist()
    keliru = StandardScaler().fit(X)
    assert int(keliru.n_samples_seen_) == len(X)
    assert int(keliru.n_samples_seen_) != len(X_latih)


def test_readme_punya_bagian_wajib_dan_batas_analogi():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    for judul in (
        "Cerita pembuka",
        "Coba sendiri dulu, baru kode",
        "Kesalahan yang paling sering terjadi",
        "Cek pemahaman",
        "Kunci jawaban",
        "Sumber",
        "Ujian tingkat advanced",
        "Mini-proyek",
        "Kriteria lulus",
        "Pertanyaan ujian",
    ):
        assert judul in teks
    for istilah in ("clustering", "PCA", "deteksi anomali"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert PATCH_ANGKA.search(teks) is None
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]
    assert "Pustaka adalah kumpulan fungsi siap pakai." in teks
    assert "Paket adalah program tambahan yang dipasang ke Python." in teks
    assert "uv adalah program yang memasang paket" in teks
    assert "Indeks adalah nomor baris, mulai dari 0." in teks


def test_readme_menyalin_keluaran_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for nama in DENGAN_KELUARAN:
        nb = _baca_notebook(nama)
        ada_stream = False
        for cell in nb["cells"]:
            for keluaran in cell.get("outputs", []):
                if keluaran.get("output_type") != "stream":
                    continue
                raw = keluaran.get("text", "")
                if isinstance(raw, list):
                    raw = "".join(raw)
                for baris in raw.splitlines():
                    ada_stream = True
                    assert baris.strip() in readme, baris
        assert ada_stream, nama


def test_pyproject_dan_lock_di_root():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = "==' + VERSI + '.*"' in teks
    assert PATCH_TITIK.search(teks) is None
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == VERSI
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()


def test_berkas_modul_tanpa_nomor_versi_python_dan_kata_terlarang():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix == ".pyc":
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path


def test_kamus_tiga_istilah_modul_7():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    baris_modul = []
    for istilah in ("clustering", "PCA", "deteksi anomali"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "7"
        assert batas
        assert "Batas" not in perumpamaan
        baris_modul.append(baris[0])
        assert arti in (ROOT / "README.md").read_text(encoding="utf-8") or arti[0].lower() + arti[1:] in (
            ROOT / "README.md"
        ).read_text(encoding="utf-8")
    assert len(baris_modul) == 3
    jumlah = [b for b in kamus.splitlines() if "| 7 |" in b]
    assert len(jumlah) == 3
