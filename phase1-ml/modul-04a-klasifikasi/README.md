# Modul 4a: Klasifikasi

**Tujuan belajar:** Membedakan tebakan golongan dari tebakan angka, lalu membandingkan regresi logistik dan pohon keputusan dengan baseline pada data uji.

**Tingkat:** intermediate

Bagian ini memakai tiga istilah baru. Dua model lain, hutan acak dan gradient boosting, ada di [modul 4b](../modul-04b-pohon-gabungan/) supaya tiap bagian tetap tidak lebih dari tiga istilah.

## Cerita pembuka

Kamu memilah mangga di meja dapur. Kemarin pertanyaannya "beratnya kira-kira berapa kilogram". Hari ini pertanyaannya berubah: masuk keranjang matang, atau keranjang yang masih mentah?

Itu bukan angka. Dua keranjang, dan tiap buah harus masuk salah satu. Modul ini belajar cara itu dengan dua spesies bunga iris yang mirip, dari berkas yang sudah terpasang bersama scikit-learn. Tidak ada unduhan. Bukan data asli perusahaan.

## Teori

Paket adalah bundel kode siap pakai. Pustaka adalah kumpulan fungsi di dalam paket. pandas adalah pustaka untuk tabel. scikit-learn adalah pustaka untuk model di modul ini.

Tiga istilah di bawah ini yang baru. Data latih dan data uji serta baseline dipakai sesuai arti di kamus, tidak diubah. Rata-rata selisih mutlak, istilah modul sebelumnya, mengukur jarak tebakan yang jawabannya angka. Di modul ini yang dibandingkan adalah banyak tebakan golongan yang salah. Overfitting juga dipakai sesuai kamus modul regresi: model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga bagus di data latih tetapi buruk di data baru.

Notebook mencetak banyak tebakan yang salah pada data latih dan pada data uji.

### klasifikasi

Memilah ke keranjang yang sudah bernama, bukan menimbang kilogram. Nama teknisnya **klasifikasi**: model yang menebak golongan, bukan angka.

**Batas analogi:** keranjang harus sudah ada di jawaban data latih. Model tidak membuat golongan baru. Kalau kenyataannya suatu spektrum, dua keranjang membuang yang di tengah. Salah keranjang bukan selisih kilogram, jadi rata-rata selisih mutlak untuk jawaban berupa angka tidak pindah begitu saja.

### regresi logistik

Bayangkan timbangan yang mengubah bukti menjadi peluang antara 0 dan 1. Peluang 0.7 pada satu keranjang belum nama keranjang. Ambang, yaitu batas peluang yang kita pilih, yang memutuskan. Pada dua golongan di modul ini, peluang virginica yang lebih besar dari 0.5 masuk virginica; selain itu masuk versicolor.

Nama teknisnya **regresi logistik**: model klasifikasi yang mengubah jumlah berbobot dari kolom menjadi peluang, lalu memilih golongan dengan peluang terbesar.

Gambar kecil, sebelum rumus. Dua peluang tangan:

```
0.7  lebih besar dari 0.5  -> virginica
0.4  tidak                 -> versicolor
```

**Batas analogi:** peluang itu pemetaan skor model, bukan janji bahwa di dunia nyata kamu benar tujuh dari sepuluh kali. Skornya jumlah berbobot, jadi batasnya lurus pada skor itu, bukan sembarang lengkung. Saat peluang tepat 0.5, kedua golongan seri dan scikit-learn memilih nama yang lebih dulu di daftar `classes_`. Secara bawaan bobot kolom ditahan agar tidak terlalu besar; tombol itu bukan istilah modul ini. Ini bukan model yang menebak kilogram.

### pohon keputusan

Seperti bagan sortir: jika lebar mahkota melewati satu batas, taruh di keranjang ini; jika tidak, tanya satu kolom lain. Nama teknisnya **pohon keputusan**: model klasifikasi yang memilah baris dengan pertanyaan ya atau tidak beruntun. Setiap pertanyaan memakai satu kolom dan satu batas.

**Batas analogi:** pohon hanya memisahkan baris data latih yang ia lihat. Ia tidak memahami arti kata. Pohon yang terlalu dalam bisa cocok pada kebetulan satu baris. Itu overfitting. Pertanyaan satu kolom sekali, jadi batas miring butuh banyak langkah. Mengubah satu baris latih di dekat batas bisa mengubah pertanyaannya. Angka batas yang tercetak di notebook adalah hasil data itu, bukan hukum untuk semua bunga.

## Coba sendiri dulu, baru kode

Ambang 0.5.

1. Peluang virginica 0.7 masuk golongan mana?
2. Peluang virginica 0.4 masuk golongan mana?

Jawab dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

`sklearn.datasets.load_iris` membaca berkas yang sudah terpasang. Tidak ada unduhan. Bukan data asli perusahaan.

`sepal` artinya kelopak pelindung, `petal` artinya mahkota, keduanya dalam sentimeter. Spesies setosa mudah terpisah, jadi notebook menyisihkannya dan memakai versicolor serta virginica. Empat kolom ukuran ikut semua. `feature_names` pada kode adalah nama kolom bawaan dataset, bukan istilah baru.

Data latih dipakai model untuk belajar. Data uji disisihkan dan tidak dilihat saat belajar. Baseline selalu menebak golongan yang paling banyak di data latih. Regresi logistik dan pohon pendek (`max_depth=2`, batas dua pertanyaan) dibandingkan dengan baseline lewat banyak tebakan yang salah di data uji. Pohon tanpa batas kedalaman menunjukkan overfitting: salah di data latih bisa nol, tetapi data ujinya lebih buruk daripada pohon pendek.

