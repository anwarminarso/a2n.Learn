"""Tes modul 5b.

Angka dihitung ulang di sini, lalu dicocokkan dengan hasil menjalankan sumber
notebook. Assert di sel kunci ujian gagal bila perbandingan dibalik, bila pohon
di-fit pada seluruh data, atau bila baseline diganti.
"""

import io
import json
import re
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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
DENGAN_KELUARAN = ("notebook.ipynb", "latihan-kunci.ipynb", "ujian-kunci.ipynb")
DOKUMEN_GENERATOR = ("README.md", "notebook.ipynb", "ujian.ipynb", "ujian-kunci.ipynb")
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
BARIS_BASELINE = "kelas_banyak = int(np.bincount(y_latih).argmax())"


def _sumber(cell):
    src = cell["source"]
    if isinstance(src, list):
        return "".join(src)
    return src


def _baca_notebook(nama):
    return json.loads((ROOT / nama).read_text(encoding="utf-8"))


def _sumber_semua(nama):
    nb = _baca_notebook(nama)
    return "\n".join(_sumber(cell) for cell in nb["cells"])


def _jalankan(nama, ganti=None):
    nb = _baca_notebook(nama)
    ruang = {"__name__": "__main__"}
    buf = io.StringIO()
    with redirect_stdout(buf):
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = _sumber(cell)
            if ganti:
                src = src.replace(*ganti)
            exec(compile(src, nama, "exec"), ruang)
    return buf.getvalue()


def _ada(keluar, baris):
    assert baris in keluar.splitlines(), baris


def _pohon_hujan(max_depth):
    X, y = make_classification(
        n_samples=400,
        n_features=6,
        n_informative=3,
        n_redundant=0,
        n_repeated=0,
        n_clusters_per_class=1,
        weights=[0.85, 0.15],
        class_sep=1.1,
        flip_y=0.03,
        random_state=SEED,
    )
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.3, random_state=SEED, shuffle=True, stratify=y
    )
    pohon = DecisionTreeClassifier(max_depth=max_depth, random_state=SEED).fit(
        X_latih, y_latih
    )
    return X, y, X_latih, X_uji, y_latih, y_uji, pohon


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
        if "random_state=" in teks:
            assert "random_state=SEED" in teks
        if "default_rng(" in teks:
            assert "default_rng(SEED)" in teks
    for nama in ("notebook.ipynb", "ujian.ipynb", "ujian-kunci.ipynb"):
        assert "random_state=SEED" in _sumber_semua(nama).replace(" ", "")


def test_satu_sel_satu_ide():
    for nama in NOTEBOOKS:
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            src = _sumber(cell).lstrip()
            assert src.startswith("# Angka tetap") or src.startswith("# Satu ide"), (
                nama,
                src.splitlines()[0],
            )
            assert src.count("# Satu ide") <= 1


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _sumber_semua(nama)
        for pola in terlarang:
            assert pola not in teks


def test_latihan_dan_ujian_tanpa_keluaran_tersimpan():
    for nama in TANPA_KELUARAN:
        nb = _baca_notebook(nama)
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            assert cell.get("outputs", []) == [], nama
            assert cell.get("execution_count") is None, nama


def test_latihan_tidak_memuat_ujian():
    for nama in ("latihan.ipynb", "latihan-kunci.ipynb"):
        teks = _sumber_semua(nama)
        assert "make_classification" not in teks
        assert "ujian_" not in teks
        assert "DecisionTreeClassifier" not in teks


def test_parameter_generator_mengikuti_dokumentasi():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".ipynb", ".py"}:
            continue
        if "tests" in path.parts:
            continue
        teks = path.read_text(encoding="utf-8")
        for frasa in FRASA_SALAH:
            assert frasa not in teks, (path, frasa)
    for nama in DOKUMEN_GENERATOR:
        teks = (ROOT / nama).read_text(encoding="utf-8").replace("`", "")
        assert "make_classification" in teks
        for frasa in (
            "diundi ulang",
            "hypercube",
            "simpangan baku 1",
            "kombinasi linear",
            "2 kali class_sep",
            "kolom acak yang tidak berguna",
            "tidak persis sama",
        ):
            assert frasa in teks, (nama, frasa)


