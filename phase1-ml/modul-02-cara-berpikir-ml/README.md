# Modul 2: Cara berpikir ML

**Tujuan belajar:** Menetapkan apa yang ditebak, memisahkan data latih dan data uji, memakai baseline sebagai pembanding, dan membaca rata-rata selisih mutlak.

**Tingkat:** beginner

## Cerita pembuka

Kamu tiga kali berjalan ke warung. Catatan menitnya: 8, 10, dan 12. Satu perjalanan lain, 16 menit, kamu masukkan ke amplop tertutup. Tebakan "biasanya 10 menit" disusun hanya dari tiga catatan yang terbuka. Amplop baru dibuka saat kamu mengukur seberapa jauh tebakan itu meleset.

Yang ditebak pada cerita ini: lama perjalanan, dalam menit. Pada kasus nanti ada satu kolom petunjuk, tetapi tebakan paling sederhana tidak membaca petunjuk itu. Yang dipakai untuk menilai: jarak tebakan pada catatan yang disisihkan.

Modul ini tidak memakai data asli perusahaan. Angka 8, 10, 12, dan 16 adalah contoh kecil untuk dihitung tangan.

## Teori

Pustaka adalah kumpulan fungsi siap pakai yang dipanggil dari kode. Di modul ini hanya ada tiga istilah baru. Kata model dipakai sebagai bahasa biasa untuk cara menebak, dan belum masuk kamus.

### data latih dan data uji

Tiga catatan terbuka dipakai untuk menyusun tebakan. Catatan di amplop disisihkan, tidak ikut menyusun tebakan, dan baru dipakai saat mengukur. Nama teknisnya **data latih dan data uji**. Artinya: data dibagi dua: data latih dipakai model untuk belajar; data uji disisihkan dan tidak dilihat model saat belajar, dipakai untuk mengukur seberapa baik model pada data baru. Satu entri karena satu ide.

Perumpamaan: seperti catatan perjalanan yang terbuka untuk menyusun tebakan, dan satu catatan di amplop tertutup yang baru dibuka saat mengukur melesetnya tebakan.

**Batas analogi:** amplop pada gambar tidak memilih catatan secara acak; notebook memisahkan baris lewat `random_state=SEED`. Pada cerita amplopnya satu catatan, data uji pada kasus berisi beberapa baris. Kalau amplop dibuka lalu rata-ratanya diubah, catatan itu berhenti menjadi penilaian yang jujur.

### baseline

Gambar dulu. Tiga jawaban yang terbuka:

```
8    10    12
```