Pada teks pohon, kata `class` berarti golongan daun itu.

## Kesalahan yang paling sering terjadi

1. Model belajar dan dinilai pada baris yang sama, sehingga skor terlihat terlalu bagus. Nilai yang dipakai adalah salah di data uji.
2. Peluang dianggap sudah nama keranjang. Masih ada ambang.
3. Pohon tanpa batas kedalaman dihafal sampai salah data latih nol, lalu angka nol itu yang dibanggakan. Keluaran notebook: `salah_latih_pohon_dalam 0` dan `salah_uji_pohon_dalam 4`, lebih buruk di data uji daripada pohon pendek (`salah_uji_pohon 3`).
4. Batas pertanyaan pohon, misalnya lebar mahkota 1.75, dianggap hukum untuk semua bunga. Angka itu hasil data latih ini.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

uv adalah perkakas yang memasang paket dan menjalankan Python sesuai berkas kunci di root repo. Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian acak, lewat `random_state=SEED`, supaya pecahan data dan pohon yang terundi berulang. Pada regresi logistik, solver bawaan tidak memakai angka itu; sel tetap menulis `random_state=SEED`.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only. Versi paket terkunci di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat.
2. Peluang virginica 0.7 dengan ambang 0.5 masuk golongan apa? Peluang 0.4?
3. Mengapa tebakan dinilai di data uji?
4. Berapa tebakan salah baseline dan regresi logistik pada data uji? Mana yang lebih kecil?
5. Pohon tanpa batas kedalaman: berapa salah di data latih, berapa di data uji? Gejala bagus di latih dan lebih buruk di uji itu istilah apa, sesuai kamus?
6. "Batas 1.75 pada pohon berlaku untuk semua bunga." Benar atau salah?
7. Dataset diunduh saat notebook dijalankan. Benar atau salah?

### Kunci jawaban

1. **klasifikasi:** model yang menebak golongan, bukan angka. **regresi logistik:** model klasifikasi yang mengubah jumlah berbobot dari kolom menjadi peluang, lalu memilih golongan dengan peluang terbesar. **pohon keputusan:** model klasifikasi yang memilah baris dengan pertanyaan ya atau tidak beruntun; setiap pertanyaan memakai satu kolom dan satu batas.
2. 0.7 masuk virginica. 0.4 masuk versicolor. Disalin dari keluaran di bawah.
3. Data uji tidak dilihat model saat belajar, jadi angka itu mengukur tebakan pada baris yang disisihkan.
4. `salah_uji_baseline 13` dan `salah_uji_logistik 2`. Logistik lebih kecil. `logistik_mengalahkan_baseline True`.
5. `salah_latih_pohon_dalam 0` dan `salah_uji_pohon_dalam 4`. Gejalanya overfitting.
6. Salah. Batas itu hasil data latih pada notebook, bukan hukum untuk semua bunga.
7. Salah. Berkas iris sudah ikut terpasang bersama scikit-learn.

### Angka yang disalin dari keluaran notebook

Jawaban di atas disalin dari keluaran ini, bukan dihitung ulang di teks.

Dari `notebook.ipynb`:

```
peluang 0.7 golongan virginica
peluang 0.4 golongan versicolor
baris 100
kolom 5
versicolor 50
virginica 50
baris_latih 75
baris_uji 25
baseline_selalu virginica
salah_latih_baseline 37
salah_uji_baseline 13
peluang versicolor 0.013309226417507314
peluang virginica 0.9866907735824927
peluang_virginica 0.9866907735824927
di_atas_ambang True
tebakan virginica
salah_latih_logistik 4
salah_uji_logistik 2
logistik_mengalahkan_baseline True
|--- petal width (cm) <= 1.75
|   |--- petal length (cm) <= 5.05
|   |   |--- class: versicolor
|   |--- petal length (cm) >  5.05
|   |   |--- class: virginica
|--- petal width (cm) >  1.75
|   |--- class: virginica
salah_latih_pohon 1
salah_uji_pohon 3
pohon_mengalahkan_baseline True
salah_latih_pohon_dalam 0
salah_uji_pohon_dalam 4
latih_nol True
uji_lebih_buruk_dari_pohon_pendek True
```

Dari `latihan-kunci.ipynb`:

```
peluang 0.7 golongan virginica
peluang 0.4 golongan versicolor
baris_latih 75
baris_uji 25
salah_uji_baseline 13
salah_uji_logistik 2
salah_latih_pohon 1
salah_uji_pohon 3
salah_latih_pohon_dalam 0
salah_uji_pohon_dalam 4
latih_nol True
uji_lebih_buruk_dari_pohon_pendek True
hukum_alam False
```

## Sumber

- scikit-learn developers. *Logistic regression.* <https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression>
- scikit-learn developers. `LogisticRegression`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>
- scikit-learn developers. *Decision Trees.* <https://scikit-learn.org/stable/modules/tree.html>
- scikit-learn developers. `DummyClassifier`. <https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html>
- scikit-learn developers. *Toy datasets* (Iris plants dataset) dan `load_iris`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html>
- Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annals of Eugenics, 7, Part II, 179-188 (1936); juga dalam "Contributions to Mathematical Statistics" (John Wiley, NY, 1950). Nama jurnal mengikuti halaman Wiley dan catatan modul persiapan: halaman toy dataset scikit-learn sempat menulis "Annual Eugenics".
