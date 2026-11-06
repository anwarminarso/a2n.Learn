# Modul 8: Proyek akhir

**Tujuan belajar:** Menyimpan model yang sudah belajar ke berkas yang program lain bisa baca, lalu memeriksa bahwa tebakannya cocok dalam batas yang tertulis.

**Tingkat:** pro

**Issue:** #8

## Cerita pembuka

Kamu menimbang bumbu untuk satu resep dan menulis angkanya di buku catatan. Tetangga mau memasak menu yang sama, tetapi dapurnya memakai aplikasi lain dan tidak bisa membuka bukumu.

Kamu menyalin takaran ke kartu dengan aturan tulis yang sama-sama dikenal. Tetangga mengikuti kartu itu. Timbangan tetangga bisa selisih sebutir garam. Nama masakannya tetap sama, bukan berubah jadi sup.

Modul ini melakukan hal yang sama pada model yang sudah belajar. Kasusnya catatan batch olahan mineral. Angkanya dibuat rumus di repo ini. Bukan timbangan lapangan. Bukan data asli perusahaan. Tidak ada yang diunduh.

## Teori

Di modul ini hanya ada tiga istilah baru. Paket adalah kumpulan kode siap pakai yang dipasang ke proyek. Pustaka adalah paket yang dipanggil dari program. uv memasang paket sesuai daftar yang terkunci di `uv.lock`.

Gambar alurnya dulu:

```
angka mentah
    |
    v
Pipeline (siapkan, lalu model) ---> probabilitas Python
    |
    v
berkas ONNX, edisi yang dikunci
    |                 \
    v                  v
onnxruntime         program .NET
```

`Pipeline`, dari modul 6, merangkai penyiapan angka dan model menjadi satu objek. Regresi logistik, dari modul 4, menghitung probabilitas tiap kelas. Probabilitas adalah angka antara 0 dan 1; pada satu baris jumlah semua kelasnya 1.

Data latih dipakai model untuk belajar. Data uji disisihkan dan tidak dilihat saat belajar. Scaler di dalam Pipeline belajar hanya dari data latih, supaya tidak terjadi data leakage: informasi data uji tidak ikut mengajar.

### ONNX

Kartu resep dengan aturan tulis yang baku bisa diikuti dapur lain tanpa meminjam buku catatanmu. Nama teknisnya **ONNX**: berkas standar yang menyimpan model yang sudah dilatih, supaya program lain bisa menghitung tebakan tanpa membuka kode Python aslinya.

**Batas analogi:** kartu itu tidak memasak sendiri; tetap perlu program pembaca. Berkas ONNX bukan objek Python yang dilatih ulang, dan tidak semua model scikit-learn bisa ditulis menjadi berkas ini. Angka program lain boleh selisih sedikit dari Python.

skl2onnx mengubah model scikit-learn menjadi berkas ONNX. onnxruntime membaca berkas itu dan menghitung tebakan. Nomor versinya tidak ditulis di halaman ini; daftarnya terkunci di `uv.lock`.

### opset

Nomor edisi buku resep memberi tahu pembaca daftar instruksi yang mana. Nama teknisnya **opset**: nomor edisi kumpulan operasi di dalam berkas ONNX. Penulis berkas dan program pembaca harus memakai edisi yang sama.

Modul ini mengunci edisi `22` lewat `OPSET = 22` dan `target_opset=OPSET`. Mengunci artinya nomor itu ditulis tetap, tidak dibiarkan mengikuti bawaan alat.

**Batas analogi:** nomor edisi bukan mutu model dan bukan jumlah kolom. Dua berkas dengan opset yang sama bisa berisi model yang berbeda. Pembaca yang tidak mengenal edisi itu gagal membuka berkas, bukan menghasilkan tebakan yang hampir benar.

### inferensi

Mengikuti kartu resep untuk satu piring memakai resepnya, bukan menulis resep baru. Nama teknisnya **inferensi**: memakai model yang sudah dilatih untuk menghitung tebakan pada catatan yang diberikan, tanpa mengubah model itu.

**Batas analogi:** berhenti berlaku saat model dilatih ulang. Satu tebakan pada satu baris bukan nilai pada seluruh data uji, dan inferensi tidak membuktikan tebakan itu tepat.

### Batas angka

float32 menyimpan angka lebih pendek daripada angka biasa Python, jadi selisih kecil boleh muncul. Batas yang diterima bukan "sama persis".

`atol=1e-5` adalah selisih mutlak paling besar yang masih lulus. Label kelas harus identik: nama kelas yang dipilih harus sama, bukan hanya angkanya dekat.

Rumus setelah gambar di atas, dengan satu baris dan satu kelas:

`selisih = nilai mutlak (probabilitas Python - probabilitas pembaca)`

Lulus bila setiap label kelas identik dan selisih paling besar tidak melebihi `atol=1e-5`.

zipmap yang dibiarkan menyala membungkus probabilitas sebagai kamus nama-dan-angka. Modul ini memasang `zipmap` mati (`False`) supaya yang dibandingkan adalah tabel angka.

## Coba sendiri dulu, baru kode

Urutan contoh: indeks 0 sisihkan, indeks 1 campur, indeks 2 simpan. Indeks adalah nomor posisi, mulai dari 0.

Program Python: 0.05, 0.15, dan 0.80.
Program pembaca: 0.0499999, 0.1499997, dan 0.8000004.

1. Indeks mana yang angkanya paling besar pada keduanya?
2. Apakah indeks itu sama?
3. Apakah selisih mutlak paling besar masih di bawah `1e-5`?

Hitung dengan tangan dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

Generator `tambang_sintetis.py` di folder ini membangun tabel. Tidak ada unduhan. Bukan data asli perusahaan. Modul ini tidak memanggil `make_regression`.

Di `make_regression`, `noise` adalah simpangan baku derau Gauss pada jawaban, dan `bias` adalah geseran tetap pada jawaban. Fungsi `buat_batch` hanya menerima `seed`. `skala` dan `pusat` adalah angka di dalam fungsi, bukan parameter yang dikirim pemanggil. Angka itu dicocokkan ke dokumentasi NumPy:

- `seed` masuk ke `numpy.random.default_rng`. Seed mengunci keadaan pembangkit supaya undian yang sama berulang. Bukan simpangan derau dan bukan geseran tetap.
- Gangguan fitur di dalam fungsi berasal dari `Generator.normal(loc=0, scale=1)`. `loc` adalah rata-rata gangguan. `scale` adalah simpangan bakunya.
- Hasil gangguan dikali angka `skala` tiap kolom. Angka itu tertulis di dalam fungsi. Rata-rata gangguan tetap 0 dan simpangan bakunya sama dengan angka `skala` kolom itu.
- `pusat` di dalam fungsi adalah nilai tengah fitur untuk tiap kelas, ditambahkan sesudah gangguan. Itu geseran pada fitur, bukan `bias` pada jawaban, dan bukan parameter `buat_batch`.

Empat fitur: kadar logam (persen), kadar air (persen), ukuran butir (milimeter), dan kedalaman (meter). Fitur adalah kolom angka yang dipakai untuk menebak. Kelasnya `sisihkan`, `campur`, atau `simpan`.

Notebook membagi data latih dan data uji, melatih Pipeline (`StandardScaler` lalu regresi logistik), mengekspor berkas ONNX pada opset 22, lalu membandingkan inferensi Python dengan onnxruntime pada data uji yang sama.

## Kesalahan yang paling sering terjadi

1. Paket dipasang di luar venv proyek ini. Gejalanya: `import` gagal. Jalankan `uv sync --frozen` dari root repo, lalu jalankan lewat `uv run`. `import` artinya memanggil pustaka yang sudah terpasang.
2. Menuntut angka sama persis. float32 membuat selisih kecil. Yang diuji: label kelas identik, dan selisih probabilitas tidak melebihi `atol=1e-5`.
3. Lupa mengunci opset, jadi edisi berkas mengikuti bawaan alat, bukan edisi 22 yang ditulis di dokumen ini.
4. Membiarkan zipmap menyala. Probabilitas berbentuk kamus, lalu perbandingan tabel gagal meskipun tebakannya dekat.
5. Mengekspor model yang tidak ada di daftar dukungan skl2onnx. Pasangan di modul ini: Pipeline, StandardScaler, dan regresi logistik.
6. Urutan kolom yang dikirim program lain berbeda dari urutan fitur saat belajar. Penyiapan angka sudah di dalam berkas, jadi yang dikirim adalah angka mentah, bukan angka yang sudah di-scaler.
7. Sel dijalankan dari bawah, atau layar masih menyimpan hasil lama. Pakai Restart & Run All.
8. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All. Sel pertama berisi `SEED = 42`. Angka itu dikirim sebagai `seed` ke `buat_batch` (mengunci `default_rng`) dan sebagai `random_state=SEED` pada pembagian data serta model. Keduanya supaya langkah acak berulang. `random_state` bukan parameter generator tabel.

.NET di modul ini adalah program di luar Python yang membaca berkas ONNX yang sama. C# adalah bahasa berkas pemanggil itu; kamu tidak perlu menghafalnya. Alat `dotnet` tidak dipasang oleh `uv sync --frozen`. Proyek `PemanggilOnnx` menargetkan `net10.0`, jadi perintah `dotnet` di bawah membutuhkan SDK .NET 10.

