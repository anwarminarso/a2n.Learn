"""Tes placeholder Fase 2.

Memeriksa tujuh modul utuh. docs/ROADMAP.md dikunci agar tetap sama dengan develop.
"""

import hashlib
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FASE2 = REPO / "phase2-ai"
ISSUE = "https://github.com/anwarminarso/a2n.Learn/issues/{}"
ROADMAP_SHA256 = "10b42cb0a032b603185318d7a5de31a21b6dffe22127568bd8deee324a5f23c9"
TERLARANG = re.compile(
    "".join(["s", "m", "p"]) + "|" + "".join(["a", "n", "t", "a", "m"]),
    re.IGNORECASE,
)
LEWATI = {".venv", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}
LISENSI_BOLEH = {"Apache-2.0", "MIT"}

MODUL = (
    {
        "nomor": "9",
        "folder": "modul-09-pytorch",
        "judul": "Dasar jaringan saraf dan PyTorch",
        "roadmap": "Dasar jaringan saraf dan PyTorch",
        "issue": 26,
        "tautan": ("phase1-ml/modul-08-proyek-akhir",),
        "sesi": (
            ("tensor", "autograd", "gradien"),
            ("jaringan saraf", "putaran latihan", "fungsi aktivasi"),
        ),
    },
    {
        "nomor": "10",
        "folder": "modul-10-tokenisasi-embedding",
        "judul": "Embedding dan tokenisasi",
        "roadmap": "Embedding dan tokenisasi",
        "issue": 27,
        "tautan": ("modul-09-pytorch",),
        "sesi": (("token", "embedding", "kemiripan vektor"),),
    },
    {
        "nomor": "11",
        "folder": "modul-11-attention-transformer",
        "judul": "Transformer",
        "roadmap": "Transformer",
        "issue": 28,
        "tautan": ("modul-10-tokenisasi-embedding",),
        "sesi": (
            ("attention", "kueri, kunci, dan nilai", "Transformer"),
            ("model pra-latih",),
        ),
    },
    {
        "nomor": "12",
        "folder": "modul-12-lora",
        "judul": "Fine-tune dengan LoRA",
        "roadmap": "Fine-tune dengan LoRA",
        "issue": 29,
        "tautan": ("modul-11-attention-transformer",),
        "sesi": (("penyetelan halus (fine-tune)", "LoRA", "adapter"),),
    },
    {
        "nomor": "13",
        "folder": "modul-13-model-lokal",
        "judul": "Menjalankan model lokal dengan Ollama",
        "roadmap": "Menjalankan model lokal dengan Ollama",
        "issue": 30,
        "tautan": ("modul-12-lora",),
        "sesi": (("GGUF", "penggabungan adapter", "peladen lokal"),),
    },
    {
        "nomor": "14",
        "folder": "modul-14-rag",
        "judul": "RAG (Retrieval-Augmented Generation)",
        "roadmap": "RAG (Retrieval-Augmented Generation)",
        "issue": 31,
        "tautan": ("modul-13-model-lokal", "modul-10-tokenisasi-embedding"),
        "sesi": (
            ("potongan", "penyimpan vektor", "pengambilan"),
            ("RAG", "jawaban mengarang", "kutipan sumber"),
        ),
    },
    {
        "nomor": "15",
        "folder": "modul-15-agen",
        "judul": "Agen dan proyek akhir Fase 2",
        "roadmap": "Agen dan proyek akhir Fase 2",
        "issue": 32,
        "tautan": ("modul-14-rag", "modul-13-model-lokal", "modul-12-lora"),
        "sesi": (
            ("pemanggilan alat", "loop agen", "injeksi prompt"),
            (),
        ),
    },
)

KALIMAT_ATURAN = (
    "Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.",
    "Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face.",
    "Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR.",
    "Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.",
    "Apache-2.0 atau MIT",
    "Lisensi dicek sebelum unduh",
    "trust_remote_code=False",
    "Hanya format safetensors",
    "belum dipin",
    "127.0.0.1",
    "convert_hf_to_gguf.py",
    "allowlist read-only di folder sandbox",
    "tanpa shell bebas",
    "tanpa akses jaringan internal",
)


