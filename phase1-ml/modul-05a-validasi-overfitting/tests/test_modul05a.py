"""Tes modul 5a.

Angka dihitung ulang di sini, lalu dicocokkan dengan hasil menjalankan sumber
notebook. Keluaran yang tersimpan di berkas bukan kunci tes.
"""

import io
import json
import re
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, TimeSeriesSplit, cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
SEED = 42
FRASA_SALAH = (
    "membawa pola",
    "menukar sebagian",
    "mengatur jarak dua golongan",
    "weights mengatur bagian",
    "membuat baris sintetis",
    "kolom informatif atau redundan",
)


def _sumber(cell):
    src = cell["source"]
    if isinstance(src, list):
        return "".join(src)
    return src


def _baca_notebook(nama):
    return json.loads((ROOT / nama).read_text(encoding="utf-8"))


def _jalankan(nama):
    nb = _baca_notebook(nama)
    ruang = {"__name__": "__main__"}
    buf = io.StringIO()
    with redirect_stdout(buf):
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            exec(compile(_sumber(cell), nama, "exec"), ruang)
    return buf.getvalue()


def _ada(keluar, baris):
    assert baris in keluar.splitlines(), baris


def test_sel_pertama_adalah_seed():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        assert nb["cells"][0]["cell_type"] == "code"
        assert "SEED = 42" in _sumber(nb["cells"][0])


def test_pemanggilan_acak_memakai_seed():
    for nama in NOTEBOOKS:
        teks = _sumber_semua(nama).replace(" ", "")
        assert "random_state=42" not in teks
        assert "default_rng(42)" not in teks
        if nama == "latihan.ipynb":
            continue
        assert "random_state=SEED" in teks


def _sumber_semua(nama):
    nb = _baca_notebook(nama)
    return "\n".join(_sumber(cell) for cell in nb["cells"])


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _sumber_semua(nama)
        for pola in terlarang:
            assert pola not in teks


def test_latihan_tanpa_keluaran_tersimpan():
    nb = _baca_notebook("latihan.ipynb")
    for cell in nb["cells"]:
        assert cell.get("outputs", []) == []


def test_parameter_generator_mengikuti_dokumentasi():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".ipynb", ".py"}:
            continue
        if "tests" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        for frasa in FRASA_SALAH:
            assert frasa not in teks, (path, frasa)
    for nama in ("README.md", *NOTEBOOKS):
        teks = (ROOT / nama).read_text(encoding="utf-8").replace("`", "")
        if "make_classification" not in teks:
            continue
        for frasa in (
            "diundi ulang",
            "hypercube",
            "simpangan baku 1",
            "kombinasi linear",
            "2 kali class_sep",
            "kolom acak yang tidak berguna",
        ):
            assert frasa in teks, (nama, frasa)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    notebook = _sumber_semua("notebook.ipynb")
    for frasa in ("standard_normal", "simpangan baku 1", "sebelum 2", "Generator NumPy"):
        assert frasa in readme
        assert frasa in notebook