Tebakan untuk setiap baris, termasuk baris di amplop, adalah rata-rata tiga angka itu. Tebakan ini tidak melihat jarak. Nama teknisnya **baseline**. Artinya: cara menebak paling sederhana (misalnya selalu menebak rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; model yang baik harus mengalahkannya.

Di modul ini jawabannya angka, jadi baseline selalu menebak rata-rata data latih. Contoh kelas yang paling banyak ada di kamus dan tidak dihitung di sini.

Perumpamaan: seperti menjawab "biasanya sekitar sepuluh menit" pada setiap perjalanan, tanpa melihat jaraknya.

**Batas analogi:** "sepuluh menit" hanya angka pada cerita. Angka di notebook adalah rata-rata jawaban data latih. Tebakan ini tidak membaca petunjuk, dan gambar rata-rata berhenti bila jawabannya bukan angka. Mengalahkan baseline berarti rata-rata selisih mutlak pada data uji lebih kecil.

### rata-rata selisih mutlak

Gambar dulu, dengan tebakan 10 pada data latih:

```
jawaban latih      8    10    12
tebakan           10    10    10
selisih bertanda  -2     0    +2
jarak              2     0     2
```

Data uji: jawaban 16, tebakan 10, jarak 6.

Jarak adalah selisih yang tanda minusnya dibuang.

Rumus pada gambar di atas:

`rata-rata selisih mutlak pada data latih = (2 + 0 + 2) / 3`

`rata-rata selisih bertanda = (-2 + 0 + 2) / 3`

Rata-rata selisih bertanda pada gambar itu nol, padahal ada jarak. Karena itu modul ini memakai jarak, lalu merata-ratakannya. Nama teknisnya **rata-rata selisih mutlak**. Artinya: rata-rata dari jarak antara tebakan dan jawaban. Jarak berarti selisih yang tanda minusnya dibuang. Jumlah jarak dibagi banyak baris yang diukur. Semakin kecil angkanya, semakin dekat. Nilai terbaik adalah nol: tebakan sama dengan jawaban pada baris yang diukur. Di scikit-learn, fungsi untuk hitungan yang sama bernama mean_absolute_error.

Perumpamaan: seperti mencatat berapa menit tebakan meleset, baik terlalu singkat maupun terlalu lama, lalu merata-rata menit meleset itu.

**Batas analogi:** pada kasus yang dirata-rata adalah jarak ke kolom `Weight`, bukan menit ke warung. Gambar ini tidak mengkuadratkan selisih. Nol pada data latih, termasuk bila model menghafal, tidak menilai data uji.

`mean_absolute_error` adalah nama fungsinya, bukan istilah kedua. Menyalin jawaban data latih membuat jarak pada data latih menjadi nol. Angka nol itu tidak mengukur data uji.

## Coba sendiri dulu, baru kode

Pakai gambar di atas. Hitung dengan tangan, lalu cocokkan dengan gambar itu.

1. Apakah rata-rata 8, 10, dan 12 sama dengan tebakan pada gambar?
2. Kalau tebakan pada data uji juga angka itu, berapa jaraknya terhadap 16?
3. Berapa hasil `(2 + 0 + 2) / 3`?
4. Berapa hasil `(-2 + 0 + 2) / 3`?

Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

Kita membaca dataset Linnerud lewat `sklearn.datasets.load_linnerud`. Dokumentasi scikit-learn menyatakan dataset mainan ini tidak perlu diunduh dari situs lain: berkasnya sudah ikut terpasang. Modul ini tidak memakai data asli perusahaan.

Dua puluh orang di klub kebugaran. Ada angka gerakan dan angka tubuh. Notebook hanya memakai satu petunjuk, kolom `Situps`, dan satu jawaban, kolom `Weight`, supaya rata-rata selisih mutlak tetap satu angka. Halaman dokumentasinya tidak menyebut satuan `Weight`. Modul ini tidak mengarang satuan.

Seperempat baris menjadi data uji, lewat `train_test_split` dengan `test_size=0.25` dan `random_state=SEED`. Dokumentasi fungsi itu menyatakan: bila ukuran latih dan uji tidak diisi, bagian uji menjadi 0.25. Modul ini menuliskan 0.25 supaya angkanya terlihat. Itu pilihan di modul ini, bukan hukum tunggal.

Baseline memakai `DummyRegressor(strategy="mean")`. Dokumentasinya menyatakan strategi `"mean"` selalu menebak rata-rata data latih. Kolom `Situps` tetap diisi karena fungsi itu meminta petunjuk, tetapi tebakannya tidak berubah mengikuti `Situps`. Semua tebakan sama dengan rata-rata kolom `Weight` pada data latih.

Kalau `kasus_mae_uji` lebih kecil daripada `kasus_mae_latih`, itu bukan tanda baseline melihat jawaban data uji: rata-ratanya dihitung dari data latih saja, dan lima baris uji kebetulan jaraknya lebih kecil. Halaman toy dataset scikit-learn mengatakan dataset sekecil ini sering terlalu kecil untuk mewakili tugas sungguhan. Angka pada data uji tetap yang disimpan sebagai penilaian baseline di modul ini.

## Kesalahan yang paling sering terjadi

1. Menilai baseline dari data latih, apalagi kalau model menghafal sampai rata-rata selisih mutlaknya nol. Angka yang menilai ada pada data uji.
2. Menghitung rata-rata baseline dari semua baris, termasuk jawaban data uji. Rata-rata itu hanya dari data latih. Kalau data uji ikut dirata-rata, lalu angkanya diubah lagi, penilaiannya tidak jujur.
3. Merata-rata selisih yang masih bertanda. Pada gambar 8, 10, dan 12, rata-rata itu nol padahal ada jarak.
4. Mengira tebakan baseline mengikuti kolom petunjuk. Pada strategi rata-rata, semua tebakan sama.
5. Angka di laporan ditulis dari ingatan, atau pemisahan dijalankan tanpa `random_state=SEED`, sehingga baris data uji berganti setiap kali notebook diulang.

## Cara menjalankan

Sel pertama setiap notebook berisi `SEED = 42`, seperti di modul 1. Angka tetap itu dipakai pada setiap pemisahan acak, lewat `random_state=SEED`, supaya baris yang terpilih sama setiap kali notebook diulang.

Paket adalah kumpulan berkas yang dipasang supaya kode bisa memanggil fungsi pustaka. uv adalah alat yang memasang paket sesuai daftar terkunci, lalu menjalankan perintah di lingkungan itu.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb` di folder modul ini, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only. Daftar paket yang terkunci ada di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Data uji boleh ikut dirata-rata saat baseline disusun. Benar atau salah?
3. Mengapa rata-rata selisih bertanda pada gambar 8, 10, dan 12 tidak dipakai sebagai angka penilaian?
4. "Baseline pada kasus mengikuti kolom Situps, jadi tebakannya berbeda-beda." Benar atau salah?
5. `tangan_mae_hafal` nol. Apakah angka nol itu penilaian pada data uji?
6. Dataset Linnerud diunduh dari internet saat notebook dijalankan. Benar atau salah?
7. Berapa baris data latih dan baris data uji yang tercetak pada kasus?
8. Berapa rata-rata selisih mutlak baseline pada data uji kasus, dan berapa angka baseline-nya?

### Kunci jawaban

1. **data latih dan data uji:** data dibagi dua: data latih dipakai model untuk belajar; data uji disisihkan dan tidak dilihat model saat belajar, dipakai untuk mengukur seberapa baik model pada data baru. **baseline:** cara menebak paling sederhana (misalnya selalu menebak rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; model yang baik harus mengalahkannya. **rata-rata selisih mutlak:** rata-rata dari jarak antara tebakan dan jawaban. Jarak berarti selisih yang tanda minusnya dibuang. Jumlah jarak dibagi banyak baris yang diukur. Semakin kecil angkanya, semakin dekat.
2. Salah. Rata-rata baseline hanya dari data latih.
3. Karena plus dan minus saling menghapus. Keluaran `tangan_bertanda` nol, padahal `tangan_jarak` masih berisi jarak.
4. Salah. `kasus_tebakan_sama` benar: semua tebakan baseline sama, dan `kasus_tebakan` sama dengan `kasus_baseline`.
5. Bukan. Nol itu jarak pada data latih karena model menghafal. Penilaian baseline memakai angka pada data uji.
6. Salah. Dataset Linnerud sudah ikut terpasang bersama scikit-learn; notebook tidak mengunduhnya.
7. `kasus_baris_latih 15` dan `kasus_baris_uji 5`, disalin dari keluaran di bawah.
8. `kasus_mae_uji 14.373333333333335` dan `kasus_baseline 177.13333333333333`, disalin dari keluaran di bawah.

Jawaban "coba sendiri": `tangan_rata 10.0`, `tangan_jarak_uji 6`, `tangan_mae 1.3333333333333333`, dan `tangan_bertanda 0.0`. Angka panjang disalin apa adanya dari keluaran, bukan dibulatkan dengan tangan.

### Angka yang disalin dari keluaran notebook

Jawaban di atas dan angka di bawah ini disalin dari keluaran notebook yang sudah dijalankan, bukan dihitung ulang di teks.

Indeks adalah nomor baris dari pandas, mulai dari 0.

Dari `notebook.ipynb`:

```
tangan_rata 10.0
tangan_jarak [2, 0, 2]
tangan_mae 1.3333333333333333
tangan_jarak_uji 6
tangan_mae_uji 6.0
tangan_bertanda 0.0
tangan_mae_hafal 0.0
kasus_baris 20
kasus_kolom 2
kasus_baris_latih 15
kasus_baris_uji 5
kasus_baseline 177.13333333333333
kasus_tebakan 177.13333333333333
kasus_tebakan_sama True
kasus_mae_uji 14.373333333333335
kasus_mae_latih 20.293333333333333
kasus_mae_sama True
kasus_mae_hafal 0.0
kasus_indeks_uji [0, 17, 15, 1, 8]
kasus_indeks_uji_lagi [0, 17, 15, 1, 8]
kasus_sama True
```

Dari `latihan-kunci.ipynb`:

```
kunci_rata 6.0
kunci_mae 3.0
kunci_baris_latih 15
kunci_baris_uji 5
kunci_baseline 35.666666666666664
kunci_mae_uji 2.266666666666667
indeks_uji [0, 17, 15, 1, 8]
indeks_uji_lagi [0, 17, 15, 1, 8]
latihan_indeks_sama True
```

## Sumber

- scikit-learn developers. `train_test_split`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html> Kalimat pada halaman itu: "Split arrays or matrices into random train and test subsets." Halaman yang sama: bila `train_size` juga `None`, `test_size` menjadi 0.25.
- scikit-learn developers. `DummyRegressor`. <https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html> Kalimat pada halaman itu untuk strategi `"mean"`: "always predicts the mean of the training set". Kalimat pada halaman yang sama: "Do not use it for real problems."
- scikit-learn developers. `mean_absolute_error`. <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html> Kalimat pada halaman itu: "The mean absolute error is a non-negative floating point value, where best value is 0.0." Nama bahasa Inggris itu nama fungsi untuk hitungan yang sama, bukan istilah kedua.
- scikit-learn developers. *Toy datasets* (Linnerud) dan `load_linnerud`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html> Halaman toy dataset menyatakan dataset ini tidak perlu mengunduh berkas dari situs lain, dan sering terlalu kecil untuk mewakili tugas sungguhan. Judul bagian di halaman itu tertulis Linnerrud. Nama yang dipakai di sini Linnerud, sama dengan fungsi `load_linnerud`.
- Tenenhaus, M. (1998). *La régression PLS : théorie et pratique.* Paris: Éditions Technip. Halaman scikit-learn menulis judul itu sebagai "La regression PLS: theorie et pratique" dan penerbitnya "Editions Technic". Ejaan di sini mengikuti katalog perpustakaan Sorbonne, ISBN 978-2-7108-0735-3. Judul buku itu bukan istilah yang diajarkan di modul ini.