def _readme(modul):
    return (FASE2 / modul["folder"] / "README.md").read_text(encoding="utf-8")


def _bagian(teks, judul):
    penanda = f"## {judul}\n"
    awal = teks.index(penanda) + len(penanda)
    sisa = teks[awal:]
    akhir = sisa.find("\n## ")
    if akhir < 0:
        return sisa
    return sisa[:akhir]


def _sesi(teks):
    bagian = _bagian(teks, "Istilah baru yang direncanakan")
    potong = re.split(r"^### Sesi \d+\s*$", bagian, flags=re.M)
    assert len(potong) > 1
    return tuple(
        tuple(re.findall(r"^\d+\. (.+)$", sesi, flags=re.M)) for sesi in potong[1:]
    )


def _kolom_kamus(kamus, istilah):
    baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
    assert len(baris) == 1, istilah
    kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
    assert len(kolom) == 5, kolom
    return kolom


def _berkas_dokumen():
    berkas = [
        REPO / "README.md",
        REPO / "data" / "README.md",
        REPO / "docs" / "kamus-istilah.md",
        REPO / "docs" / "lisensi-model.md",
        REPO / ".gitignore",
        REPO / "pyproject.toml",
        Path(__file__),
    ]
    berkas.extend(path for path in FASE2.rglob("*") if path.is_file())
    return berkas


def test_hanya_tujuh_modul_utuh():
    folder = sorted(path.name for path in FASE2.iterdir() if path.is_dir() and path.name.startswith("modul-"))
    assert folder == [modul["folder"] for modul in MODUL]
    for nama in ("modul-09a-tensor-autograd", "modul-09b-jaringan-saraf", "modul-11a-attention", "modul-11b-klasifikasi-teks", "modul-14a-penyimpan-vektor", "modul-14b-jawaban-sumber"):
        assert not (FASE2 / nama).exists()


def test_readme_punya_bagian_wajib_dan_issue():
    for modul in MODUL:
        teks = _readme(modul)
        assert modul["judul"] == modul["roadmap"]
        assert teks.startswith(f"# Modul {modul['nomor']}: {modul['judul']}\n")
        assert "**Status:** PLACEHOLDER" in teks
        assert "**Tingkat:** pro" in teks
        assert "**Tujuan belajar:**" in teks
        assert modul["roadmap"] in teks
        assert ISSUE.format(modul["issue"]) in teks
        assert ISSUE.format(33) in teks
        for judul in (
            "## Issue",
            "## Prasyarat",
            "## Garis besar bagian",
            "## Rencana latihan",
            "## Kriteria lulus",
            "## Mode cepat dan mode penuh",
            "## Model dan dataset kandidat",
            "## Aturan",
        ):
            assert judul in teks
        assert "Notebook, latihan, dan kunci belum dibuat." in teks
        assert _sesi(teks) == modul["sesi"]
        for sesi in modul["sesi"]:
            assert len(sesi) <= 3


def test_tautan_prasyarat_ada():
    for modul in MODUL:
        teks = _readme(modul)
        for slug in modul["tautan"]:
            assert slug in teks
            if slug.startswith("phase1-ml/"):
                assert (REPO / slug / "README.md").is_file()
            else:
                assert (FASE2 / slug / "README.md").is_file()


def test_kriteria_dan_mode():
    for modul in MODUL:
        teks = _readme(modul)
        kriteria = _bagian(teks, "Kriteria lulus")
        mode = _bagian(teks, "Mode cepat dan mode penuh")
        assert "DRAF" in kriteria
        assert "belum dipilih" in kriteria
        assert "sel siswa" in kriteria
        assert "16 baris atau lebih" in kriteria
        assert "### mode cepat" in mode
        assert "### mode penuh" in mode
        assert "CPU" in mode
        assert "MyLegion7i" in mode
        assert "log mentah" in mode
        assert "RTX 5070" not in teks