def test_notebook_cocok_dengan_hitung_ulang():
    keluar = _jalankan("notebook.ipynb")
    nilai = np.array([2, 4, 6, 8])
    _ada(keluar, f"mean_semua {float(nilai.mean())}")
    _ada(keluar, f"mean_latih {float(nilai[:2].mean())}")
    kolom = nilai.reshape(-1, 1)
    scaler_salah = StandardScaler().fit(kolom)
    scaler_benar = StandardScaler().fit(kolom[:2])
    _ada(keluar, f"mean_scaler_salah {float(scaler_salah.mean_[0])}")
    _ada(keluar, f"mean_scaler_benar {float(scaler_benar.mean_[0])}")

    rng = np.random.default_rng(SEED)
    X_acak = rng.standard_normal((400, 2000))
    y_acak = rng.integers(0, 2, size=400)
    _ada(keluar, f"baris_acak {int(X_acak.shape[0])}")
    _ada(keluar, f"kolom_acak {int(X_acak.shape[1])}")
    X_terpilih = SelectKBest(f_classif, k=15).fit_transform(X_acak, y_acak)
    X_latih_s, X_uji_s, y_latih_s, y_uji_s = train_test_split(
        X_terpilih, y_acak, test_size=0.25, random_state=SEED
    )
    model_salah = LogisticRegression(max_iter=500, random_state=SEED)
    model_salah.fit(X_latih_s, y_latih_s)
    _ada(keluar, f"skor_salah {float(model_salah.score(X_uji_s, y_uji_s))}")
    X_latih_b, X_uji_b, y_latih_b, y_uji_b = train_test_split(
        X_acak, y_acak, test_size=0.25, random_state=SEED
    )
    pilih = SelectKBest(f_classif, k=15).fit(X_latih_b, y_latih_b)
    model_benar = LogisticRegression(max_iter=500, random_state=SEED)
    model_benar.fit(pilih.transform(X_latih_b), y_latih_b)
    _ada(
        keluar,
        f"skor_benar {float(model_benar.score(pilih.transform(X_uji_b), y_uji_b))}",
    )

    jam = np.arange(80)
    acak_latih, acak_uji = train_test_split(
        jam, test_size=0.25, random_state=SEED, shuffle=True
    )
    _ada(keluar, f"acak_uji_min {int(acak_uji.min())}")
    _ada(keluar, f"acak_latih_max {int(acak_latih.max())}")
    _ada(keluar, f"masa_depan_di_latih {int(np.sum(acak_latih > acak_uji.min()))}")
    for i, (bagian_latih, bagian_uji) in enumerate(TimeSeriesSplit(n_splits=3).split(jam)):
        assert bagian_latih.max() < bagian_uji.min()
        _ada(
            keluar,
            " ".join(
                [
                    "giliran",
                    str(i),
                    "latih_akhir",
                    str(int(bagian_latih.max())),
                    "uji_awal",
                    str(int(bagian_uji.min())),
                    "urut",
                    "1",
                ]
            ),
        )

    nomor = np.arange(240)
    y_jam = (np.sin(nomor / 4.0) > 0).astype(int)
    X_jam = nomor.reshape(-1, 1).astype(float)
    Xk_l, Xk_u, yk_l, yk_u = train_test_split(
        X_jam, y_jam, test_size=0.25, random_state=SEED, shuffle=True
    )
    pohon_kocok = DecisionTreeClassifier(max_depth=6, random_state=SEED).fit(Xk_l, yk_l)
    _ada(keluar, f"skor_kocok {float(pohon_kocok.score(Xk_u, yk_u))}")
    potong = int(0.75 * len(nomor))
    pohon_urut = DecisionTreeClassifier(max_depth=6, random_state=SEED).fit(
        X_jam[:potong], y_jam[:potong]
    )
    _ada(keluar, f"skor_urut {float(pohon_urut.score(X_jam[potong:], y_jam[potong:]))}")

    X_pola, y_pola = make_classification(
        n_samples=400,
        n_features=30,
        n_informative=3,
        n_redundant=0,
        n_repeated=0,
        n_clusters_per_class=1,
        class_sep=0.7,
        flip_y=0.1,
        random_state=SEED,
    )
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X_pola, y_pola, test_size=0.3, random_state=SEED, shuffle=True
    )
    dalam = DecisionTreeClassifier(max_depth=None, random_state=SEED).fit(X_latih, y_latih)
    dangkal = DecisionTreeClassifier(max_depth=2, random_state=SEED).fit(X_latih, y_latih)
    skor_latih_dalam = float(dalam.score(X_latih, y_latih))
    skor_uji_dalam = float(dalam.score(X_uji, y_uji))
    skor_latih_dangkal = float(dangkal.score(X_latih, y_latih))
    skor_uji_dangkal = float(dangkal.score(X_uji, y_uji))
    _ada(keluar, f"skor_latih_dalam {skor_latih_dalam}")
    _ada(keluar, f"skor_uji_dalam {skor_uji_dalam}")
    _ada(keluar, f"skor_latih_dangkal {skor_latih_dangkal}")
    _ada(keluar, f"skor_uji_dangkal {skor_uji_dangkal}")
    _ada(keluar, f"selisih_dalam {float(skor_latih_dalam - skor_uji_dalam)}")
    _ada(keluar, f"selisih_dangkal {float(skor_latih_dangkal - skor_uji_dangkal)}")
    assert skor_latih_dalam - skor_uji_dalam > skor_latih_dangkal - skor_uji_dangkal
    lipatan = cross_val_score(
        DecisionTreeClassifier(max_depth=None, random_state=SEED),
        X_latih,
        y_latih,
        cv=KFold(n_splits=5, shuffle=True, random_state=SEED),
    )
    for i, skor in enumerate(lipatan):
        _ada(keluar, f"lipatan {i} {float(skor)}")
    _ada(keluar, f"rata_lipatan {float(lipatan.mean())}")


