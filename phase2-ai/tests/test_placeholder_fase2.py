"""Tes placeholder Fase 2.

Memeriksa rencana di README, bukan materi yang belum ditulis.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FASE2 = REPO / "phase2-ai"
EM_DASH = "\u2014"
TERLARANG = re.compile(
    "".join(["s", "m", "p"]) + "|" + "".join(["a", "n", "t", "a", "m"]),
    re.IGNORECASE,
)
LEWATI = {".venv", "__pycache__", ".pytest_cache", ".ipynb_checkpoints"}

MODUL = (
    {
        "nomor": "9a",
        "folder": "modul-09a-tensor-autograd",
        "judul": "Tensor dan autograd",
        "bergantung": "Modul 8",
        "prasyarat": "phase1-ml/modul-08-proyek-akhir",
        "istilah": ("tensor", "autograd", "gradien"),
    },
    {
        "nomor": "9b",
        "folder": "modul-09b-jaringan-saraf",
        "judul": "Jaringan saraf kecil dan putaran latihan",
        "bergantung": "Modul 9a",
        "prasyarat": "modul-09a-tensor-autograd",
        "istilah": ("jaringan saraf", "putaran latihan", "fungsi aktivasi"),
    },
    {
        "nomor": "10",
        "folder": "modul-10-embedding-tokenisasi",
        "judul": "Embedding dan tokenisasi",
        "bergantung": "Modul 9b",
        "prasyarat": "modul-09b-jaringan-saraf",
        "istilah": ("token", "embedding", "kemiripan vektor"),
    },
    {
        "nomor": "11a",
        "folder": "modul-11a-attention",
        "judul": "Attention skala mini",
        "bergantung": "Modul 10",
        "prasyarat": "modul-10-embedding-tokenisasi",
        "istilah": ("attention", "kueri, kunci, dan nilai", "Transformer"),
    },
    {
        "nomor": "11b",
        "folder": "modul-11b-klasifikasi-teks",
        "judul": "Klasifikasi teks dengan model siap pakai",
        "bergantung": "Modul 11a",
        "prasyarat": "modul-11a-attention",
        "istilah": ("model pra-latih",),
    },
    {
        "nomor": "12",
        "folder": "modul-12-lora",
        "judul": "Penyelarasan dengan LoRA",
        "bergantung": "Modul 11b",
        "prasyarat": "modul-11b-klasifikasi-teks",
        "istilah": ("penyelarasan", "LoRA", "adapter"),
    },
    {
        "nomor": "13",
        "folder": "modul-13-model-lokal",
        "judul": "Menjalankan model lokal",
        "bergantung": "Modul 12",
        "prasyarat": "modul-12-lora",
        "istilah": ("GGUF", "penggabungan adapter", "peladen lokal"),
    },
    {
        "nomor": "14a",
        "folder": "modul-14a-penyimpan-vektor",
        "judul": "Potongan teks dan penyimpan vektor",
        "bergantung": "Modul 13",
        "prasyarat": "modul-13-model-lokal",
        "istilah": ("potongan", "penyimpan vektor", "pengambilan"),
    },
    {
        "nomor": "14b",
        "folder": "modul-14b-jawaban-sumber",
        "judul": "Jawaban dengan sumber",
        "bergantung": "Modul 14a",
        "prasyarat": "modul-14a-penyimpan-vektor",
        "istilah": ("RAG", "jawaban mengarang", "kutipan sumber"),
    },
    {
        "nomor": "15",
        "folder": "modul-15-agen",
        "judul": "Agen",
        "bergantung": "Modul 14b",
        "prasyarat": "modul-14b-jawaban-sumber",
        "istilah": ("pemanggilan alat", "loop agen", "injeksi prompt"),
    },
)

JUDUL_WAJIB = (
    "## Prasyarat",
    "## Garis besar bagian",
    "## Rencana latihan",
    "## Kriteria lulus",
    "## Mode cepat dan mode penuh",
    "## Model dan dataset kandidat",
    "## Aturan",
)

KALIMAT_ATURAN = (
    "dataset publik berlisensi jelas atau sintetis dari generator di repo",
    "Tanpa data asli perusahaan",
    "Mode cepat memakai model sangat kecil, beberapa langkah, dan jalan di CPU",
    "Mode cepat dipakai untuk gate QA tiap PR",
    "Mode penuh memakai GPU",
    "laptop RTX 5070 8 GB VRAM",
    "di-pin ke revisi",
    "Hanya format safetensors",
    "trust_remote_code=False",
    "Lisensi tiap model dicatat",
    "Pengecekan pakai ambang",
    "loss turun minimal X",
    "bukan angka persis",
    "tidak boleh masuk repo atau di-push ke Hugging Face",
    "127.0.0.1",
    "0.40.14",
    "convert_hf_to_gguf.py",
    "MLX",
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


def _istilah(teks):
    bagian = _bagian(teks, "Istilah baru yang direncanakan")
    return tuple(re.findall(r"^\d+\. (.+)$", bagian, flags=re.M))


def _kolom_kamus(kamus, istilah):
    baris = [b for b in kamus.splitlines() if b.startswith(f"| {istilah} |")]
    assert len(baris) == 1, istilah
    kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
    assert len(kolom) == 5, kolom
    return kolom


def _berkas_yang_dicek():
    berkas = [
        REPO / "README.md",
        REPO / "docs" / "ROADMAP.md",
        REPO / "docs" / "kamus-istilah.md",
        REPO / "data" / "README.md",
        REPO / ".gitignore",
        REPO / "pyproject.toml",
        Path(__file__),
    ]
    berkas.extend(path for path in FASE2.rglob("*") if path.is_file())
    return berkas


def test_hanya_modul_yang_direncanakan():
    folder = sorted(path.name for path in FASE2.iterdir() if path.is_dir() and path.name.startswith("modul-"))
    assert folder == sorted(modul["folder"] for modul in MODUL)


def test_readme_punya_bagian_wajib():
    for modul in MODUL:
        teks = _readme(modul)
        assert teks.startswith(f"# Modul {modul['nomor']}: {modul['judul']}\n")
        assert "**Status:** PLACEHOLDER" in teks
        assert "**Tingkat:** pro" in teks
        assert "**Tujuan belajar:**" in teks
        assert "PLACEHOLDER" in teks
        for judul in JUDUL_WAJIB:
            assert judul in teks, (modul["nomor"], judul)
        assert modul["prasyarat"] in teks
        assert "Notebook, latihan, dan kunci belum dibuat." in teks
        assert len(modul["istilah"]) <= 3
        assert _istilah(teks) == modul["istilah"]


def test_tautan_prasyarat_menunjuk_folder_yang_ada():
    for modul in MODUL:
        teks = _readme(modul)
        if modul["nomor"] == "9a":
            tujuan = REPO / "phase1-ml" / "modul-08-proyek-akhir" / "README.md"
        else:
            tujuan = FASE2 / modul["prasyarat"] / "README.md"
        assert tujuan.is_file(), modul["nomor"]
        assert modul["prasyarat"] in teks


def test_kriteria_draf_dan_mode():
    for modul in MODUL:
        teks = _readme(modul)
        kriteria = _bagian(teks, "Kriteria lulus")
        mode = _bagian(teks, "Mode cepat dan mode penuh")
        kandidat = _bagian(teks, "Model dan dataset kandidat")
        assert "DRAF" in kriteria
        assert "belum dipilih" in kriteria
        assert "### mode cepat" in mode
        assert "### mode penuh" in mode
        assert "CPU" in mode
        assert "RTX 5070" in mode
        assert "belum dipin" in kandidat
        assert "Lisensi belum dicatat" in kandidat
        assert "Apache" not in teks
        assert "CC-BY" not in teks
        assert re.search(r"\bMIT\b", teks) is None


def test_aturan_gate_ada_di_setiap_readme():
    for modul in MODUL:
        aturan = _bagian(_readme(modul), "Aturan")
        for kalimat in KALIMAT_ATURAN:
            assert kalimat in aturan, (modul["nomor"], kalimat)
        assert "data asli perusahaan" in aturan
        assert "safetensors" in aturan


def test_isi_khusus_modul():
    assert "data yang sama" in _readme(MODUL[1])
    assert "Fase 1" in _readme(MODUL[1])
    assert "set uji yang sama" in _readme(MODUL[5])
    assert "fine-tune" in _readme(MODUL[5])
    modul13 = _readme(MODUL[6])
    assert "kontrol tanpa LoRA" in modul13
    assert "convert_hf_to_gguf.py" in modul13
    assert "127.0.0.1" in modul13
    assert "jawaban mengarang" in _readme(MODUL[8])
    modul15 = _readme(MODUL[9])
    assert "injeksi prompt" in modul15
    assert "allowlist" in modul15
    assert "sandbox" in modul15
    assert "shell" in modul15


def test_kamus_mengunci_nama_placeholder():
    kamus = (REPO / "docs" / "kamus-istilah.md").read_text(encoding="utf-8")
    assert "PLACEHOLDER" in kamus.split("Catatan Fase 2:", 1)[0]
    for modul in MODUL:
        for istilah in modul["istilah"]:
            _nama, arti, perumpamaan, pengenal, batas = _kolom_kamus(kamus, istilah)
            assert arti == "PLACEHOLDER"
            assert perumpamaan == "PLACEHOLDER"
            assert batas == "PLACEHOLDER"
            assert pengenal == modul["nomor"]
    indeks = [i for i, b in enumerate(kamus.splitlines()) if b.startswith("|")]
    assert indeks[-1] - indeks[0] + 1 == len(indeks)


def test_roadmap_tabel_fase2():
    teks = (REPO / "docs" / "ROADMAP.md").read_text(encoding="utf-8")
    assert "## Fase 2 " in teks
    assert "PLACEHOLDER" in teks
    assert "garis besar, belum ada issue" not in teks
    assert teks.split("## Fase 2", 1)[0].count("| pro | 8 |") == 1
    for modul in MODUL:
        baris = [b for b in teks.splitlines() if b.startswith(f"| {modul['nomor']} |")]
        assert len(baris) == 1, modul["nomor"]
        kolom = [k.strip() for k in baris[0].strip().strip("|").split("|")]
        assert kolom[0] == modul["nomor"]
        assert kolom[1] == modul["judul"]
        assert kolom[2] == modul["bergantung"]
        assert kolom[3:7] == ["Pyra", "Ursa", "Squal", "Frieren"]
        assert kolom[7] == "pro"
        assert kolom[8] == EM_DASH
    assert "Tidak dipecah" in teks
    assert "modul 9 menjadi 9a" in teks
    assert "Modul 11 menjadi 11a" in teks
    assert "Modul 14 menjadi 14a" in teks


def test_readme_root_menautkan_setiap_modul():
    teks = (REPO / "README.md").read_text(encoding="utf-8")
    assert "PLACEHOLDER" in teks
    for modul in MODUL:
        tautan = f"(phase2-ai/{modul['folder']}/)"
        assert tautan in teks, modul["folder"]
        assert f"| {EM_DASH} |" in teks
    assert "Notebook, latihan, dan kunci menyusul bersama materi." in teks


def test_pyproject_memuat_phase2_tanpa_paket_baru():
    teks = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    assert '"phase2-ai"' in teks
    for nama in ("torch", "transformers", "peft", "datasets"):
        assert nama not in teks


def test_gitignore_menolak_bobot():
    teks = (REPO / ".gitignore").read_text(encoding="utf-8")
    for pola in ("*.safetensors", "*.gguf", "*.pt", "*.pth"):
        assert pola in teks


def test_data_readme_menyebut_aturan_fase2():
    teks = (REPO / "data" / "README.md").read_text(encoding="utf-8")
    assert "phase2-ai" in teks
    assert "safetensors" in teks
    assert "trust_remote_code=False" in teks
    assert "tidak boleh masuk repo atau di-push ke Hugging Face" in teks
    assert "Tanpa data asli perusahaan" in teks


def test_tanpa_kata_terlarang():
    for path in _berkas_yang_dicek():
        if not path.is_file():
            continue
        if LEWATI.intersection(path.parts):
            continue
        if path.suffix == ".pyc":
            continue
        teks = path.read_text(encoding="utf-8")
        assert TERLARANG.search(teks) is None, path
        assert TERLARANG.search(path.name) is None, path