def test_aturan_gate():
    for modul in MODUL:
        aturan = _bagian(_readme(modul), "Aturan")
        for kalimat in KALIMAT_ATURAN:
            assert kalimat in aturan, (modul["nomor"], kalimat)


def test_isi_khusus_modul():
    assert "data yang sama" in _readme(MODUL[0])
    assert "Fase 1" in _readme(MODUL[0])
    assert "set uji yang sama" in _readme(MODUL[3])
    assert "fine-tune" in _readme(MODUL[3]).lower() or "Fine-tune" in _readme(MODUL[3])
    modul13 = _readme(MODUL[4])
    assert "kontrol tanpa LoRA" in modul13
    assert "convert_hf_to_gguf.py" in modul13
    modul14 = _readme(MODUL[5])
    assert "jawaban mengarang" in modul14
    modul15 = _readme(MODUL[6])
    assert "injeksi prompt" in modul15
    assert "allowlist" in modul15
    assert "sandbox" in modul15
    assert ".NET" in modul15
    assert "HTTP" in modul15
    assert "127.0.0.1" in modul15


def test_kamus_mengunci_nama_pada_modul_utuh():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    assert "folder berhuruf" in kamus
    for modul in MODUL:
        istilah = [nama for sesi in modul["sesi"] for nama in sesi]
        for nama in istilah:
            _judul, arti, perumpamaan, pengenal, batas = _kolom_kamus(kamus, nama)
            assert arti == perumpamaan == batas == "PLACEHOLDER"
            assert pengenal == modul["nomor"]
        jumlah = [b for b in kamus.splitlines() if f"| {modul['nomor']} |" in b and "PLACEHOLDER" in b]
        assert len(jumlah) == len(istilah)
    assert "9a" not in kamus
    assert "14a" not in kamus
    indeks = [i for i, b in enumerate(kamus.splitlines()) if b.startswith("|")]
    assert indeks[-1] - indeks[0] + 1 == len(indeks)


def test_roadmap_sama_dengan_develop():
    data = (REPO / "docs" / "ROADMAP.md").read_bytes()
    assert hashlib.sha256(data).hexdigest() == ROADMAP_SHA256
    teks = data.decode("utf-8")
    assert "Tracking: #33" in teks
    assert "| 9 | Dasar jaringan saraf dan PyTorch | Modul 8 |" in teks
    assert "| #26 |" in teks
    assert "| #32 |" in teks
    assert "MyLegion7i" in teks
    assert "sel siswa 16 baris atau lebih" in teks
    assert "9a" not in teks


def test_readme_root_menautkan_issue():
    teks = (REPO / "README.md").read_text(encoding="utf-8")
    assert "7 modul utuh" in teks
    assert "docs/lisensi-model.md" in teks
    for modul in MODUL:
        assert f"(phase2-ai/{modul['folder']}/)" in teks
        assert ISSUE.format(modul["issue"]) in teks
    assert "modul-09a-tensor-autograd" not in teks


def test_register_lisensi_hanya_apache_atau_mit():
    teks = (REPO / "docs" / "lisensi-model.md").read_text(encoding="utf-8")
    assert "tanpa mengunduh bobot" in teks
    assert "sebelum unduh" in teks
    baris = [b for b in teks.splitlines() if b.startswith("| `")]
    assert len(baris) == 5
    for baris_kandidat in baris:
        kolom = [k.strip() for k in baris_kandidat.strip().strip("|").split("|")]
        assert kolom[2] in LISENSI_BOLEH, kolom
        assert kolom[3].endswith(".safetensors"), kolom
        assert kolom[4] == "belum dipin"
        assert "bert-tiny" not in kolom[0]
    assert "| 12, 13, 14, 15 |" in teks
    assert "prajjwal1/bert-tiny" in teks
    assert "tidak berisi berkas `.safetensors`" in teks
    assert "GPL" not in teks
    assert "CC-BY" not in teks