def test_notebook_cocok_dengan_hitung_ulang():
    keluar = _jalankan("notebook.ipynb")
    _ada(keluar, "precision_contoh 0.8")
    _ada(keluar, f"recall_contoh {8 / (8 + 1)}")
    y_benar = np.array([1] * 8 + [0] * 2 + [1] * 1 + [0] * 9)
    y_tebak = np.array([1] * 8 + [1] * 2 + [0] * 1 + [0] * 9)
    _ada(keluar, f"precision_pustaka {float(precision_score(y_benar, y_tebak, pos_label=1))}")
    _ada(keluar, f"recall_pustaka {float(recall_score(y_benar, y_tebak, pos_label=1))}")
    _ada(keluar, "sama True")
    y_jarang = np.array([0] * 95 + [1] * 5)
    tebak_jarang = np.zeros(100, dtype=int)
    _ada(keluar, f"cocok_jarang {float((tebak_jarang == y_jarang).mean())}")
    _ada(keluar, "recall_jarang 0.0")

    X, y, X_latih, X_uji, y_latih, y_uji, pohon = _pohon_hujan(3)
    _ada(keluar, f"bagian_hujan {float(y.mean())}")
    assert float(y.mean()) != 0.15
    kelas = int(np.bincount(y_latih).argmax())
    tebakan = np.full_like(y_uji, kelas)
    _ada(keluar, f"cocok_baseline {float((tebakan == y_uji).mean())}")
    _ada(
        keluar,
        "recall_baseline "
        + str(float(recall_score(y_uji, tebakan, pos_label=1, zero_division=0))),
    )
    tebakan_uji = pohon.predict(X_uji)
    tn, fp, fn, tp = confusion_matrix(y_uji, tebakan_uji, labels=[0, 1]).ravel()
    _ada(keluar, f"tepat_positif {int(tp)}")
    _ada(keluar, f"precision_uji {float(tp / (tp + fp))}")
    _ada(keluar, f"recall_uji {float(tp / (tp + fn))}")
    _ada(keluar, f"skor_latih_dangkal {float(pohon.score(X_latih, y_latih))}")
    dalam = DecisionTreeClassifier(max_depth=None, random_state=SEED).fit(X_latih, y_latih)
    _ada(keluar, f"skor_latih_dalam {float(dalam.score(X_latih, y_latih))}")
    _ada(keluar, f"skor_uji_dalam {float(dalam.score(X_uji, y_uji))}")


def test_kunci_cocok_dengan_hitung_ulang():
    keluar = _jalankan("latihan-kunci.ipynb")
    _ada(keluar, f"latihan_precision {6 / (6 + 3)}")
    _ada(keluar, f"latihan_recall {6 / (6 + 4)}")
    _ada(keluar, "latihan_cocok 0.9")
    _ada(keluar, "latihan_recall_jarang 0.0")
    assert "ujian_" not in keluar


def test_ujian_kunci_cocok_dengan_hitung_ulang():
    keluar = _jalankan("ujian-kunci.ipynb")
    X, y = make_classification(
        n_samples=400,
        n_features=20,
        n_informative=3,
        n_redundant=0,
        n_repeated=0,
        n_clusters_per_class=1,
        weights=[0.85, 0.15],
        class_sep=1.3,
        flip_y=0.02,
        random_state=SEED,
    )
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.3, random_state=SEED, shuffle=True, stratify=y
    )
    kelas = int(np.bincount(y_latih).argmax())
    tebakan = np.full_like(y_uji, kelas)
    _ada(keluar, f"ujian_cocok_baseline {float((tebakan == y_uji).mean())}")
    recall_baseline = float(recall_score(y_uji, tebakan, pos_label=1, zero_division=0))
    _ada(keluar, f"ujian_recall_baseline {recall_baseline}")
    pohon = DecisionTreeClassifier(max_depth=2, random_state=SEED).fit(X_latih, y_latih)
    tebakan_uji = pohon.predict(X_uji)
    tn, fp, fn, tp = confusion_matrix(y_uji, tebakan_uji, labels=[0, 1]).ravel()
    precision = float(precision_score(y_uji, tebakan_uji, pos_label=1, zero_division=0))
    recall = float(recall_score(y_uji, tebakan_uji, pos_label=1, zero_division=0))
    assert precision == tp / (tp + fp)
    assert recall == tp / (tp + fn)
    _ada(keluar, f"ujian_precision {precision}")
    _ada(keluar, f"ujian_recall {recall}")
    dalam = DecisionTreeClassifier(max_depth=None, random_state=SEED).fit(X_latih, y_latih)
    selisih_dalam = float(dalam.score(X_latih, y_latih) - dalam.score(X_uji, y_uji))
    selisih_dangkal = float(pohon.score(X_latih, y_latih) - (tebakan_uji == y_uji).mean())
    assert selisih_dalam > selisih_dangkal
    assert recall > recall_baseline
    _ada(keluar, "ujian_menghafal dalam")
    _ada(keluar, "ujian_model_dipilih dangkal")
    _ada(keluar, "ujian_metrik_dipilih recall")
    _ada(keluar, "ujian_nama_kebocoran data leakage")
    _ada(keluar, "ujian_rata_boleh data latih")


