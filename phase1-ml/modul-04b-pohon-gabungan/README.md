# Modul 4b: Pohon yang digabung

**Tujuan belajar:** Menggabungkan banyak pohon keputusan dengan dua cara yang berbeda, hutan acak dan gradient boosting, lalu membandingkan banyak tebakan salah pada data uji.

**Tingkat:** intermediate

## Cerita pembuka

Satu pemilah mangga kadang berubah pikiran kalau satu buah aneh ikut masuk ke meja. Kamu bisa bertanya ke banyak pemilah sekaligus, atau menyuruh pemilah baru memperbaiki sisa tebakan pemilah sebelumnya.

Dua cara itu bukan hal yang sama. Modul ini melihat keduanya pada tabel anggur yang sudah terpasang bersama scikit-learn. Tidak ada unduhan. Bukan data asli perusahaan.

## Teori

Paket adalah bundel kode siap pakai. Pustaka adalah kumpulan fungsi di dalam paket. pandas adalah pustaka untuk tabel. scikit-learn adalah pustaka untuk model di modul ini.

Hanya dua istilah baru di bawah. Klasifikasi, dari bagian sebelumnya, artinya model yang menebak golongan, bukan angka. Pohon keputusan artinya bagan pertanyaan ya atau tidak, satu kolom tiap pertanyaan. Dua kalimat itu mengingat arti yang sudah ada, bukan istilah baru di sini.

Data latih dan data uji, baseline, serta overfitting dipakai sesuai kamus. Rata-rata selisih mutlak mengukur jarak tebakan angka, bukan golongan. Di modul ini yang dibandingkan tetap banyak tebakan golongan yang salah. Overfitting: bagus di data latih, termasuk kebetulan-kebetulannya, tetapi buruk di data baru.

### hutan acak

Beberapa pemilah masing-masing melihat sebagian buah, lalu kamu ikut dukungan yang paling besar. Nama teknisnya **hutan acak**: banyak pohon keputusan. Setiap pohon dilatih pada cuplikan baris yang diambil dengan pengembalian, dan setiap pertanyaan hanya melihat sebagian kolom yang diundi. Golongan akhir adalah yang peluang rata-ratanya paling tinggi.

Di scikit-learn nama kelasnya `RandomForestClassifier`.

**Batas analogi:** yang dirata-rata adalah peluang tiap pohon, bukan selalu satu pemilah satu suara. Pada satu baris, notebook menunjukkan keduanya sama; itu tidak selalu begitu, karena satu pohon bisa ragu di dalam daunnya. Pemilahnya pohon dengan resep yang sama pada potongan data yang tumpang-tindih, bukan ahli dengan pengalaman hidup yang berbeda. Kalau pohon-pohonnya sepakat karena datanya mudah, pohon tambahan tidak menambah informasi. Hasilnya bukan satu bagan yang bisa dibaca seperti satu pohon. Nol kesalahan pada satu data uji bukan janji untuk data baru.

### gradient boosting

Pemilah pertama menebak kasar. Pemilah berikutnya hanya menggeser sisa yang masih meleset, sedikit demi sedikit. Nama teknisnya **gradient boosting**: model klasifikasi yang menambah pohon secara berurutan. Setiap pohon baru dilatih pada arah pergeseran skor yang memperkecil kesalahan saat ini. Kata gradient pada nama ini adalah arah pergeseran itu, bukan istilah terpisah. Sumbangan pohon lalu dikecilkan supaya langkahnya tetap kecil. Notebook mencetak pengali langkah itu sebagai `learning_rate`.

Di scikit-learn nama kelasnya `GradientBoostingClassifier`.

**Batas analogi:** yang diperbaiki adalah sisa angka pada skor, bukan daftar nama golongan yang salah. Langkah dikecilkan agar pohon baru tidak menghapus pohon lama. Ini bukan peluang yang dirata-rata serentak seperti hutan acak. Terlalu banyak pohon, atau langkah yang terlalu besar, bisa menghafal kebetulan data latih. Itu overfitting. Notebook hanya mencetak tahap pertama dan tahap terakhir, jadi jangan menyimpulkan bahwa tiap langkah di antaranya selalu lebih baik.

