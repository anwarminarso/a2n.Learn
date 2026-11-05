# Modul 3: Regresi

**Tujuan belajar:** Menyusun tebakan angka dengan garis lurus, membaca fungsi kerugian pada data latih, memakai baseline dan rata-rata selisih mutlak sebagai pembanding, dan mengenali overfitting.

**Tingkat:** beginner

Modul ini menutup tingkat beginner. Ujian tingkat ada di bagian akhir, dengan kunci dan kriteria lulus.

## Cerita pembuka

Kamu naik angkot. Tiga perjalanan catatannya terbuka:

```
jarak km    1     2     3
menit       4     6     9
```

Kamu coba satu garis: menit = 2 + 2 × jarak. Hasilnya 4, 6, dan 8. Perjalanan ketiga meleset satu menit. Satu perjalanan lain, 4 km dan 12 menit, kamu simpan di amplop. Amplop tidak dipakai untuk memilih garis.

Di modul 2, tebakan paling sederhana tidak membaca petunjuk. Garis di modul ini membaca jarak. Angka pada cerita ini contoh kecil untuk dihitung tangan. Modul ini tidak memakai data asli perusahaan.

## Teori

Di modul ini hanya ada tiga istilah baru. Pustaka adalah kumpulan fungsi siap pakai. scikit-learn adalah pustaka yang sudah dipakai di modul 1 dan 2. Nama fungsi di pustaka bukan istilah baru. Kata model di kamus tetap bahasa biasa untuk cara menebak, sama seperti di modul 2, dan belum masuk kamus. Baseline dan rata-rata selisih mutlak dipakai lagi dengan arti yang sama seperti di modul 2.

### regresi linear

Gambar dulu. Garis yang dicoba pada tiga catatan terbuka:

```
jarak km      1     2     3
menit         4     6     9
garis coba    4     6     8
```

Ada bayaran awal, lalu tambahan yang mengikuti jarak. Nama teknisnya **regresi linear**. Artinya: Cara menyusun tebakan angka berupa garis lurus dari data latih: satu angka awal, ditambah satu angka pengali untuk tiap petunjuk. Garis itu membaca petunjuk.

Perumpamaan: seperti ongkos angkot: ada bayaran awal, lalu tambahannya mengikuti jarak.

**Batas analogi:** gambar ongkos itu satu petunjuk, yaitu jarak, jadi bisa digambar sebagai satu garis di kertas. Bila petunjuk lebih dari satu, tetap satu angka awal ditambah satu angka pengali per petunjuk, tetapi bukan garis di satu kertas. Garis ini tidak melengkung. Ini bukan baseline: baseline selalu menebak rata-rata data latih dan tidak membaca petunjuk. Angka awal adalah tebakan saat semua petunjuk bernilai nol. Pada kolom yang sudah digeser pembuat dataset, nol itu bukan nol kilometer atau nol kilogram.

Garis pada gambar kita pilih dengan tangan. Pustaka nanti mencari garis lain, dengan angka awal dan angka pengali yang membuat fungsi kerugian lebih kecil. Notebook mencetak kedua garis itu.

### fungsi kerugian

Gambar dulu, masih dengan garis coba:

```
menit        4     6     9
garis coba   4     6     8
selisih      0     0     1
kuadrat      0     0     1
```

Kuadrat artinya selisih dikali dirinya sendiri. Selisih 1 menjadi 1. Selisih 2 menjadi 4. Dua selisih 1 punya jumlah kuadrat 2, lebih kecil daripada satu selisih 2.

Rumus pada gambar di atas:

`fungsi kerugian garis coba = (0 + 0 + 1) / 3`

Nama teknisnya **fungsi kerugian**. Artinya: Angka pada data latih yang dibuat sekecil mungkin saat garis disusun. Pada regresi linear di modul ini, angka itu adalah rata-rata dari selisih yang dikuadratkan: tiap selisih dikali dirinya sendiri, lalu dirata-rata. Makin kecil, makin dekat garis ke jawaban data latih yang dipakai menyusunnya.