def test_data_readme_dan_gitignore():
    data = (REPO / "data" / "README.md").read_text(encoding="utf-8")
    assert "termasuk yang sudah disamarkan" in data
    assert "Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face." in data
    abaikan = (REPO / ".gitignore").read_text(encoding="utf-8")
    assert "Data non-publik dilarang sama sekali." in abaikan
    assert "dari data non-publik" not in abaikan
    for pola in (
        "*.safetensors",
        "*.gguf",
        "*.pt",
        "*.pth",
        "*.faiss",
        "*.npy",
        "*.index",
        "*.ann",
        "chroma/",
        "*.sqlite3",
        "adapters/",
        "outputs/",
        "checkpoints/",
    ):
        assert pola in abaikan


def test_penyelarasan_tidak_dipakai_untuk_fine_tune():
    berkas = [
        REPO / "README.md",
        REPO / "docs" / "kamus-istilah.md",
        REPO / "docs" / "lisensi-model.md",
        REPO / "data" / "README.md",
    ]
    berkas.extend(FASE2.glob("modul-*/README.md"))
    for path in berkas:
        assert "penyelarasan" not in path.read_text(encoding="utf-8"), path
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    assert "| penyetelan halus (fine-tune) |" in kamus
    assert "maksimal tiga istilah baru per sesi" in kamus
    assert "maksimal tiga istilah baru per modul" in kamus


def test_pin_llama_cpp_di_modul_13():
    teks = _readme(MODUL[4])
    assert "ca89968a23a13e571a6b802a9891d22763153b61" in teks
    assert "gguf-py" in teks
    assert "membuat ulang adapter LoRA kecil" in teks
    assert "bukan gerbang PR" in teks
    assert "b12317" not in teks
    assert "jalur GGUF" in teks
    assert "impor GGUF ke Ollama" in teks
    assert "kontrol lewat jalur yang sama" in teks


def test_sandbox_menolak_path_traversal():
    teks = _readme(MODUL[6])
    butir = [
        baris
        for baris in teks.splitlines()
        if "../" in baris and "path absolut" in baris and "symlink" in baris
    ]
    assert len(butir) == 1
    assert "sandbox" in butir[0]


def test_jalur_gguf_hanya_modul_ini_pada_modul_13():
    frasa = "Modul ini memakai jalur GGUF"
    for modul in MODUL:
        teks = _readme(modul)
        if modul["nomor"] == "13":
            assert frasa in teks
        else:
            assert frasa not in teks
            assert "Modul 13 memakai jalur GGUF" in teks


def test_modul_11_memuat_use_safetensors():
    assert "use_safetensors=True" in _readme(MODUL[2])


def test_enam_modul_muat_safetensors_dan_allow_patterns():
    nomor = {"10", "11", "12", "13", "14", "15"}
    blok = None
    for modul in MODUL:
        if modul["nomor"] not in nomor:
            continue
        aturan = _bagian(_readme(modul), "Aturan")
        assert "use_safetensors=True" in aturan
        assert "allow_patterns" in aturan
        butir = tuple(
            baris
            for baris in aturan.splitlines()
            if "use_safetensors=True" in baris or "allow_patterns" in baris
        )
        assert len(butir) == 2, modul["nomor"]
        if blok is None:
            blok = butir
        else:
            assert butir == blok, modul["nomor"]


def test_pyproject_tanpa_paket_baru():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert '"phase2-ai"' in teks
    for nama in ("torch", "transformers", "peft", "datasets"):
        assert nama not in teks


def test_tanpa_kata_terlarang():
    for path in _berkas_dokumen():
        if not path.is_file() or path.suffix == ".pyc":
            continue
        if LEWATI.intersection(path.parts):
            continue
        teks = path.read_text(encoding="utf-8")
        assert TERLARANG.search(teks) is None, path
        assert TERLARANG.search(path.name) is None, path
