# Modul 9: Dasar jaringan saraf dan PyTorch

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menyimpan angka dalam tensor, memeriksa gradien yang dihitung otomatis, lalu melatih jaringan saraf pertama dan membandingkannya dengan model Fase 1 pada data yang sama.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa unduhan.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Dasar jaringan saraf dan PyTorch.

## Issue

Modul ini: [#26](https://github.com/anwarminarso/a2n.Learn/issues/26).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 8: Proyek akhir](../../phase1-ml/modul-08-proyek-akhir/). Array dari modul 1 dipakai lagi dengan arti yang sudah ada. Regresi logistik dari modul 4a menjadi pembanding pada data yang sama.

## Cerita pembuka

Kamu mengatur garam pada sup. Satu cicipan terasa hambar. Kamu menambah sedikit, lalu mencicipi lagi. Kamu tidak menuang satu genggam sekaligus, karena satu loncatan besar bisa membuat sup terlalu asin.

Jaringan kecil belajar dengan cara yang mirip. Angka ditaruh di nampan. Kita lihat seberapa meleset tebakannya. Lalu bobot digeser sedikit, berkali-kali. Di modul klasifikasi Fase 1, regresi logistik sudah memilah dua spesies bunga. Modul ini melatih jaringan saraf pertama pada data yang sama, lalu membandingkan jumlah tebakan yang salah.

## Teori

PyTorch adalah nama alat. Mode cepat memakai numpy, yang sudah ada sejak modul 1, supaya gerbang PR tidak memasang paket baru dan tidak mengunduh bobot. Nama langkahnya mengikuti PyTorch: tensor, langkah mundur, dan putaran latihan.

Jalur PyTorch nyata ada di sel akhir `notebook.ipynb`. Sel itu memakai `torch.tensor`, `backward`, dan jaringan kecil pada data iris yang sama, di CPU. Sel jalan hanya bila lingkungan `A2N_TORCH=1` dan paket torch sudah terpasang. Jika tidak, sel mencetak kalimat lewati. Pasang grup opsional dari root repo:

```bash
uv sync --group torch
```

`uv sync` biasa tidak memasang grup itu. Grup ini CPU saja, dari indeks resmi PyTorch. Gerbang PR tetap tanpa torch.

Fungsi kerugian pada latihan ini tetap rata-rata selisih yang dikuadratkan, seperti modul 3. Yang dikuadratkan sekarang adalah selisih antara tebakan peluang dan label 0 atau 1, bukan kilogram. Sigmoid, yaitu fungsi yang mengubah skor menjadi angka antara 0 dan 1, dijelaskan satu kalimat dan belum menjadi entri kamus.

### tensor

Bayangkan nampan telur yang sekaligus mencatat kemiringan. Tiga angka `[1.0, 2.0, 3.0]` punya bentuk `(3,)`. Jumlahnya 6. Nama teknisnya **tensor**: kumpulan angka dengan bentuk tetap yang dihitung sekaligus, dan bisa menyimpan gradien bila langkah hitungannya dicatat.

Di PyTorch, baris yang sama dimulai dengan `torch.tensor`.

**Batas analogi:** nampan pada modul 1 (array) tidak menyimpan gradien. Tensor di mode cepat adalah array numpy. Gradien hanya terisi bila kita menjalankan langkah mundur. Dua nampan yang bentuknya tidak cocok tidak bisa dijumlahkan.

### autograd

Struk belanja menyimpan tiap perkalian. Dari total, kamu berjalan mundur ke harga barang. Nama teknisnya **autograd**: mesin yang menghitung gradien dari langkah hitungan yang baru saja dijalankan, dengan berjalan mundur dari hasil ke masukan.

Di mode cepat, mesinnya hanya untuk `y = x * x`. Di PyTorch, panggilannya `y.backward()`.

**Batas analogi:** struk hanya tahu langkah yang benar-benar dijalankan. Rumus yang tidak ditulis tidak ikut. Autograd tidak menggeser bobot sendirian. Mesin mini di modul ini bukan autograd untuk seluruh jaringan.

### gradien

Pada `y = x * x` dan `x = 4`, kemiringannya `2 * x`, yaitu 8. Langkah mundur juga mengisi 8. Selisihnya 0. Nama teknisnya **gradien**: angka yang menunjukkan arah dan besar perubahan hasil bila satu masukan digeser sedikit.

**Batas analogi:** kemiringan ini lokal, di satu titik, bukan peta seluruh jalan. Pada ReLU di angka nol, kemiringan tidak tunggal. Gradien bukan fungsi kerugian. Gradien nol tidak selalu berarti tebakan sudah benar di data uji.

### jaringan saraf

Beberapa petugas berurutan. Petugas pertama menimbang empat ukuran bunga menjadi empat angka, lalu ReLU mematikan yang negatif. Petugas kedua mengubah empat angka itu menjadi satu skor. Nama teknisnya **jaringan saraf**. Di modul ini yang dimaksud MLP: ada lapisan di antara masukan dan keluaran. MLP tidak menjadi entri terpisah.

**Batas analogi:** petugas tidak memahami nama bunga. Jaringan kecil ini bukan otak dan bukan model besar. Lapisan di tengah tidak wajib mengalahkan regresi logistik pada data yang sama.

### putaran latihan

Satu giliran: hitung tebakan, hitung fungsi kerugian, hitung gradien, geser bobot sedikit. Modul ini mengulang giliran itu 80 kali pada data latih. Nama teknisnya **putaran latihan**.

Di PyTorch, urutannya `loss.backward()` lalu `optimizer.step()`.

**Batas analogi:** satu cicipan tidak menghabiskan masak. Delapan puluh giliran di CPU bukan latihan sampai selesai. Fungsi kerugian yang turun di data latih belum janji salah pada data uji ikut turun.

### fungsi aktivasi

ReLU seperti saklar: angka negatif menjadi nol, angka positif diteruskan. Pada `[-1.0, 0.0, 2.0]` hasilnya `[0.0, 0.0, 2.0]`. Nama teknisnya **fungsi aktivasi**: fungsi yang membelokkan jumlah berbobot, supaya tumpukan lapisan tidak sama dengan satu garis lurus.

Di PyTorch namanya `torch.nn.ReLU`.

**Batas analogi:** saklar ini bukan sel saraf tubuh. Di sebelah kiri nol, kemiringan ReLU nol, jadi masukan itu tidak menggeser bobot pada langkah tersebut. ReLU bukan satu-satunya pilihan. Sigmoid di lapisan akhir hanya mengubah skor menjadi peluang, dan sigmoid belum menjadi entri kamus.

## Coba sendiri dulu, baru kode

Jawab dulu. Jangan gulir ke kunci.

1. Pada `y = x * x` dan `x = 4`, gradiennya berapa?
2. ReLU pada `-1` menghasilkan berapa?

Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

`sklearn.datasets.load_iris` membaca berkas yang sudah terpasang. Tidak ada unduhan. Bukan data asli perusahaan.

Spesies setosa disisihkan, sama seperti modul klasifikasi Fase 1. Yang tinggal versicolor dan virginica, 100 baris. Empat ukuran bunga ikut semua. `feature_names` pada kode adalah nama kolom bawaan dataset, bukan istilah baru.

Data latih 75 baris, data uji 25 baris, dipecah dengan `random_state=SEED`. Rata-rata dan sebaran petunjuk dihitung dari data latih saja, lalu dipakai pada data uji. Itu supaya data uji tidak ikut menyetel timbangan. Label 1 berarti virginica, label 0 berarti versicolor.

Baseline selalu menebak golongan yang paling banyak di data latih. Regresi logistik dilatih pada petunjuk yang sudah digeser, pada data yang sama dengan jaringan.

## Kesalahan yang paling sering terjadi

1. Gradien tangan dan autograd dibanding pada rumus yang berbeda. Di modul ini keduanya untuk `y = x * x` pada `x = 4`.
2. Rata-rata petunjuk dihitung dari seluruh tabel, termasuk data uji. Notebook hanya memakai data latih.
3. Fungsi kerugian yang turun di data latih dibanggakan sebagai nilai akhir. Yang dibanding dengan baseline adalah salah pada data uji.
4. Selisih nol antara jaringan dan regresi logistik dibaca sebagai "jaringan selalu menang". Pada keluaran ini keduanya salah 3. Modul ini tidak mengunci pemenang di antara keduanya.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Perintah dijalankan dari root repo, folder yang berisi `pyproject.toml` dan `uv.lock`:

```bash
uv sync --frozen
uv run pytest
```

Jalur torch, bila ingin dicoba di CPU:

```bash
uv sync --group torch
```

Lalu jalankan notebook dengan `A2N_TORCH=1`. Tanpa itu, sel torch mencetak kalimat lewati.

Sel pertama setiap notebook berisi `SEED = 42`. Mode cepat tidak mengunduh dan tidak memakai GPU. Tiap sel kode setelah sel pertama memuat satu ide.

## Cek pemahaman

1. Apa beda tensor di modul ini dengan array di modul 1?
2. Autograd menggeser bobot, atau hanya mengisi gradien?
3. Pada keluaran notebook, salah uji jaringan lebih kecil daripada baseline, atau tidak?

## Kunci jawaban

1. Array menyimpan angka. Tensor di modul ini bisa menyimpan gradien bila langkah mundurnya dijalankan. Mode cepat memakai array numpy untuk keduanya.
2. Autograd hanya mengisi gradien. Yang menggeser bobot adalah putaran latihan.
3. Lebih kecil. `salah_uji_jaringan` 3 dan `salah_uji_baseline` 13.

## Sumber

- PyTorch contributors. *Tensors*. <https://docs.pytorch.org/docs/stable/tensors.html>
- PyTorch contributors. *Automatic Differentiation with torch.autograd*. <https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html>
- NumPy developers. *Array creation*. <https://numpy.org/doc/stable/user/basics.creation.html>
- scikit-learn developers. `load_iris`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html>
- scikit-learn developers. `LogisticRegression`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>

## Istilah baru yang direncanakan

Arti, perumpamaan, dan batas analogi ada di bagian Teori dan di [kamus](../../docs/kamus-istilah.md). Nama di bawah tetap paling banyak tiga per sesi. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. tensor
2. autograd
3. gradien

### Sesi 2

1. jaringan saraf
2. putaran latihan
3. fungsi aktivasi

## Garis besar bagian

1. Cerita pembuka sehari-hari.
2. Teori enam istilah, dibagi dua sesi.
3. Coba sendiri dulu, baru kode.
4. Kasus iris, data yang sama dengan model Fase 1.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi di bagian Sumber.

Notebook, latihan, dan kunci ada di folder ini. Mode cepat diuji tanpa jaringan.

## Rencana latihan

- Hitung gradien `y = 3 * x` pada `x = 5` sebelum membuka kunci.
- Terapkan ReLU pada `-2`, `0`, dan `4`.
- Cek bahwa fungsi kerugian dari `0.25` ke `0.10` turun minimal `0.15`.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Selisih gradien tangan dan autograd lebih kecil dari `0.00001`.
- Fungsi kerugian pada data latih turun minimal `0.15`.
- Salah pada data uji untuk jaringan lebih kecil daripada baseline. Regresi logistik pada data yang sama ikut dicetak. Modul ini tidak mengunci pemenang di antara jaringan dan regresi logistik.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Tensor dan jaringan sangat kecil, 80 putaran latihan, jalan di CPU, tanpa unduhan. Ini gerbang tiap PR. Kode mode cepat memakai numpy. Nama langkahnya mengikuti PyTorch. Gerbang tidak memasang grup torch, jadi sel torch mencetak kalimat lewati.

### mode penuh

Opsional. Notebook bisa menjalankan sel torch di CPU bila `A2N_TORCH=1`. Lebih banyak putaran pada GPU di MyLegion7i dinilai dari log mentah. Modul ini tidak mengunduh model Hugging Face.

## Model dan dataset kandidat

- Model Hugging Face: tidak ada. Jaringan ditulis di materi.
- Dataset: iris bawaan scikit-learn, supaya sama dengan kasus Fase 1. Bukan unduhan. Bukan data asli perusahaan.
- Pembanding: regresi logistik, arti dari modul 4a, pada data yang sama.
- Status pin: belum dipin, karena tidak ada id yang diunduh.
- Lisensi kartu model tidak berlaku di modul ini. Register: [docs/lisensi-model.md](../../docs/lisensi-model.md).

## Aturan

Aturan ini tetap berlaku pada materi yang sudah ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul 13 memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.

## Keluaran mode cepat

Angka di bawah disalin dari keluaran `notebook.ipynb` dan `latihan-kunci.ipynb`.

```
bentuk (3,)
jumlah 6.0
gradien_tangan 8.0
gradien_autograd 8.0
selisih_gradien 0.0
relu [0.0, 0.0, 2.0]
nama_tensor torch.tensor
nama_mundur backward
nama_relu torch.nn.ReLU
baris 100
spesies ['versicolor', 'virginica']
baris_latih 75
baris_uji 25
petunjuk 4
bentuk_W1 (4, 4)
kerugian_awal 0.247573
kerugian_akhir 0.0296
turun 0.217973
salah_uji_jaringan 3
salah_uji_baseline 13
salah_uji_logistik 3
jalur_torch lewati
jalur_torch nyala
lewati_tensor Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_mundur Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_jaringan Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_data Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_latih Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_hasil Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
bentuk_torch (3,)
jumlah_torch 6.0
gradien_torch 8.0
cpu_torch cpu
baris_torch 75
turun_torch ya
uji_torch lebih_kecil
gradien_latihan 3.0
hasil_relu [0.0, 0.0, 4.0]
turun_latihan 0.15
```