Dalam bahasa Inggris, angka ini sering disebut loss. Sebutan itu bukan istilah kedua.

Perumpamaan: seperti mencatat menit yang meleset, mengkuadratkan menit itu, lalu merata-ratakannya. Meleset dua menit dihitung empat, jadi satu meleset besar lebih berat daripada dua meleset kecil yang jumlah jaraknya sama.

**Batas analogi:** lebih berat hanya gambar. Yang dihitung adalah kuadrat, bukan perasaan penumpang. Ini bukan rata-rata selisih mutlak. Rata-rata selisih mutlak membuang tanda minus dan tidak mengkuadratkan; modul ini tetap memakainya untuk membandingkan garis dengan baseline pada data uji. Dokumentasi scikit-learn memperkecil jumlah kuadrat selisih. Selama banyak baris data latih tidak berubah, garis yang memperkecil jumlah itu sama dengan garis yang memperkecil rata-ratanya. Angka ini dihitung pada data latih dan bukan nilai pada data uji. Nol berarti tebakan sama dengan jawaban pada baris data latih, dan nol itu belum menilai data baru.

Rata-rata selisih mutlak pada amplop tetap pembanding dengan baseline, sama seperti modul 2. Fungsi kerugian tidak menggantikan pembanding itu.

### overfitting

Gambar dulu. Titik-titik hampir sejajar, satu titik melonjak:

```
menit
  9 |           *
  6 |        *
  4 |     *
  2 |  *
    +-------------- jarak
```

Garis lurus meleset sedikit pada titik yang melonjak. Garis yang dipelintir bisa menempel di setiap titik, termasuk lonjakan yang kebetulan, lalu meleset jauh pada catatan di amplop. Nama teknisnya **overfitting**. Artinya: Model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru.

Di modul 2 pola ini hanya disebut "model menghafal". Nama overfitting baru dipakai di modul ini.

Perumpamaan: seperti garis yang dipelintir sampai menempel di setiap titik catatan yang terbuka, termasuk satu titik yang kebetulan meleset, lalu meleset jauh pada catatan di amplop.

**Batas analogi:** gambar garis yang dipelintir adalah untuk satu petunjuk. Modul ini tidak memasang garis yang dipelintir itu. Angka pada notebook memakai garis lurus dengan banyak petunjuk, yang bisa menempel di setiap baris data latih karena petunjuknya lebih banyak daripada baris latih. Menempel di data latih bukan nilai pada data uji. Gambar ini tidak mengatakan setiap garis lurus menghafal. Garis dengan satu petunjuk pada kasus diabetes dibanding baseline memakai rata-rata selisih mutlak pada data uji. Menyalin jawaban data latih sampai jaraknya nol adalah contoh menghafal dari modul 2; nama overfitting baru dipakai di sini, dan nol itu tetap bukan nilai pada data uji.

## Coba sendiri dulu, baru kode

Pakai gambar garis coba di atas. Hitung dengan tangan, lalu cocokkan dengan gambar itu.

1. Apakah tebakan pada jarak 1, 2, dan 3 sama dengan 4, 6, dan 8?
2. Berapa hasil `(0 + 0 + 1) / 3`?
3. Berapa rata-rata 4, 6, dan 9?
4. Amplop: jarak 4 km, menit 12. Tebakan garis coba adalah 10. Berapa jaraknya terhadap 12?

Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

Kita membaca dataset diabetes lewat `sklearn.datasets.load_diabetes`. Dokumentasi scikit-learn menyatakan dataset mainan ini tidak perlu diunduh dari situs lain: berkasnya sudah ikut terpasang. Modul ini tidak memakai data asli perusahaan.