Dari root repo, setelah `model.onnx` dan `baris.json` ada (lihat ujian di bawah):

```bash
dotnet run --project phase1-ml/modul-08-proyek-akhir/dotnet/PemanggilOnnx -- model.onnx baris.json keluar.json
```

CPU only. Versi paket terkunci di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Berkas ONNX bisa dilatih ulang dari program lain. Benar atau salah?
3. Mengapa opset dikunci, dan berapa edisi yang dikunci di modul ini?
4. Apa batas selisih probabilitas, dan apa yang harus identik pada label kelas?
5. Data modul ini diunduh dari internet, atau diambil dari data asli perusahaan. Benar atau salah?
6. Untuk apa `SEED = 42`?
7. Salin baris `label_identik`, `selisih_maks`, dan `dalam_batas` dari keluaran notebook.

### Kunci jawaban

1. **ONNX:** berkas standar yang menyimpan model yang sudah dilatih, supaya program lain bisa menghitung tebakan tanpa membuka kode Python aslinya. **opset:** nomor edisi kumpulan operasi di dalam berkas ONNX. Penulis berkas dan program pembaca harus memakai edisi yang sama. **inferensi:** memakai model yang sudah dilatih untuk menghitung tebakan pada catatan yang diberikan, tanpa mengubah model itu.
2. Salah. Berkas ONNX bukan objek Python yang dilatih ulang dari program lain.
3. Supaya penulis berkas dan program pembaca memakai edisi yang sama. Edisi yang dikunci: 22. Lihat baris `opset_dikunci` pada keluaran.
4. Batasnya `atol=1e-5`. Label kelas harus identik. Lihat baris `label_identik` dan `dalam_batas` pada keluaran.
5. Salah. Tabel dibuat generator di repo. Bukan unduhan. Bukan data asli perusahaan.
6. Supaya undian yang sama berulang. Pada generator, `seed` mengunci `default_rng`. Pada pembagian data dan model, angka yang sama masuk lewat `random_state`.
7. Tiga baris itu ada di keluaran yang disalin di bawah.

### Angka yang disalin dari keluaran notebook

Jawaban "coba sendiri", angka batch, dan hasil banding disalin dari keluaran `notebook.ipynb` dan `latihan-kunci.ipynb`. Baris yang dicetak notebook utama juga ada di kunci. Baris `nama_uji` hanya dicetak kunci, bukan notebook utama. Jangan dibulatkan dengan tangan.

Dua baris `opset ai.onnx 22` berarti konverter menuliskan edisi yang sama dua kali. Edisi yang kita kunci tetap 22. Baris `opset ai.onnx.ml 1` adalah edisi domain lain yang dipilih konverter, bukan kunci kita.

```
selisih_contoh 3.9999999990047996e-07
batas 1e-05
contoh_dalam_batas True
kelas_contoh_python 2
kelas_contoh_pembaca 2
label_contoh_identik True
baris 240
kolom 5
fitur ['kadar_logam_persen', 'kadar_air_persen', 'ukuran_butir_mm', 'kedalaman_m']
nama_kelas ['sisihkan', 'campur', 'simpan']
n_latih 180
n_uji 60
baris_uji 60
opset_dikunci 22
opset ai.onnx.ml 1
opset ai.onnx 22
opset ai.onnx 22
label_identik True
selisih_maks 6.787675388419956e-08
dalam_batas True
nama_uji ['sisihkan', 'campur', 'campur', 'sisihkan', 'simpan', 'sisihkan', 'sisihkan', 'sisihkan', 'sisihkan', 'campur', 'sisihkan', 'simpan', 'simpan', 'sisihkan', 'sisihkan', 'sisihkan', 'campur', 'campur', 'sisihkan', 'simpan', 'simpan', 'sisihkan', 'sisihkan', 'campur', 'campur', 'simpan', 'simpan', 'simpan', 'simpan', 'sisihkan', 'campur', 'campur', 'campur', 'simpan', 'campur', 'sisihkan', 'simpan', 'simpan', 'campur', 'simpan', 'campur', 'sisihkan', 'sisihkan', 'campur', 'campur', 'sisihkan', 'campur', 'sisihkan', 'simpan', 'simpan', 'campur', 'campur', 'simpan', 'simpan', 'campur', 'campur', 'simpan', 'sisihkan', 'simpan', 'simpan']
n_mini 8
label_mini_python ['sisihkan', 'campur', 'campur', 'sisihkan', 'simpan', 'sisihkan', 'sisihkan', 'sisihkan']
label_mini_onnx ['sisihkan', 'campur', 'campur', 'sisihkan', 'simpan', 'sisihkan', 'sisihkan', 'sisihkan']
label_mini_identik True
selisih_mini 6.702036248196208e-08
mini_dalam_batas True
```