def test_kunci_cocok_dengan_hitung_ulang():
    keluar = _jalankan("latihan-kunci.ipynb")
    nilai = np.array([1, 3, 5, 7])
    _ada(keluar, f"latihan_mean_semua {float(nilai.mean())}")
    _ada(keluar, f"latihan_mean_latih {float(nilai[:2].mean())}")
    _ada(keluar, "latihan_rata_boleh data latih")
    jam = np.arange(12)
    acak_latih, acak_uji = train_test_split(
        jam, test_size=0.25, random_state=SEED, shuffle=True
    )
    _ada(keluar, f"latihan_acak_uji_min {int(acak_uji.min())}")
    _ada(keluar, f"latihan_acak_latih_max {int(acak_latih.max())}")
    masa = int(np.sum(acak_latih > acak_uji.min()))
    assert masa > 0
    _ada(keluar, f"latihan_masa_depan_di_latih {masa}")
    for i, (bagian_latih, bagian_uji) in enumerate(TimeSeriesSplit(n_splits=2).split(jam)):
        assert bagian_latih.max() < bagian_uji.min()
        _ada(
            keluar,
            " ".join(
                [
                    "latihan_giliran",
                    str(i),
                    "latih_akhir",
                    str(int(bagian_latih.max())),
                    "uji_awal",
                    str(int(bagian_uji.min())),
                    "urut",
                    "1",
                ]
            ),
        )
    _ada(keluar, "latihan_boleh_kocok tidak")
    X, y = make_classification(
        n_samples=300,
        n_features=25,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_clusters_per_class=1,
        class_sep=0.6,
        flip_y=0.12,
        random_state=SEED,
    )
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.3, random_state=SEED, shuffle=True
    )
    dalam = DecisionTreeClassifier(max_depth=None, random_state=SEED).fit(X_latih, y_latih)
    dangkal = DecisionTreeClassifier(max_depth=2, random_state=SEED).fit(X_latih, y_latih)
    selisih_dalam = dalam.score(X_latih, y_latih) - dalam.score(X_uji, y_uji)
    selisih_dangkal = dangkal.score(X_latih, y_latih) - dangkal.score(X_uji, y_uji)
    _ada(keluar, f"latihan_selisih_dalam {float(selisih_dalam)}")
    _ada(keluar, f"latihan_selisih_dangkal {float(selisih_dangkal)}")
    assert selisih_dalam > selisih_dangkal
    _ada(keluar, "latihan_menghafal dalam")


def test_mutasi_nilai_latihan_memicu_assert():
    nb = _baca_notebook("latihan-kunci.ipynb")
    ruang = {"__name__": "__main__"}
    ketemu = False
    with redirect_stdout(io.StringIO()):
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = _sumber(cell).replace(
                "nilai = np.array([1, 3, 5, 7])",
                "nilai = np.array([1, 3, 5, 8])",
            )
            if "np.array([1, 3, 5, 8])" in src:
                ketemu = True
            try:
                exec(compile(src, "latihan-kunci.ipynb", "exec"), ruang)
            except AssertionError:
                assert ketemu
                return
    raise AssertionError("mutasi nilai latihan tidak memicu assert")


def test_readme_punya_bagian_wajib():
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
    assert teks.count("Batas analogi") >= 2
    assert PATCH_ANGKA.search(teks) is None
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]


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


def test_berkas_modul_tanpa_nomor_patch_python():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        assert PATCH_ANGKA.search(path.read_text(encoding="utf-8")) is None, path
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()


def test_kamus_istilah_modul():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    awal = kamus.index("| Istilah |")
    akhir = kamus.index("| recall |")
    akhir = kamus.index("\n", akhir)
    assert "\n\n" not in kamus[awal:akhir]
    for istilah, modul in (("data leakage", "5a"), ("cross-validation", "5a")):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, kolom_modul, batas = kolom
        assert arti and perumpamaan and batas
        assert kolom_modul == modul