Ada 442 baris. Notebook hanya memakai satu petunjuk, kolom `bmi`, dan satu jawaban, kolom `target`, supaya garisnya tetap satu garis di kertas. `bmi` pada dokumentasi adalah ukuran tubuh. Kolom itu sudah dipusatkan dan diskalakan pembuat dataset, sampai jumlah kuadrat isi kolom itu 1. Bukan kilogram yang kamu timbang di rumah. `target` adalah ukuran seberapa jauh penyakit berkembang, satu tahun setelah pengukuran awal. Halaman dokumentasinya tidak menyebut satuan jawaban. Modul ini tidak mengarang satuan. Karena kolom `bmi` sudah diskalakan, angka pengali yang tercetak bisa besar. Itu bukan "satu langkah timbangan menambah ratusan penyakit".

Seperempat baris menjadi data uji, lewat `train_test_split` dengan `test_size=0.25` dan `random_state=SEED`. Sama seperti pilihan di modul 2.

Baseline memakai `DummyRegressor(strategy="mean")`. Tebakannya tidak berubah mengikuti `bmi`. Semua tebakan sama dengan rata-rata kolom `target` pada data latih.

Garis regresi linear disusun hanya dari data latih. Pembandingnya rata-rata selisih mutlak pada data uji. Pada keluaran notebook, jarak garis di data uji lebih kecil daripada jarak baseline. Itu yang dipakai untuk bilang garis mengalahkan baseline.

Pada keluaran yang sama, rata-rata selisih mutlak garis di data latih sedikit lebih besar daripada di data uji. Itu boleh terjadi pada kumpulan baris ini. Angka yang kecil di data latih tidak otomatis angka yang kecil di data uji.

Bagian overfitting memakai `make_regression`: pembuat angka di komputer, bukan unduhan. Ada 24 baris dan 20 petunjuk. Hanya satu petunjuk yang benar-benar dipakai membuat jawaban. Petunjuk lain kebetulan. `noise`: gangguan acak pada jawaban (derau). Geseran tetap adalah parameter `bias`. Petunjuk lebih banyak daripada baris data latih, jadi garis lurus bisa menempel di data latih. Jarak pada data uji lebih buruk daripada baseline. Garis satu petunjuk pada diabetes tidak diperlakukan seperti itu.

Indeks adalah nomor baris pada tabel, mulai dari 0.

## Kesalahan yang paling sering terjadi

1. Menilai garis dari fungsi kerugian di data latih, apalagi kalau angkanya nol atau sangat kecil. Pembanding dengan baseline adalah rata-rata selisih mutlak pada data uji.
2. Mengira fungsi kerugian sama dengan rata-rata selisih mutlak. Yang satu mengkuadratkan selisih pada data latih. Yang satu mengukur jarak tanpa kuadrat.
3. Memasukkan baris data uji saat garis atau baseline disusun. Amplop yang ikut mengubah garis berhenti menjadi penilaian yang jujur.
4. Mengira tebakan baseline mengikuti petunjuk. Pada strategi rata-rata, semua tebakan sama.
5. Mengira setiap garis lurus menghafal. Garis satu petunjuk pada kasus diabetes tidak menempel di setiap baris. Gambar garis yang dipelintir tidak dipasang di modul ini.
6. Angka di laporan ditulis dari ingatan, atau pemisahan dijalankan tanpa `random_state=SEED`, sehingga baris data uji berganti setiap kali notebook diulang.

## Cara menjalankan

Paket adalah perkakas yang dipasang ke venv. Semua modul memakai satu venv di root repo, dibuat dengan `uv sync --frozen` dari root. Kamus menjelaskan venv sebagai lingkungan satu proyek. uv adalah alat yang membaca `uv.lock` di root repo dan memasang paket itu. Pustaka scikit-learn adalah salah satu paket tersebut.

Sel pertama setiap notebook berisi `SEED = 42`, seperti di modul 1. Angka tetap itu dipakai pada setiap pemisahan acak dan pada pembuat angka, lewat `random_state=SEED`.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul ini:

```bash
uv sync --frozen
uv run pytest
uv run pytest --nbmake
```

Buka `notebook.ipynb` di folder modul ini, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Ujian tingkat ada di `ujian.ipynb`, kuncinya di `ujian-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only. Versi paket terkunci di `uv.lock` di root repo. Jalan yang dipakai modul ini adalah uv.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Fungsi kerugian sama dengan rata-rata selisih mutlak. Benar atau salah?
3. Mengapa selisih 2 dihitung lebih berat daripada dua selisih 1 pada fungsi kerugian?
4. "Baseline pada kasus diabetes mengikuti kolom bmi, jadi tebakannya berbeda-beda." Benar atau salah?
5. `kasus_mae_latih_hafal` nol. Apakah angka nol itu penilaian pada data uji?
6. Dataset diabetes diunduh dari internet saat notebook dijalankan. Benar atau salah?
7. Berapa baris data latih dan data uji pada kasus diabetes, dan apakah garis mengalahkan baseline pada data uji?
8. Pada angka buatan dengan banyak petunjuk, apakah jarak di data uji lebih buruk daripada baseline?

### Kunci jawaban

1. **regresi linear:** cara menyusun tebakan angka berupa garis lurus dari data latih: satu angka awal, ditambah satu angka pengali untuk tiap petunjuk. Garis itu membaca petunjuk. **fungsi kerugian:** angka pada data latih yang dibuat sekecil mungkin saat garis disusun. Pada regresi linear di modul ini, angka itu adalah rata-rata dari selisih yang dikuadratkan. **overfitting:** model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru.
2. Salah. Fungsi kerugian mengkuadratkan selisih pada data latih. Rata-rata selisih mutlak tidak mengkuadratkan, dan pembanding dengan baseline memakai angka pada data uji.
3. Karena selisih dikali dirinya sendiri. Selisih 2 menjadi 4. Dua selisih 1 menjadi 1 + 1 = 2.
4. Salah. `kasus_baseline` adalah rata-rata jawaban data latih. Tebakan baseline tidak mengikuti `bmi`.
5. Bukan. Nol itu jarak pada data latih karena jawaban disalin. Penilaian memakai angka pada data uji.
6. Salah. Dataset diabetes sudah ikut terpasang bersama scikit-learn; notebook tidak mengunduhnya.
7. `kasus_baris_latih 331` dan `kasus_baris_uji 111`. `kasus_garis_mengalahkan_baseline True`, disalin dari keluaran di bawah.
8. Ya. `lentur_uji_lebih_buruk True`, disalin dari keluaran di bawah. `lentur_mae_latih` sangat kecil, tetapi bukan angka nol yang dicetak sebagai `0.0`. Angka `0.0` pada modul ini adalah `kasus_mae_latih_hafal`, yaitu salinan jawaban data latih.

Jawaban "coba sendiri": `tangan_tebakan [4.0, 6.0, 8.0]`, `tangan_fungsi_kerugian 0.3333333333333333`, `tangan_baseline 6.333333333333333`, dan `tangan_mae_garis_coba 2.0`. Angka panjang disalin apa adanya dari keluaran, bukan dibulatkan dengan tangan.

### Angka yang disalin dari keluaran notebook

Jawaban di atas dan angka di bawah ini disalin dari keluaran notebook yang sudah dijalankan, bukan dihitung ulang di teks.

Dari `notebook.ipynb`:

```
tangan_tebakan [4.0, 6.0, 8.0]
tangan_kuadrat [0.0, 0.0, 1.0]
tangan_fungsi_kerugian 0.3333333333333333
tangan_baseline 6.333333333333333
tangan_mae_garis_coba 2.0
tangan_mae_baseline 5.666666666666667
tangan_coba_lebih_dekat True
tangan_awal 1.3333333333333348
tangan_pengali 2.499999999999999
tangan_fungsi_kerugian_pas 0.05555555555555556
tangan_pas_lebih_kecil True
tangan_mae_pas 0.6666666666666679
tangan_pas_mengalahkan_baseline True
kasus_baris 442
kasus_kolom 2
kasus_baris_latih 331
kasus_baris_uji 111
kasus_baseline 154.34441087613294
kasus_awal 152.07653296894014
kasus_pengali 975.2769831271274
kasus_mae_uji_baseline 65.52742168150024
kasus_mae_uji_garis 49.80505217504619
kasus_garis_mengalahkan_baseline True
kasus_mae_latih_garis 52.28773945157054
kasus_mae_latih_hafal 0.0
lentur_petunjuk 20
lentur_baris_latih 18
lentur_mae_latih 4.717214273518443e-14
lentur_mae_uji 85.73737383461155
lentur_mae_uji_baseline 39.33668638735008
lentur_latih_lebih_kecil True
lentur_uji_lebih_buruk True
kasus_indeks_pertama 287
kasus_indeks_pertama_lagi 287
kasus_sama True
```

Dari `latihan.ipynb`: notebook latihan tidak menyimpan keluaran. Jawaban latihan ada di `latihan-kunci.ipynb`.

Dari `latihan-kunci.ipynb`:

```
kunci_fungsi_kerugian 0.3333333333333333
kunci_baseline 5.333333333333333
kunci_mae_garis 3.0
kunci_mae_baseline 4.666666666666667
kunci_garis_lebih_dekat True
kunci_baris_latih 331
kunci_baris_uji 111
kunci_baseline_bp 154.34441087613294
kunci_mae_uji_baseline 65.52742168150024
kunci_mae_uji_garis 57.483640272772284
kunci_garis_mengalahkan True
```

`kunci_baseline_bp` sama dengan `kasus_baseline`, dan `kunci_mae_uji_baseline` sama dengan `kasus_mae_uji_baseline`, karena baseline tidak membaca petunjuk dan pemisahan barisnya sama: dataset yang sama, `test_size=0.25`, dan `random_state=SEED`. Jarak garis berbeda karena latihan membaca kolom `bp`, sedangkan notebook membaca kolom `bmi`.

## Ujian tingkat beginner

Modul 3 menutup tingkat beginner. Ujian ini proyek mini plus pertanyaan. Ursa menjalankannya sebagai bagian dari uji modul. Squal mengaudit tulisannya. Bagian ini tidak menambah istilah baru.

Berkasnya: `ujian.ipynb` untuk dikerjakan, `ujian-kunci.ipynb` untuk kunci yang dijalankan. Keduanya memakai `SEED` di sel pertama.

### Proyek mini

Angka dibuat dengan `make_regression`: 80 baris, satu petunjuk, `noise` 15: gangguan acak pada jawaban (derau), `random_state=SEED`. Bukan unduhan. Bukan data asli perusahaan. Seperempat baris menjadi data uji dengan `test_size=0.25` dan `random_state=SEED`. Baseline adalah rata-rata jawaban data latih. Garis regresi linear disusun hanya dari data latih. Pembandingnya rata-rata selisih mutlak pada data uji.

### Pertanyaan

1. Dengan kata-katamu sendiri: mengapa garis diuji pada data yang tidak dipakai saat garis disusun?
2. "Fungsi kerugian yang kecil pada data latih sudah membuktikan garis baik pada data baru." Benar atau salah?
3. "Baseline membaca petunjuk, jadi tebakannya berubah-ubah." Benar atau salah?
4. Berapa baris data latih dan data uji pada proyek mini? Apakah garis mengalahkan baseline pada data uji?

### Kriteria lulus

Lulus bila semua butir ini terpenuhi sekaligus.

- Pemisahan memakai `test_size=0.25` dan `random_state=SEED`. Data uji tidak ikut menyusun garis maupun baseline.
- Soal 1 lulus bila jawaban memuat kedua gagasan pada kunci, dengan kata apa pun. Tes otomatis tidak menilai kata-kata bebas. Ursa membaca butir ini.
- `ujian-kunci.ipynb` memeriksa proyek mini, dan tes modul menghitung ulang syarat yang sama.

Tidak lulus bila data uji ikut menyusun garis.

### Kunci ujian

- Proyek mini: `ujian_lulus True`. Artinya rata-rata selisih mutlak garis pada data uji lebih kecil daripada baseline.
- Soal 2 salah. Soal 3 salah.
- Soal 1 lulus bila jawaban memuat kedua gagasan ini, dengan kata apa pun: data uji tidak ikut menyusun garis maupun baseline; angka pada data latih, termasuk yang sangat kecil karena garis menempel, tidak mengukur data baru.
- Soal 4 sama dengan angka yang disalin di bawah: 60 baris latih, 20 baris uji, dan garis mengalahkan baseline.

Tidak lulus bila garis tidak mengalahkan baseline pada data uji, atau bila soal 2 atau 3 dijawab benar.

1. Dua gagasan pada butir soal 1 di atas. Contoh yang memenuhi: garis dan baseline disusun hanya dari data latih; data uji disisihkan supaya kita melihat melesetnya pada data yang belum dipakai. Angka yang bagus pada data latih, termasuk nol karena menyalin jawaban, tidak memberi tahu hasil pada data baru.
2. Salah. Fungsi kerugian dihitung pada data latih. Pada bagian overfitting, jarak data latih sangat kecil, tetapi jarak data uji lebih buruk daripada baseline.
3. Salah. Baseline selalu menebak rata-rata jawaban data latih. Semua tebakan baseline sama.
4. `ujian_baris_latih 60`, `ujian_baris_uji 20`, dan `ujian_lulus True`.

### Angka yang disalin dari keluaran ujian

Dari `ujian-kunci.ipynb`. `ujian.ipynb` tidak menyimpan keluaran.

```
ujian_baris_latih 60
ujian_baris_uji 20
ujian_mae_baseline 66.88133498136851
ujian_mae_garis 12.230903600589109
ujian_lulus True
```

## Sumber

- scikit-learn developers. `LinearRegression`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html> Kalimat pada dokumentasi terpasang: "LinearRegression fits a linear model with coefficients w = (w1, ..., wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation."
- scikit-learn developers. `make_regression`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html> Kalimat pada dokumentasi terpasang: "Generate a random regression problem."
- scikit-learn developers. *Toy datasets* (Diabetes) dan `load_diabetes`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html> Halaman toy dataset menyatakan dataset ini tidak perlu mengunduh berkas dari situs lain. Kalimat pada halaman itu tentang kolom: tiap kolom petunjuk sudah dipusatkan dan diskalakan sehingga jumlah kuadrat tiap kolom menjadi 1.
- Efron, Bradley, Trevor Hastie, Iain Johnstone, and Robert Tibshirani. "Least Angle Regression." *The Annals of Statistics* 32, no. 2 (2004): 407–499. Halaman toy dataset scikit-learn menulis "Annals of Statistics" tanpa "The" dan tanpa nomor volume. Nama jurnal di sini mengikuti nama resminya, *The Annals of Statistics*, volume 32, nomor 2, termasuk discussion sampai halaman 499.
- scikit-learn developers. `train_test_split`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html> Kalimat pada halaman itu: "Split arrays or matrices into random train and test subsets." Halaman yang sama: bila `train_size` juga `None`, `test_size` menjadi 0.25.
- scikit-learn developers. `DummyRegressor`. <https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html> Kalimat pada halaman itu untuk strategi `"mean"`: "always predicts the mean of the training set". Kalimat pada halaman yang sama: "Do not use it for real problems."
- scikit-learn developers. `mean_absolute_error`. <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html> Kalimat pada halaman itu: "The mean absolute error is a non-negative floating point value, where best value is 0.0."