## Coba sendiri dulu, baru kode

Tiga pemilah berkata: matang, mentah, matang.

Golongan mana yang menang?

Jawab dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

`sklearn.datasets.load_wine` membaca berkas yang sudah terpasang. Tidak ada unduhan. Bukan data asli perusahaan.

Isinya analisis kimia anggur dari daerah yang sama di Italia, tiga kelompok varietas. Nama golongannya `class_0`, `class_1`, dan `class_2`: tiga kelompok, bukan peringkat dari buruk ke baik. `feature_names` pada kode adalah nama kolom bawaan dataset, bukan istilah baru.

Satu pohon tanpa batas kedalaman, hutan acak, dan gradient boosting belajar hanya dari data latih. Yang dibandingkan adalah banyak tebakan salah di data uji, bukan angka nol di data latih. Baseline tetap golongan yang paling banyak di data latih.

Pada pecahan ini hutan acak salah nol kali di data uji. Aeberhard, Coomans, dan de Vel menulis bahwa kelompok-kelompoknya bisa dipisahkan, tetapi pada leave-one-out hanya satu metode mereka yang nol kesalahan. Leave-one-out artinya tiap baris sekali giliran dijadikan satu-satunya baris uji. Itu bukan istilah modul ini, dan notebook ini tidak melakukan uji itu. Nol pada 45 baris di notebook ini bukan janji untuk anggur lain.

## Kesalahan yang paling sering terjadi

1. Hutan acak dikira beberapa ahli dengan pengalaman yang berbeda. Pohon-pohonnya satu resep pada potongan data yang tumpang-tindih.
2. Salah data latih yang nol dipakai untuk memilih model. Keluaran: `salah_latih_pohon 0` tetapi `salah_uji_pohon 2`. Angka untuk anggur baru adalah yang di data uji.
3. Hutan acak disamakan dengan gradient boosting. Yang pertama merata-rata peluang banyak pohon. Yang kedua menambah pohon berurutan dengan langkah kecil.
4. `salah_uji_hutan 0` pada `baris_uji 45` dianggap bukti model tidak akan salah lagi.
5. `random_state` tidak diisi `SEED`, sehingga undian hutan berubah setiap dijalankan.
6. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

uv adalah perkakas yang memasang paket dan menjalankan Python sesuai berkas kunci di root repo. Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian acak, lewat `random_state=SEED`.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only. Versi paket terkunci di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan dua istilah baru modul ini, masing-masing dalam satu kalimat.
2. Tiga suara: matang, mentah, matang. Yang mana yang menang, dan berapa suaranya?
3. Pada baris uji pertama, berapa pohon yang memilih `class_0`? Apakah peluang rata-rata pada baris itu sama dengan bagian suara?
4. Berapa salah uji untuk satu pohon, hutan acak, dan gradient boosting? Mana yang paling sedikit pada pecahan ini?
5. Nol kesalahan hutan acak pada data uji ini berarti model tidak akan salah pada anggur lain. Benar atau salah?
6. Salah data latih satu pohon adalah nol. Apakah angka itu yang dipakai untuk anggur baru?
7. Apa beda cara hutan acak dan gradient boosting menggabungkan pohon?

### Kunci jawaban

1. **hutan acak:** banyak pohon keputusan; tiap pohon melihat cuplikan baris dan sebagian kolom, lalu golongan akhir adalah yang peluang rata-ratanya paling tinggi. **gradient boosting:** pohon ditambah berurutan; tiap pohon baru mengikuti arah yang memperkecil kesalahan skor, dan sumbangannya dikecilkan.
2. Matang, dua dari tiga. `terbanyak matang` dan `hitung {'matang': 2, 'mentah': 1}`.
3. `suara class_0 95` dari `jumlah_pohon 100`. `sama_pada_baris_ini True`.
4. `salah_uji_pohon 2`, `salah_uji_hutan 0`, `salah_uji_boosting 1`. `paling_sedikit_salah_uji hutan_acak`.
5. Salah. Nol itu hanya pecahan data uji ini.
6. Salah. `pakai_nol_latih_untuk_anggur_baru False`. Yang dipakai adalah salah di data uji.
7. Hutan acak merata-rata peluang banyak pohon yang dilatih bersama-sama. Gradient boosting menambah pohon satu per satu, dengan langkah yang dikecilkan `learning_rate`.