def test_assert_baseline_menghitung_ulang_kelas_mayoritas():
    teks = _sumber_semua("ujian-kunci.ipynb")
    assert teks.count("np.bincount(y_latih).argmax()") >= 2
    assert teks.count("assert ") >= 5


def _mutasi_gagal(ganti, pesan):
    try:
        _jalankan("ujian-kunci.ipynb", ganti=ganti)
    except AssertionError:
        return
    raise AssertionError(pesan)


def test_mutasi_perbandingan_memicu_assert():
    teks = _sumber_semua("ujian-kunci.ipynb")
    assert teks.count("selisih_dalam > selisih_dangkal") == 1
    _mutasi_gagal(
        ("selisih_dalam > selisih_dangkal", "selisih_dalam < selisih_dangkal"),
        "mutasi perbandingan tidak memicu assert",
    )


def test_mutasi_fit_seluruh_data_memicu_assert():
    teks = _sumber_semua("ujian-kunci.ipynb")
    assert teks.count(".fit(X_latih, y_latih)") == 2
    _mutasi_gagal(
        (".fit(X_latih, y_latih)", ".fit(X_ujian, y_ujian)"),
        "mutasi fit seluruh data tidak memicu assert",
    )


def test_mutasi_baseline_memicu_assert():
    _mutasi_gagal(
        (BARIS_BASELINE, "kelas_banyak = 1"),
        "mutasi baseline tidak memicu assert",
    )


def _butir(teks, judul):
    bagian = teks.split(judul, 1)[1]
    hasil = []
    for ln in bagian.splitlines():
        if ln.startswith("#"):
            break
        if len(ln) >= 2 and ln[0].isdigit() and ln[1] == ".":
            hasil.append(ln.strip())
    return hasil


def _markdown(nama):
    nb = _baca_notebook(nama)
    return "\n".join(_sumber(cell) for cell in nb["cells"] if cell["cell_type"] == "markdown")


def test_soal_dan_kunci_bernomor_sama():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    soal = _butir(readme, "### Soal")
    kunci = _butir(readme, "### Kunci ujian")
    assert [b.split(".", 1)[0] for b in soal] == ["1", "2", "3", "4", "5", "6"]
    assert [b.split(".", 1)[0] for b in kunci] == ["1", "2", "3", "4", "5", "6"]
    assert soal == _butir(_markdown("ujian.ipynb"), "### Soal")
    assert soal == _butir(_markdown("ujian-kunci.ipynb"), "### Soal")
    assert kunci == _butir(_markdown("ujian-kunci.ipynb"), "### Kunci ujian")
    assert "### Kunci ujian" not in _markdown("ujian.ipynb")


def test_jawaban_ujian_berada_di_bawah_kunci():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    atas, bawah = teks.split("### Kunci ujian", 1)
    assert "ujian_" not in atas
    for nama in (
        "ujian_precision",
        "ujian_recall_baseline",
        "ujian_selisih_dalam",
        "ujian_selisih_dangkal",
        "ujian_menghafal",
        "ujian_model_dipilih",
        "ujian_metrik_dipilih",
        "ujian_nama_kebocoran",
    ):
        assert nama in bawah
    for angka in ("0.10833333333333328", "0.04761904761904767", "0.631578947368421"):
        assert angka not in atas
        assert angka in bawah


def test_ujian_tidak_membocorkan_solusi():
    nb = _baca_notebook("ujian.ipynb")
    teks = "\n".join(_sumber(cell) for cell in nb["cells"] if cell["cell_type"] == "code")
    for potongan in (
        "DecisionTreeClassifier",
        "precision_score",
        "recall_score",
        "confusion_matrix",
        "ujian_precision",
        "data leakage",
    ):
        assert potongan not in teks


def test_ujian_terdaftar_di_testpaths():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert "phase1-ml/modul-05b-metrik-penilaian" in teks
    for nama in ("ujian.ipynb", "ujian-kunci.ipynb"):
        assert (ROOT / nama).is_file()


def test_readme_punya_bagian_wajib():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    for judul in (
        "Cerita pembuka",
        "Coba sendiri dulu, baru kode",
        "Kesalahan yang paling sering terjadi",
        "Cek pemahaman",
        "Kunci jawaban",
        "Sumber",
        "Ujian tingkat intermediate",
        "Soal",
        "Aturan penilaian",
        "Kunci ujian",
    ):
        assert judul in teks
    assert teks.count("Batas analogi") >= 3
    assert PATCH_ANGKA.search(teks) is None
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]


def test_readme_menyalin_keluaran_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for nama in DENGAN_KELUARAN:
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
    for istilah in ("confusion matrix", "precision", "recall"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti and perumpamaan and batas
        assert modul == "5b"
