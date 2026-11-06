"""Tes sederhana modul 2.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import io
import json
import re
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import load_linnerud
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
# Disambung supaya berkas tes tidak memuat angka versi sebagai teks utuh.
ANGKA_VERSI = "3" + ".14"
LEWATI = {".venv", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
KALIMAT_TEKNIS = {
    "indeks": "Indeks adalah nomor baris dari pandas, mulai dari 0.",
    "paket": "Paket adalah kumpulan berkas yang dipasang supaya kode bisa memanggil fungsi pustaka.",
    "pustaka": "Pustaka adalah kumpulan fungsi siap pakai yang dipanggil dari kode.",
    "uv": "uv adalah alat yang memasang paket sesuai daftar terkunci, lalu menjalankan perintah di lingkungan itu.",
}
# Istilah modul lain, disambung di sini supaya tidak berdiri sebagai bahan ajar.
ISTILAH_NANTI = (
    "over" + "fitting",
    "leak" + "age",
    "cross-" + "validation",
    "cross_" + "val",
    "validasi " + "silang",
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
    menit_latih = np.array([8, 10, 12])
    menit_uji = np.array([16])
    rata = float(menit_latih.mean())
    jarak = [int(abs(nilai - rata)) for nilai in menit_latih]
    _cetak(garis, "tangan_rata", rata)
    _cetak(garis, "tangan_jarak", jarak)
    tebakan_latih = np.full(menit_latih.shape, rata)
    _cetak(garis, "tangan_mae", float(mean_absolute_error(menit_latih, tebakan_latih)))
    _cetak(garis, "tangan_jarak_uji", int(abs(menit_uji[0] - rata)))
    tebakan_uji = np.full(menit_uji.shape, rata)
    _cetak(garis, "tangan_mae_uji", float(mean_absolute_error(menit_uji, tebakan_uji)))
    _cetak(garis, "tangan_bertanda", float((menit_latih - rata).mean()))
    _cetak(garis, "tangan_mae_hafal", float(mean_absolute_error(menit_latih, menit_latih)))

    bahan = load_linnerud(as_frame=True)
    tabel = pd.DataFrame(
        {
            "Situps": bahan.data["Situps"],
            "Weight": bahan.target["Weight"],
        }
    )
    _cetak(garis, "kasus_baris", int(tabel.shape[0]))
    _cetak(garis, "kasus_kolom", int(tabel.shape[1]))
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    _cetak(garis, "kasus_baris_latih", int(len(latih)))
    _cetak(garis, "kasus_baris_uji", int(len(uji)))
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(latih[["Situps"]], latih["Weight"])
    nilai_baseline = float(latih["Weight"].mean())
    _cetak(garis, "kasus_baseline", nilai_baseline)
    tebakan = baseline.predict(uji[["Situps"]])
    _cetak(garis, "kasus_tebakan", float(tebakan[0]))
    _cetak(garis, "kasus_tebakan_sama", bool(np.all(tebakan == tebakan[0])))
    mae_uji = float(mean_absolute_error(uji["Weight"], tebakan))
    mae_latih = float(
        mean_absolute_error(latih["Weight"], baseline.predict(latih[["Situps"]]))
    )
    _cetak(garis, "kasus_mae_uji", mae_uji)
    _cetak(garis, "kasus_mae_latih", mae_latih)
    tebakan_tangan = np.full(len(uji), nilai_baseline)
    mae_tangan = float(mean_absolute_error(uji["Weight"], tebakan_tangan))
    _cetak(
        garis,
        "kasus_mae_sama",
        mae_uji == mae_tangan and float(tebakan[0]) == nilai_baseline,
    )
    _cetak(garis, "kasus_mae_hafal", float(mean_absolute_error(latih["Weight"], latih["Weight"])))
    _latih_lagi, uji_lagi = train_test_split(tabel, test_size=0.25, random_state=42)
    _cetak(garis, "kasus_indeks_uji", uji.index.tolist())
    _cetak(garis, "kasus_indeks_uji_lagi", uji_lagi.index.tolist())
    _cetak(garis, "kasus_sama", uji.index.tolist() == uji_lagi.index.tolist())
    return garis


def _garis_latihan():
    bahan = load_linnerud(as_frame=True)
    tabel = pd.DataFrame(
        {
            "Jumps": bahan.data["Jumps"],
            "Waist": bahan.target["Waist"],
        }
    )
    _latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    _latih_lagi, uji_lagi = train_test_split(tabel, test_size=0.25, random_state=42)
    return [
        " ".join(str(a) for a in args)
        for args in (
            ("indeks_uji", uji.index.tolist()),
            ("indeks_uji_lagi", uji_lagi.index.tolist()),
            ("latihan_indeks_sama", uji.index.tolist() == uji_lagi.index.tolist()),
        )
    ]


def _garis_kunci():
    garis = []
    menit_latih = np.array([4, 6, 8], dtype=float)
    menit_uji = np.array([4, 10], dtype=float)
    rata = float(menit_latih.mean())
    mae = float(mean_absolute_error(menit_uji, np.full(menit_uji.shape, rata)))
    _cetak(garis, "kunci_rata", rata)
    _cetak(garis, "kunci_mae", mae)

    bahan = load_linnerud(as_frame=True)
    tabel = pd.DataFrame(
        {
            "Jumps": bahan.data["Jumps"],
            "Waist": bahan.target["Waist"],
        }
    )
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    rata_pinggang = float(latih["Waist"].mean())
    mae_uji = float(mean_absolute_error(uji["Waist"], np.full(len(uji), rata_pinggang)))
    _cetak(garis, "kunci_baris_latih", int(len(latih)))
    _cetak(garis, "kunci_baris_uji", int(len(uji)))
    _cetak(garis, "kunci_baseline", rata_pinggang)
    _cetak(garis, "kunci_mae_uji", mae_uji)
    garis.extend(_garis_latihan())
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


def test_contoh_tangan():
    menit_latih = np.array([8, 10, 12], dtype=float)
    rata = float(menit_latih.mean())
    assert rata == 10.0
    mae = float(mean_absolute_error(menit_latih, np.full_like(menit_latih, rata)))
    assert mae == 4 / 3
    assert float((menit_latih - rata).mean()) == 0.0
    assert float(mean_absolute_error(np.array([16.0]), np.array([rata]))) == 6.0
    assert float(mean_absolute_error(menit_latih, menit_latih)) == 0.0


def _jalankan_sumber(nama):
    nb = _baca_notebook(nama)
    ruang = {"__name__": "__main__"}
    with redirect_stdout(io.StringIO()):
        for cell in nb["cells"]:
            if cell["cell_type"] != "code":
                continue
            exec(_sumber(cell), ruang, ruang)
    return ruang


def test_notebook_dan_kunci_dijalankan_dari_sumber():
    """Sumber sel dijalankan, jadi assert di dalam notebook ikut terpicu."""
    ruang = _jalankan_sumber("notebook.ipynb")
    assert ruang["baseline"].strategy == "mean", "Baseline harus memakai strategi rata-rata."
    assert ruang["mae_latih"] > ruang["mae_hafal"], (
        "Galat baseline harus lebih besar dari galat model yang menghafal."
    )
    kunci = _jalankan_sumber("latihan-kunci.ipynb")
    assert kunci["baseline"].strategy == "mean", "Baseline kunci harus memakai strategi rata-rata."


def test_kunci_baseline_memakai_dummy_bukan_tautologi():
    teks = _seluruh_sumber("latihan-kunci.ipynb")
    assert "DummyRegressor" in teks, "Kunci baseline harus memakai DummyRegressor."
    assert 'assert float(latih["Waist"].mean()) == rata' not in teks, (
        "Assert baseline tidak boleh membandingkan rata-rata dengan dirinya sendiri."
    )


def test_latihan_tangan():
    menit_latih = np.array([4, 6, 8], dtype=float)
    menit_uji = np.array([4, 10], dtype=float)
    rata = float(menit_latih.mean())
    mae = float(mean_absolute_error(menit_uji, np.full_like(menit_uji, rata)))
    assert rata == 6.0
    assert mae == 3.0


def test_linnerud_bawaan_dan_baseline_mengabaikan_petunjuk():
    bahan = load_linnerud(as_frame=True)
    assert bahan.data.shape == (20, 3)
    assert bahan.target.shape == (20, 3)
    tabel = pd.DataFrame(
        {"Situps": bahan.data["Situps"], "Weight": bahan.target["Weight"]}
    )
    latih, uji = train_test_split(tabel, test_size=0.25, random_state=42)
    assert len(latih) == 15
    assert len(uji) == 5
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(latih[["Situps"]], latih["Weight"])
    tebakan = baseline.predict(uji[["Situps"]])
    assert float(tebakan[0]) == float(latih["Weight"].mean())
    assert np.all(tebakan == tebakan[0])
    assert float(mean_absolute_error(latih["Weight"], latih["Weight"])) == 0.0
    lagi = train_test_split(tabel, test_size=0.25, random_state=42)[1]
    assert uji.index.tolist() == lagi.index.tolist()


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
    for istilah in ("data latih dan data uji", "baseline", "rata-rata selisih mutlak"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert PATCH_ANGKA.search(teks) is None
    assert ANGKA_VERSI not in teks
    assert "uv sync --frozen" in teks
    assert "uv run pytest --nbmake" in teks
    assert "uv sync" not in teks.replace("uv sync --frozen", "")
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]
    for awal in ("Artinya: Data", "Artinya: Cara", "Artinya: Rata-rata"):
        assert awal not in teks


def test_pyproject_dan_lock_di_root():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    syarat = 'requires-python = "==' + ANGKA_VERSI + '.*"'
    assert syarat in teks
    assert PATCH_ANGKA.search(teks) is None
    assert "phase1-ml/modul-02-cara-berpikir-ml" in teks
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == ANGKA_VERSI
    kunci = (REPO / "uv.lock").read_text(encoding="utf-8")
    assert syarat in kunci
    assert PATCH_ANGKA.search(kunci) is None
    assert not (ROOT / "pyproject.toml").exists()
    assert not (ROOT / "uv.lock").exists()
    assert not (ROOT / "requirements.txt").exists()


def test_berkas_modul_tanpa_angka_versi():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if LEWATI.intersection(path.parts):
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path
        assert ANGKA_VERSI not in teks, path


def test_modul_tidak_mengajarkan_istilah_nanti():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if LEWATI.intersection(path.parts):
            continue
        teks = path.read_text(encoding="utf-8").lower()
        for istilah in ISTILAH_NANTI:
            assert istilah not in teks, path


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


def test_kamus_tiga_istilah_modul_2():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("data latih dan data uji", "baseline", "rata-rata selisih mutlak"):
        _nama, arti, perumpamaan, modul, batas = _kolom_kamus(kamus, istilah)
        assert arti
        assert perumpamaan
        assert modul == "2"
        assert batas
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        assert f"Artinya: {arti[0].lower()}{arti[1:]}" in readme
    assert "| ukuran kesalahan |" not in kamus
    for istilah, modul in (("venv", "1"), ("array", "1"), ("DataFrame", "1")):
        assert _kolom_kamus(kamus, istilah)[3] == modul
    assert _kolom_kamus(kamus, "over" + "fitting")[3] == "3"
    assert _kolom_kamus(kamus, "data " + "lea" + "kage")[3] == "5"