### Angka yang disalin dari keluaran notebook

Jawaban di atas disalin dari keluaran ini, bukan dihitung ulang di teks.

Dari `notebook.ipynb`:

```
suara ['matang', 'mentah', 'matang']
hitung {'matang': 2, 'mentah': 1}
terbanyak matang
baris 178
kolom_ukuran 13
class_0 59
class_1 71
class_2 48
baris_latih 133
baris_uji 45
baseline_selalu class_1
salah_uji_baseline 27
salah_latih_pohon 0
salah_uji_pohon 2
pohon_mengalahkan_baseline True
banyak_pohon 100
salah_latih_hutan 0
salah_uji_hutan 0
jumlah_pohon 100
suara class_0 95
suara class_1 2
suara class_2 3
golongan_benar class_0
peluang class_0 0.95
bagian_suara class_0 0.95
peluang class_1 0.02
bagian_suara class_1 0.02
peluang class_2 0.03
bagian_suara class_2 0.03
tebakan class_0
sama_pada_baris_ini True
learning_rate 0.1
banyak_tahap 100
salah_latih_boosting 0
salah_uji_boosting 1
salah_uji_tahap_pertama 14
salah_uji_tahap_terakhir 1
terakhir_lebih_sedikit True
paling_sedikit_salah_uji hutan_acak
```

Dari `latihan-kunci.ipynb`:

```
hitung {'matang': 2, 'mentah': 1}
terbanyak matang
baris_uji 45
salah_latih_pohon 0
salah_uji_pohon 2
salah_uji_hutan 0
salah_uji_boosting 1
pakai_nol_latih_untuk_anggur_baru False
paling_sedikit_salah_uji hutan_acak
```

## Sumber

- scikit-learn developers. *Ensembles* (halaman panduan untuk hutan acak dan gradient boosting). <https://scikit-learn.org/stable/modules/ensemble.html>
- scikit-learn developers. `RandomForestClassifier`. <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
- scikit-learn developers. `GradientBoostingClassifier`. <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html>
- scikit-learn developers. *Toy datasets* (Wine recognition dataset) dan `load_wine`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html>
- Forina, M., Leardi, R., Armanino, C., dan Lanteri, S. *PARVUS: An extendable package of programs for data exploration, classification and correlation.* Elsevier, Amsterdam, 1988. ISBN 0-444-43012-1. Ejaan judul mengikuti tinjauan Vandeginste, B. G. M., Journal of Chemometrics (1990), doi:10.1002/cem.1180040210. Berkas `wine.names` di UCI menulis "Extendible Package" tanpa "of Programs".
- UCI Machine Learning Repository. `wine.names` menyebut "three different cultivars". Halaman toy dataset scikit-learn menulis "cultivators" dan sempat menyebut R.A. Fisher sebagai creator. Fisher adalah penulis dataset iris, bukan pemilik data anggur. Modul ini mengikuti `wine.names`: tiga kelompok varietas.
- Aeberhard, S., Coomans, D., dan de Vel, O. "Comparison of Classifiers in High Dimensional Settings." Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of Mathematics and Statistics, James Cook University of North Queensland.
- Breiman, L. "Random Forests." Machine Learning 45, 5-32 (2001). doi:10.1023/A:1010933404324
- Friedman, J. H. "Greedy Function Approximation: A Gradient Boosting Machine." The Annals of Statistics 29(5), 1189-1232 (2001). doi:10.1214/aos/1013203451
