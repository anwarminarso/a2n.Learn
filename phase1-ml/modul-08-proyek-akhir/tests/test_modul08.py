"""Tes modul 8.

Nilai yang dicek dihitung ulang di sini, bukan disalin dari ingatan.
"""

import json
import re
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