## Ujian tingkat pro

Ujian ini menutup tingkat pro. Ada mini-proyek dan empat pertanyaan.

### Kriteria lulus

Lulus bila semua butir ini terpenuhi pada input yang sama:

1. Label kelas dari Python, dari onnxruntime, dan dari program .NET identik.
2. Selisih mutlak probabilitas paling besar antara Python dan onnxruntime tidak melebihi `atol=1e-5`.
3. Selisih mutlak probabilitas paling besar antara Python dan program .NET tidak melebihi `atol=1e-5`.
4. Edisi `ai.onnx` yang tercetak sama dengan yang dikunci, yaitu 22.
5. Empat pertanyaan di bawah dijawab sesuai kunci.

### Mini-proyek

Pakai `SEED` yang sama dengan notebook. Latih Pipeline pada data latih. Ekspor dengan `target_opset=OPSET` dan `zipmap` mati. Ambil 8 baris pertama data uji.

1. Bandingkan `predict` dan `predict_proba` Python dengan keluaran onnxruntime.
2. Simpan berkas dan delapan baris itu, lalu jalankan program .NET pada berkas yang sama. Angka yang dikirim adalah angka mentah, karena scaler sudah di dalam berkas.

```python
from pathlib import Path
import json

Path("model.onnx").write_bytes(berkas.SerializeToString())
Path("baris.json").write_text(
    json.dumps({"nama_masukan": "masukan_angka", "fitur": masukan[:8].tolist()})
)
```

Lalu, dari root repo. Perintah `dotnet` ini membutuhkan SDK .NET 10, karena proyek menargetkan `net10.0`:

```bash
dotnet run --project phase1-ml/modul-08-proyek-akhir/dotnet/PemanggilOnnx -- model.onnx baris.json keluar.json
```

`keluar.json` berisi `label` dan `probabilitas`. Bandingkan dengan Python pada delapan baris yang sama. Jangan menyimpan `model.onnx` ke git.

Bagian Python mini-proyek ini juga dijalankan di `latihan-kunci.ipynb` dan di `tests/test_modul08.py` (`test_ujian_level_pro_label_dan_probabilitas`).

### Pertanyaan

1. Pada 8 baris itu, apa yang harus identik antara Python, onnxruntime, dan program .NET?
2. Berapa batas selisih probabilitas yang masih lulus?
3. Mengapa modul ini tidak menulis "sama persis"?
4. Mengapa yang diekspor Pipeline dengan StandardScaler dan regresi logistik, dan angka apa yang dikirim program .NET?

### Kunci ujian

1. Label kelas. Pada keluaran, `label_mini_identik` bernilai `True`, dan kedua daftar nama kelas sama.
2. `atol=1e-5`. Pada keluaran, `mini_dalam_batas` bernilai `True`.
3. Karena berkas menyimpan angka float32, yaitu lebih pendek daripada angka biasa Python. Selisih kecil boleh ada. Label kelas tetap harus identik.
4. Karena pasangan itu didukung skl2onnx. Tidak semua model scikit-learn bisa diekspor. Program .NET mengirim angka mentah; penyiapan kolom sudah tersimpan di dalam berkas.

## Sumber

- ONNX. *ONNX Versioning*, bagian Operator versioning. <https://github.com/onnx/onnx/blob/main/docs/Versioning.md>
- sklearn-onnx. *Introduction*. <https://onnx.ai/sklearn-onnx/introduction.html>
- sklearn-onnx. *Supported scikit-learn Models*. <https://onnx.ai/sklearn-onnx/supported.html>
- ONNX Runtime. *Python*. <https://onnxruntime.ai/docs/get-started/with-python.html>
- ONNX Runtime. *C#*. <https://onnxruntime.ai/docs/get-started/with-csharp.html>
- scikit-learn developers. *LogisticRegression*. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>
- scikit-learn developers. *Pipeline*. <https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html>
- scikit-learn developers. *Preprocessing data*. <https://scikit-learn.org/stable/modules/preprocessing.html>
- NumPy developers. *Random Generator* (`default_rng`: seed mengunci BitGenerator). <https://numpy.org/doc/stable/reference/random/generator.html>
- NumPy developers. *numpy.random.Generator.normal* (`loc` rata-rata, `scale` simpangan baku). <https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html>
- scikit-learn developers. *make_regression* (`noise` simpangan baku derau pada jawaban, `bias` suku geseran pada model linier). Modul ini tidak memanggil fungsi itu. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html>
- Astral. *uv*. <https://docs.astral.sh/uv/>
