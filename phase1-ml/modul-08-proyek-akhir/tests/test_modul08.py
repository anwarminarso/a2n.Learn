"""Tes modul 8.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import onnxruntime as ort
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT))

from tambang_sintetis import NAMA_FITUR, NAMA_KELAS, buat_batch  # noqa: E402

NOTEBOOKS = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
PATCH_ANGKA = re.compile(r"3\.14\.\d")
OPSET = 22
ATOL = 1e-5


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


def _latih_dan_banding(seed):
    tabel = buat_batch(seed)
    X = tabel[list(NAMA_FITUR)].to_numpy()
    y = tabel["kelas"].to_numpy()
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=seed,
        stratify=y,
    )
    pipeline = Pipeline(
        [
            ("siapkan", StandardScaler()),
            ("model", LogisticRegression(random_state=seed, max_iter=500)),
        ]
    )
    pipeline.fit(X_latih, y_latih)
    masukan = np.ascontiguousarray(X_uji, dtype=np.float32)
    berkas = convert_sklearn(
        pipeline,
        initial_types=[("masukan_angka", FloatTensorType([None, len(NAMA_FITUR)]))],
        target_opset=OPSET,
        options={"zipmap": False},
    )
    sesi = ort.InferenceSession(
        berkas.SerializeToString(),
        providers=["CPUExecutionProvider"],
    )
    pasangan = sesi.run(None, {"masukan_angka": masukan})
    keluar = {item.name: nilai for item, nilai in zip(sesi.get_outputs(), pasangan)}
    return pipeline, masukan, berkas, keluar


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


def test_opset_dan_zipmap_eksplisit():
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama)
        assert "OPSET = 22" in teks
        assert "target_opset=OPSET" in teks
        assert '"zipmap": False' in teks


def test_tidak_ada_unduhan():
    terlarang = ("fetch_", "urlretrieve", "urlopen", "requests.get", "wget ")
    for nama in NOTEBOOKS:
        teks = _seluruh_sumber(nama)
        for pola in terlarang:
            assert pola not in teks
    generator = (ROOT / "tambang_sintetis.py").read_text(encoding="utf-8")
    for pola in terlarang:
        assert pola not in generator


def test_generator_stabil_dan_bukan_unduhan():
    a = buat_batch(42)
    b = buat_batch(42)
    assert a.equals(b)
    assert list(a.columns[:4]) == list(NAMA_FITUR)
    assert set(a["kelas"].tolist()) == {0, 1, 2}
    assert len(a) == len(NAMA_KELAS) * 80
    assert np.isfinite(a[list(NAMA_FITUR)].to_numpy()).all()


def _jalankan_notebook(nama):
    """Jalankan notebook dari sumbernya. Keluaran tersimpan tidak dipakai."""
    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(ROOT / nama, as_version=4)
    NotebookClient(
        nb,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
    ).execute()
    baris = []
    for cell in nb.cells:
        for keluar in cell.get("outputs", []):
            if keluar.get("output_type") != "stream":
                continue
            if keluar.get("name") not in (None, "stdout"):
                continue
            raw = keluar.get("text", "")
            if isinstance(raw, list):
                raw = "".join(raw)
            baris.extend(raw.splitlines())
    return baris


def test_kunci_dijalankan_dan_cocok_dengan_hitungan():
    baris = _jalankan_notebook("latihan-kunci.ipynb")
    teks = "\n".join(baris)
    pipeline, masukan, _berkas, keluar = _latih_dan_banding(42)
    nama = [NAMA_KELAS[int(i)] for i in pipeline.predict(masukan)]
    assert f"nama_uji {nama}" in teks
    assert f"label_mini_python {nama[:8]}" in teks
    assert f"label_mini_onnx {nama[:8]}" in teks
    assert "label_identik True" in teks
    assert "label_mini_identik True" in teks
    assert "opset_dikunci 22" in teks
    assert "opset ai.onnx 22" in teks
    for satu in baris:
        if satu.startswith("selisih_maks ") or satu.startswith("selisih_mini "):
            assert float(satu.split()[1]) <= ATOL
    selisih = float(
        np.max(np.abs(pipeline.predict_proba(masukan) - keluar["probabilities"]))
    )
    assert selisih <= ATOL


def test_toleransi_longgar_ditolak():
    """Batas di kunci harus tetap 1e-5. Angka ini literal, bukan variabel yang bisa dilonggarkan."""
    teks = _seluruh_sumber("latihan-kunci.ipynb")
    assert "assert selisih_maks <= 1e-5" in teks, "Batas selisih maksimum di kunci harus 1e-5."
    assert "assert selisih_mini <= 1e-5" in teks, "Batas selisih mini di kunci harus 1e-5."
    pipeline, masukan, _berkas, keluar = _latih_dan_banding(42)
    selisih = float(
        np.max(np.abs(pipeline.predict_proba(masukan) - keluar["probabilities"]))
    )
    assert selisih < 1e-5, "Selisih maksimum harus lebih kecil dari 1e-5."
    selisih_mini = float(
        np.max(
            np.abs(
                pipeline.predict_proba(masukan)[:8] - keluar["probabilities"][:8]
            )
        )
    )
    assert selisih_mini < 1e-5, "Selisih mini harus lebih kecil dari 1e-5."


def test_ujian_level_pro_label_dan_probabilitas():
    _pipeline, masukan, berkas, keluar = _latih_dan_banding(42)
    domain_kosong = [op.version for op in berkas.opset_import if op.domain == ""]
    assert OPSET in domain_kosong
    label_python = _pipeline.predict(masukan)
    prob_python = _pipeline.predict_proba(masukan)
    np.testing.assert_array_equal(label_python, keluar["label"])
    np.testing.assert_allclose(
        keluar["probabilities"],
        prob_python,
        atol=ATOL,
        rtol=0,
    )
    np.testing.assert_array_equal(label_python[:8], keluar["label"][:8])
    np.testing.assert_allclose(
        keluar["probabilities"][:8],
        prob_python[:8],
        atol=ATOL,
        rtol=0,
    )


def test_keluaran_onnx_adalah_tabel_bukan_kamus():
    _pipeline, _masukan, _berkas, keluar = _latih_dan_banding(42)
    assert keluar["probabilities"].ndim == 2
    assert keluar["probabilities"].shape[1] == len(NAMA_KELAS)
    assert keluar["label"].ndim == 1


def test_latihan_tanpa_output_tersimpan():
    nb = _baca_notebook("latihan.ipynb")
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        assert cell.get("outputs", []) == []
        assert cell.get("execution_count") in (None,)


def test_readme_punya_bagian_wajib_dan_batas_analogi():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    for judul in (
        "Cerita pembuka",
        "Coba sendiri dulu, baru kode",
        "Kesalahan yang paling sering terjadi",
        "Cek pemahaman",
        "Kunci jawaban",
        "Sumber",
        "Ujian tingkat pro",
        "Kriteria lulus",
        "Mini-proyek",
    ):
        assert judul in teks
    for istilah in ("ONNX", "opset", "inferensi"):
        assert istilah in teks
    assert teks.count("Batas analogi") >= 3
    assert "atol=1e-5" in teks
    assert "22" in teks
    assert PATCH_ANGKA.search(teks) is None
    assert re.search(r"\d+\.\d+\.\d+", teks) is None
    assert "uv sync --frozen" in teks
    assert "uv run pytest" in teks
    assert "uv run pytest --nbmake" in teks
    assert "folder modul" not in teks.split("bukan dari folder modul")[0]


def test_pyproject_dan_lock_di_root():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = "==3.14.*"' in teks
    assert "skl2onnx" in teks
    assert "onnxruntime" in teks
    assert PATCH_ANGKA.search(teks) is None
    assert (REPO / ".python-version").read_text(encoding="utf-8").strip() == "3.14"
    kunci = (REPO / "uv.lock").read_text(encoding="utf-8")
    assert 'requires-python = "==3.14.*"' in kunci
    for nama in ("skl2onnx", "onnxruntime", "onnx", "protobuf", "flatbuffers", "ml-dtypes"):
        assert f'name = "{nama}"' in kunci
    assert PATCH_ANGKA.search(kunci) is None
    syarat = (REPO / "requirements.txt").read_text(encoding="utf-8")
    assert "skl2onnx==" in syarat
    assert "onnxruntime==" in syarat
    for nama in ("pyproject.toml", "uv.lock", "requirements.txt"):
        assert not (ROOT / nama).exists()


def test_berkas_modul_tanpa_nomor_patch_python():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        if "obj" in path.parts or "bin" in path.parts:
            continue
        if path.suffix == ".csproj":
            continue
        teks = path.read_text(encoding="utf-8")
        assert PATCH_ANGKA.search(teks) is None, path
        if path.suffix in {".md", ".ipynb", ".py"}:
            assert re.search(r"\d+\.\d+\.\d+", teks) is None, path


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


def test_kamus_tiga_istilah_modul_8():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    for istilah in ("ONNX", "opset", "inferensi"):
        baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
        assert len(baris) == 1, istilah
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert len(kolom) == 5, kolom
        _nama, arti, perumpamaan, modul, batas = kolom
        assert arti
        assert perumpamaan
        assert modul == "8"
        assert batas


def test_tanpa_kata_terlarang_di_modul():
    # Pola disusun dari kepingan supaya berkas tes ini tidak memuat kata utuhnya.
    pola = re.compile("sm" + "p" + "|" + "an" + "tam", re.IGNORECASE)
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(bagian in path.parts for bagian in (".venv", "__pycache__", "obj", "bin")):
            continue
        teks = path.read_text(encoding="utf-8", errors="ignore")
        assert pola.search(teks) is None, path


def test_program_dotnet_menyebut_keluaran_onnx():
    sumber = (ROOT / "dotnet" / "PemanggilOnnx" / "Program.cs").read_text(encoding="utf-8")
    assert "InferenceSession" in sumber
    assert '"label"' in sumber
    assert '"probabilities"' in sumber
    assert "nama_masukan" in sumber


def _sumber_pemanggil():
    return (ROOT / "dotnet" / "PemanggilOnnx" / "Program.cs").read_text(encoding="utf-8")


def test_readme_dotnet_dijalankan_dari_folder_modul():
    teks = (ROOT / "README.md").read_text(encoding="utf-8")
    perintah = "dotnet run --project dotnet/PemanggilOnnx -- model.onnx baris.json keluar.json"
    assert teks.count(perintah) == 2
    assert "phase1-ml/modul-08-proyek-akhir/dotnet/PemanggilOnnx" not in teks
    assert "Dari folder modul ini" in teks


def test_program_menolak_berkas_hilang_json_rusak_dan_panjang_baris():
    sumber = _sumber_pemanggil()
    assert "File.Exists(args[0])" in sumber
    assert "File.Exists(args[1])" in sumber
    assert "berkas tidak ditemukan:" in sumber
    assert "JsonException" in sumber
    assert "baris.json rusak" in sumber
    assert "panjang baris tidak cocok" in sumber
    assert "fitur hilang atau null" in sumber
    assert "baris.json berisi null" in sumber
    assert "nama_masukan hilang atau kosong" in sumber
    assert "angka tidak hingga" in sumber
    assert "jumlah kolom tidak cocok" in sumber
    assert "model.onnx rusak, jalankan notebook ulang" in sumber
    assert "folder keluaran tidak ada" in sumber
    assert "InputMetadata" in sumber
    assert "OnnxRuntimeException" in sumber
    assert "ArgumentException" in sumber
    assert "IOException" in sumber
    assert "berkas masukan kosong" not in sumber
    assert sumber.index("File.Exists(args[0])") < sumber.index("JsonDocument.Parse")
    assert sumber.index("panjang baris tidak cocok") < sumber.index("new InferenceSession")


def test_keluaran_json_modul_diabaikan_git():
    for contoh in (
        "phase1-ml/modul-08-proyek-akhir/baris.json",
        "phase1-ml/modul-08-proyek-akhir/keluar.json",
    ):
        hasil = subprocess.run(
            ["git", "check-ignore", "-q", "--", contoh],
            cwd=REPO,
        )
        assert hasil.returncode == 0, contoh


def _dotnet():
    kandidat = shutil.which("dotnet")
    if kandidat:
        return kandidat
    rumah = Path.home() / ".dotnet" / "dotnet"
    if rumah.is_file():
        return str(rumah)
    return None


def _jalankan_dotnet(argumen):
    return subprocess.run(
        [
            _dotnet(),
            "run",
            "--project",
            str(ROOT / "dotnet" / "PemanggilOnnx"),
            "--",
            *argumen,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_live_model_hilang(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    baris = tmp_path / "baris.json"
    baris.write_text('{"nama_masukan":"masukan_angka","fitur":[[1,2,3,4]]}', encoding="utf-8")
    hasil = _jalankan_dotnet(
        [str(tmp_path / "tidak-ada.onnx"), str(baris), str(tmp_path / "keluar.json")]
    )
    assert hasil.returncode == 1
    assert "berkas tidak ditemukan" in hasil.stderr
    assert "tidak-ada.onnx" in hasil.stderr


def test_live_baris_hilang(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    model = tmp_path / "model.onnx"
    model.write_bytes(b"bukan-onnx")
    hasil = _jalankan_dotnet(
        [str(model), str(tmp_path / "baris.json"), str(tmp_path / "keluar.json")]
    )
    assert hasil.returncode == 1
    assert "berkas tidak ditemukan" in hasil.stderr
    assert "baris.json" in hasil.stderr


def test_live_folder_tidak_ada(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    hilang = tmp_path / "folder-tidak-ada" / "model.onnx"
    baris = tmp_path / "baris.json"
    baris.write_text('{"nama_masukan":"masukan_angka","fitur":[[1,2,3,4]]}', encoding="utf-8")
    hasil = _jalankan_dotnet([str(hilang), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "berkas tidak ditemukan" in hasil.stderr
    assert "folder-tidak-ada" in hasil.stderr


def test_live_json_rusak(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    model = tmp_path / "model.onnx"
    model.write_bytes(b"bukan-onnx")
    baris = tmp_path / "baris.json"
    baris.write_text("{", encoding="utf-8")
    hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "baris.json rusak" in hasil.stderr


def test_live_panjang_baris_tidak_cocok(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    model = tmp_path / "model.onnx"
    model.write_bytes(b"bukan-onnx")
    baris = tmp_path / "baris.json"
    baris.write_text(
        '{"nama_masukan":"masukan_angka","fitur":[[1,2,3,4],[5,6]]}',
        encoding="utf-8",
    )
    hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "panjang baris tidak cocok" in hasil.stderr
    assert "IndexOutOfRangeException" not in hasil.stderr
    assert "IndexOutOfRangeException" not in hasil.stdout


def test_live_roundtrip_label_identik(tmp_path):
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")
    pipeline, masukan, berkas, _keluar = _latih_dan_banding(42)
    delapan = masukan[:8]
    model = tmp_path / "model.onnx"
    baris = tmp_path / "baris.json"
    keluar = tmp_path / "keluar.json"
    model.write_bytes(berkas.SerializeToString())
    baris.write_text(
        json.dumps({"nama_masukan": "masukan_angka", "fitur": delapan.tolist()}),
        encoding="utf-8",
    )
    hasil = _jalankan_dotnet([str(model), str(baris), str(keluar)])
    assert hasil.returncode == 0, hasil.stderr
    data = json.loads(keluar.read_text(encoding="utf-8"))
    python_label = [int(nilai) for nilai in pipeline.predict(delapan)]
    assert [int(nilai) for nilai in data["label"]] == python_label


def _lewati_tanpa_dotnet():
    if _dotnet() is None:
        import pytest

        pytest.skip("dotnet tidak ada")


def _tulis_json(path, muatan):
    path.write_text(json.dumps(muatan), encoding="utf-8")


def test_live_fitur_hilang_atau_null(tmp_path):
    _lewati_tanpa_dotnet()
    model = tmp_path / "model.onnx"
    model.write_bytes(b"x")
    hilang = tmp_path / "hilang.json"
    _tulis_json(hilang, {"nama_masukan": "masukan_angka"})
    kosong = tmp_path / "null.json"
    _tulis_json(kosong, {"nama_masukan": "masukan_angka", "fitur": None})
    for berkas in (hilang, kosong):
        hasil = _jalankan_dotnet([str(model), str(berkas), str(tmp_path / "keluar.json")])
        assert hasil.returncode == 1
        assert "fitur hilang atau null" in hasil.stderr
        assert "berkas masukan kosong" not in hasil.stderr


def test_live_berkas_berisi_null(tmp_path):
    _lewati_tanpa_dotnet()
    model = tmp_path / "model.onnx"
    model.write_bytes(b"x")
    baris = tmp_path / "baris.json"
    baris.write_text("null", encoding="utf-8")
    hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "baris.json berisi null" in hasil.stderr


def test_live_nama_masukan_hilang_atau_kosong(tmp_path):
    _lewati_tanpa_dotnet()
    model = tmp_path / "model.onnx"
    model.write_bytes(b"x")
    kasus = (
        {"fitur": [[1, 2, 3, 4]]},
        {"nama_masukan": None, "fitur": [[1, 2, 3, 4]]},
        {"nama_masukan": "", "fitur": [[1, 2, 3, 4]]},
    )
    for muatan in kasus:
        baris = tmp_path / "baris.json"
        _tulis_json(baris, muatan)
        hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
        assert hasil.returncode == 1, muatan
        assert "nama_masukan hilang atau kosong" in hasil.stderr


def test_live_fitur_baris_kosong(tmp_path):
    _lewati_tanpa_dotnet()
    model = tmp_path / "model.onnx"
    model.write_bytes(b"x")
    baris = tmp_path / "baris.json"
    _tulis_json(baris, {"nama_masukan": "masukan_angka", "fitur": [[]]})
    hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "panjang baris tidak cocok" in hasil.stderr
    assert "baris 0 kosong" in hasil.stderr


def test_live_angka_tidak_hingga(tmp_path):
    _lewati_tanpa_dotnet()
    model = tmp_path / "model.onnx"
    model.write_bytes(b"x")
    baris = tmp_path / "baris.json"
    baris.write_text(
        '{"nama_masukan":"masukan_angka","fitur":[[1e999,1,1,1]]}',
        encoding="utf-8",
    )
    hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
    assert hasil.returncode == 1
    assert "angka tidak hingga" in hasil.stderr


def test_live_model_rusak(tmp_path):
    _lewati_tanpa_dotnet()
    baris = tmp_path / "baris.json"
    _tulis_json(baris, {"nama_masukan": "masukan_angka", "fitur": [[1, 2, 3, 4]]})
    for isi in (b"", b"x", b"bukan-onnx-terpotong"):
        model = tmp_path / "model.onnx"
        model.write_bytes(isi)
        hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
        assert hasil.returncode == 1, isi
        assert "model.onnx rusak, jalankan notebook ulang" in hasil.stderr


def test_live_jumlah_kolom_bukan_dimensi_model(tmp_path):
    _lewati_tanpa_dotnet()
    _pipeline, _masukan, berkas, _keluar = _latih_dan_banding(42)
    model = tmp_path / "model.onnx"
    model.write_bytes(berkas.SerializeToString())
    for lebar in (3, 5):
        baris = tmp_path / "baris.json"
        _tulis_json(
            baris,
            {"nama_masukan": "masukan_angka", "fitur": [[1.0] * lebar]},
        )
        hasil = _jalankan_dotnet([str(model), str(baris), str(tmp_path / "keluar.json")])
        assert hasil.returncode == 1, lebar
        assert "jumlah kolom tidak cocok" in hasil.stderr
        assert f"punya {lebar} angka" in hasil.stderr
        assert "model minta 4" in hasil.stderr


def test_live_folder_keluaran_hilang(tmp_path):
    _lewati_tanpa_dotnet()
    _pipeline, masukan, berkas, _keluar = _latih_dan_banding(42)
    model = tmp_path / "model.onnx"
    baris = tmp_path / "baris.json"
    model.write_bytes(berkas.SerializeToString())
    _tulis_json(
        baris,
        {"nama_masukan": "masukan_angka", "fitur": masukan[:1].tolist()},
    )
    keluar = tmp_path / "folder-hilang" / "keluar.json"
    hasil = _jalankan_dotnet([str(model), str(baris), str(keluar)])
    assert hasil.returncode == 1
    assert "folder keluaran tidak ada" in hasil.stderr
