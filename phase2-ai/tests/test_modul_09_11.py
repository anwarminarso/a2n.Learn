"""Tes materi modul 9 sampai 13.

Mode cepat jalan di CPU tanpa jaringan dan tanpa torch. Uji unduhan dilewati
secara bawaan. Uji torch dilewati kecuali A2N_TORCH=1.
"""

import importlib.util
import io
import json
import os
import re
from contextlib import redirect_stdout
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
FASE2 = REPO / "phase2-ai"
MODUL = (
    "modul-09-pytorch",
    "modul-10-tokenisasi-embedding",
    "modul-11-attention-transformer",
    "modul-12-lora",
    "modul-13-model-lokal",
)
NOTEBOOK = ("notebook.ipynb", "latihan.ipynb", "latihan-kunci.ipynb")
SHA40 = re.compile(r"[0-9a-f]{40}")
NAMA_PANGGILAN = ("from_pretrained", "snapshot_download", "hf_hub_download")


def _sumber(cell):
    src = cell["source"]
    if isinstance(src, list):
        return "".join(src)
    return src


def _baca(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _muat_hf():
    spec = importlib.util.spec_from_file_location("muat_hf", FASE2 / "muat_hf.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def _register():
    teks = (REPO / "docs" / "lisensi-model.md").read_text(encoding="utf-8")
    hasil = {}
    for baris in teks.splitlines():
        if not baris.startswith("| `"):
            continue
        kolom = [k.strip().strip("`") for k in baris.strip().strip("|").split("|")]
        hasil[kolom[0]] = kolom[3]
        assert re.fullmatch(r"[0-9a-f]{40}", kolom[3])
    assert len(hasil) == 5
    return hasil


def _kode_fase2():
    berkas = [FASE2 / "muat_hf.py"]
    berkas.extend(sorted(FASE2.glob("modul-*/*")))
    for path in berkas:
        if not path.is_file():
            continue
        if path.suffix == ".py":
            yield path, path.read_text(encoding="utf-8")
        elif path.suffix == ".ipynb":
            nb = _baca(path)
            potong = [
                _sumber(cell)
                for cell in nb["cells"]
                if cell["cell_type"] == "code"
            ]
            yield path, "\n".join(potong)


def _panggilan(teks):
    hasil = []
    for nama in NAMA_PANGGILAN:
        jarum = nama + "("
        mulai = 0
        while True:
            i = teks.find(jarum, mulai)
            if i < 0:
                break
            kedalaman = 0
            akhir = None
            for j in range(i + len(nama), len(teks)):
                if teks[j] == "(":
                    kedalaman += 1
                elif teks[j] == ")":
                    kedalaman -= 1
                    if kedalaman == 0:
                        akhir = j
                        break
            assert akhir is not None, nama
            hasil.append((nama, teks[i:akhir + 1], teks[max(0, i - 80):i]))
            mulai = akhir + 1
    return hasil


def _jalankan(path):
    nb = _baca(path)
    ruang = {"__name__": "__main__"}
    potong = []
    for nomor, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        buf = io.StringIO()
        with redirect_stdout(buf):
            exec(compile(_sumber(cell), f"{path.name}:{nomor}", "exec"), ruang)
        potong.append(buf.getvalue())
    return "".join(potong)


def test_revisi_muat_sama_dengan_register():
    register = _register()
    muat = _muat_hf()
    assert muat.REVISI == register
    assert muat.POLA_UNDUH == (
        "*.safetensors",
        "config.json",
        "generation_config.json",
        "tokenizer.json",
        "tokenizer_config.json",
        "special_tokens_map.json",
        "vocab.txt",
        "merges.txt",
        "vocab.json",
    )


def test_setiap_muatan_hf_memakai_revisi_yang_dipin():
    register = _register()
    jumlah = 0
    for path, teks in _kode_fase2():
        assert "revision=\"main\"" not in teks
        assert "revision='main'" not in teks
        for sha in SHA40.findall(teks):
            assert sha in set(register.values()), (path, sha)
        for nama, panggilan, sebelum in _panggilan(teks):
            jumlah += 1
            assert "revision=revisi" in panggilan, (path, nama)
            if nama == "snapshot_download":
                assert "allow_patterns=POLA_UNDUH" in panggilan
            if nama == "from_pretrained":
                assert "trust_remote_code=False" in panggilan
                if "AutoModel" in sebelum:
                    assert "use_safetensors=True" in panggilan
    assert jumlah == 9


def test_kelas_muat_causal_lm_tanpa_jaringan(monkeypatch):
    import sys
    import types

    rekam = []

    class AutoModel:
        @classmethod
        def from_pretrained(cls, folder, **kwargs):
            rekam.append((cls, kwargs))
            return cls

    class AutoModelForCausalLM(AutoModel):
        pass

    class AutoTokenizer:
        @classmethod
        def from_pretrained(cls, folder, **kwargs):
            return cls

    palsu_tf = types.ModuleType("transformers")
    palsu_tf.AutoModel = AutoModel
    palsu_tf.AutoModelForCausalLM = AutoModelForCausalLM
    palsu_tf.AutoTokenizer = AutoTokenizer

    def snapshot_download(**kwargs):
        rekam.append(kwargs)
        return "folder-lokal"

    palsu_hub = types.ModuleType("huggingface_hub")
    palsu_hub.snapshot_download = snapshot_download
    monkeypatch.setitem(sys.modules, "transformers", palsu_tf)
    monkeypatch.setitem(sys.modules, "huggingface_hub", palsu_hub)

    def _panggil(folder, fungsi):
        spec = importlib.util.spec_from_file_location(
            "muat_" + folder + "_" + fungsi, FASE2 / folder / "muat.py"
        )
        modul = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modul)
        return getattr(modul, fungsi)()

    def _cek_bendera(kelas):
        kelas_muat, kwargs = rekam[-1]
        assert kelas_muat is kelas
        assert kwargs["use_safetensors"] is True
        assert kwargs["trust_remote_code"] is False
        assert kwargs["local_files_only"] is True

    muat = _muat_hf()
    id_kecil = "HuggingFaceTB/SmolLM2-135M-Instruct"
    _tokenizer, model = muat.muat_model(id_kecil)
    assert model is AutoModel
    assert rekam[0]["allow_patterns"] == muat.POLA_UNDUH
    assert rekam[0]["revision"] == muat.REVISI[id_kecil]
    _cek_bendera(AutoModel)
    rekam.clear()
    _tokenizer, model = muat.muat_model(
        "Qwen/Qwen2.5-0.5B-Instruct", AutoModelForCausalLM
    )
    assert model is AutoModelForCausalLM
    _cek_bendera(AutoModelForCausalLM)

    for folder, fungsi in (
        ("modul-10-tokenisasi-embedding", "muat_embedding"),
        ("modul-11-attention-transformer", "muat_bert_kecil"),
    ):
        rekam.clear()
        _tokenizer, model = _panggil(folder, fungsi)
        assert model is AutoModel
        _cek_bendera(AutoModel)

    for folder, fungsi in (
        ("modul-12-lora", "muat_smol"),
        ("modul-12-lora", "muat_qwen"),
        ("modul-13-model-lokal", "muat_dasar"),
        ("modul-13-model-lokal", "muat_penuh"),
    ):
        rekam.clear()
        _tokenizer, model = _panggil(folder, fungsi)
        assert model is AutoModelForCausalLM
        _cek_bendera(AutoModelForCausalLM)


def test_sel_siswa_di_bawah_16_baris():
    for folder in MODUL:
        latihan = FASE2 / folder / "latihan.ipynb"
        for cell in _baca(latihan)["cells"]:
            if cell["cell_type"] != "code":
                continue
            assert cell.get("metadata", {}).get("sel_siswa") is True
            assert len(_sumber(cell).splitlines()) < 16
        for nama in NOTEBOOK:
            for cell in _baca(FASE2 / folder / nama)["cells"]:
                if cell["cell_type"] != "code":
                    continue
                assert len(_sumber(cell).splitlines()) < 16, (folder, nama)


def test_sel_pertama_seed_dan_satu_ide():
    for folder in MODUL:
        for nama in NOTEBOOK:
            nb = _baca(FASE2 / folder / nama)
            assert nb["cells"][0]["cell_type"] == "code"
            assert "SEED = 42" in _sumber(nb["cells"][0])
            kode = [c for c in nb["cells"] if c["cell_type"] == "code"]
            assert "Satu ide:" not in _sumber(kode[0])
            for cell in kode[1:]:
                assert _sumber(cell).count("Satu ide:") == 1
            teks = "\n".join(_sumber(c) for c in kode).replace(" ", "")
            assert "random_state=42" not in teks


def test_latihan_tanpa_keluaran_tersimpan():
    for folder in MODUL:
        for cell in _baca(FASE2 / folder / "latihan.ipynb")["cells"]:
            if cell["cell_type"] != "code":
                continue
            assert cell.get("outputs", []) == []
            assert cell.get("execution_count") is None


def test_mode_cepat_cpu_tanpa_jaringan():
    for folder in MODUL:
        readme = (FASE2 / folder / "README.md").read_text(encoding="utf-8")
        for nama in ("notebook.ipynb", "latihan-kunci.ipynb"):
            keluar = _jalankan(FASE2 / folder / nama)
            assert keluar.strip()
            for baris in keluar.splitlines():
                assert baris.strip() in readme, (folder, nama, baris)


def test_mode_cepat_tidak_mengimpor_torch(monkeypatch):
    import sys
    from importlib.machinery import ModuleSpec

    monkeypatch.delenv("A2N_TORCH", raising=False)

    class Pemblokir:
        def find_spec(self, nama, path, target=None):
            akar = nama.split(".", 1)[0]
            if akar in {"torch", "peft"}:
                return ModuleSpec(nama, self)
            return None

        def create_module(self, spec):
            raise AssertionError(spec.name)

        def exec_module(self, modul):
            raise AssertionError(modul.__name__)

    kunci = {
        nama: sys.modules.pop(nama)
        for nama in list(sys.modules)
        if nama == "torch" or nama.startswith("torch.") or nama == "peft" or nama.startswith("peft.")
    }
    sys.meta_path.insert(0, Pemblokir())
    try:
        for folder in MODUL:
            for nama in ("notebook.ipynb", "latihan-kunci.ipynb"):
                _jalankan(FASE2 / folder / nama)
    finally:
        sys.meta_path.pop(0)
        sys.modules.update(kunci)


@pytest.mark.skipif(
    os.environ.get("A2N_TORCH") != "1",
    reason="Jalur torch dilewati. Set A2N_TORCH=1 bila grup torch terpasang.",
)
def test_torch_backward_dan_lora_nyata():
    import torch
    from peft import LoraConfig, inject_adapter_in_model
    from torch import nn

    torch.manual_seed(42)
    x = torch.tensor(4.0, requires_grad=True)
    y = x * x
    y.backward()
    assert abs(float(x.grad) - 8.0) < 1e-5
    assert x.device.type == "cpu"

    class Jaring(nn.Module):
        def __init__(self):
            super().__init__()
            self.lapisan = nn.Linear(4, 1, bias=False)

        def forward(self, data):
            return self.lapisan(data)

    jaring = Jaring()
    for nilai in jaring.parameters():
        nilai.requires_grad_(False)
    konfigurasi = LoraConfig(r=1, lora_alpha=1, target_modules=["lapisan"], bias="none")
    jaring = inject_adapter_in_model(konfigurasi, jaring)
    data = torch.tensor([[0.2, -0.1, 0.4, 0.3], [0.5, 0.2, -0.3, 0.1]])
    target = torch.tensor([[1.0], [0.0]])
    opt = torch.optim.SGD([p for p in jaring.parameters() if p.requires_grad], lr=0.8)
    opt.zero_grad()
    awal = float(torch.mean((torch.sigmoid(jaring(data)) - target) ** 2).detach())
    for _ in range(40):
        opt.zero_grad()
        rugi = torch.mean((torch.sigmoid(jaring(data)) - target) ** 2)
        rugi.backward()
        opt.step()
    assert awal - float(rugi.detach()) > 0


@pytest.mark.skipif(
    os.environ.get("A2N_UNDUH") != "1",
    reason="Uji jaringan dilewati secara bawaan. Set A2N_UNDUH=1 untuk menjalankannya.",
)
def test_unduh_model_opsional():
    def _panggil(folder, fungsi):
        spec = importlib.util.spec_from_file_location(
            "muat_" + folder, FASE2 / folder / "muat.py"
        )
        modul = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modul)
        return getattr(modul, fungsi)()

    _panggil("modul-10-tokenisasi-embedding", "muat_embedding")
    _panggil("modul-11-attention-transformer", "muat_bert_kecil")
    _panggil("modul-12-lora", "muat_smol")
    _panggil("modul-13-model-lokal", "muat_dasar")
