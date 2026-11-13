# Modul 5a: Validasi dan overfitting

**Tujuan belajar:** Mengenali data leakage, mengukur model dengan cross-validation, dan melihat overfitting dari selisih skor data latih dan data uji.

**Tingkat:** intermediate

**Istilah baru:** data leakage dan cross-validation. Overfitting sudah punya arti tetap dari modul regresi; di sini artinya diperdalam, bukan ditambah sebagai istilah baru.

## Cerita pembuka

Kamu mengerjakan setumpuk kartu latihan di meja. Sebagian kartu kamu hafal kata per kata. Besok kartunya beda, dan hafalan itu tidak menolong.

Lalu kamu merapikan kartu sambil mengintip lembar jawaban yang seharusnya tertutup. Nilai latihan melonjak. Lonjakan itu tidak jujur, karena jawaban yang belum boleh dilihat sudah ikut terbaca.

Cara yang lebih adil: bagi kartu menjadi beberapa tumpukan. Setiap tumpukan sekali ditahan dan tidak dipakai untuk belajar. Nilaimu adalah rata-rata giliran, bukan satu tumpukan yang kebetulan mudah.

Kalau kartu itu catatan jam per jam, jangan dikocok. Mengocok membuat catatan besok ikut mengajar kamu menjawab hari ini.

Angka di modul ini dibuat di memori. Tidak ada berkas yang diunduh. Bukan data asli perusahaan.

## Teori

Pustaka adalah kumpulan fungsi siap pakai, bukan rak buku. Paket adalah bundel kode yang dipasang ke lingkungan proyek. NumPy dan scikit-learn adalah pustaka sekaligus paket.

Data dibagi dua. Data latih dipakai model untuk belajar. Data uji disisihkan dan tidak dilihat model saat belajar, lalu dipakai untuk mengukur seberapa baik model pada data baru.

Di bagian ini ada dua istilah baru.

### data leakage

Gambar dulu. Empat nilai, dua terakhir ditahan:

```
2    4    |    6    8
latih     |    uji
```

Rata-rata yang boleh dipakai saat belajar: `(2 + 4) / 2`

Rata-rata yang sudah melihat data uji: `(2 + 4 + 6 + 8) / 4`

Hasil baginya kamu hitung sendiri di bagian berikutnya. Notebook mencetak hasilnya.

Nama teknisnya **data leakage**: informasi yang seharusnya tidak tersedia saat model belajar (misalnya dari data uji atau dari masa depan) ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan.

Perumpamaan: seperti mengerjakan latihan dengan kunci jawaban masih terbuka di meja. Nilai latihan terlihat tinggi karena jawaban yang belum boleh dilihat sudah ikut terbaca.

**Batas analogi:** kunci yang terbuka menggambarkan bocornya label. Analogi berhenti bila yang bocor adalah ringkasan seluruh baris, misalnya rata-rata kolom, sebelum data uji disisihkan. Pada data berurutan waktu, memakai kejadian besok untuk menebak hari ini tetap kebocoran.

Rata-rata yang bocor belum tentu menggeser skor pohon. Kebocorannya tetap nyata: angka dari data uji sudah terpakai. Notebook menunjukkan pemilihan kolom yang skornya terlihat lebih tinggi.

### overfitting

Arti yang dipakai di sini sama dengan modul regresi: model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru.

Gambar skornya, sebelum angkanya diisi dari keluaran:

```
data latih   ########
data uji     ####
```

Selisih itulah tanda menghafal. Notebook mencetak kedua skor. Modul ini tidak menambah perumpamaan baru untuk overfitting, supaya artinya tetap satu.

### cross-validation

Gambar dulu. Lima giliran, satu potongan ditahan tiap kali:

```
giliran 0   [uji] [latih] [latih] [latih] [latih]
giliran 1   [latih] [uji] [latih] [latih] [latih]
```

Lipatan adalah satu potongan pada giliran itu. Kata lipatan bagian dari cross-validation, bukan istilah terpisah. Nomor giliran dimulai dari 0. Notebook menomori lima lipatan 0, 1, 2, 3, dan 4.

Rumus, setelah gambar:

`rata-rata = (skor lipatan 0 + skor lipatan 1 + skor lipatan 2 + skor lipatan 3 + skor lipatan 4) / 5`

Angka tiap lipatan dicetak notebook. Jangan diisi dari ingatan.

Nama teknisnya **cross-validation**: cara mengukur model dengan memutar bagian yang disisihkan: data dibagi beberapa lipatan, tiap lipatan bergiliran menjadi data uji, lalu skor lipatan dirata-rata.

Perumpamaan: seperti regu yang bergiliran menahan satu halaman. Setiap halaman sekali tidak dipakai untuk belajar. Nilai regu adalah rata-rata giliran, bukan nilai satu halaman saja.

**Batas analogi:** regu itu tetap memakai buku yang sama. Cross-validation tidak mendatangkan data dari bulan depan. Bila baris berurutan waktu, mengocok bisa membuat masa depan ikut melatih masa lalu; giliran yang adil menahan masa depan di belakang. Analogi halaman tidak mengukur jenis kesalahan mana yang lebih mahal.

TimeSeriesSplit memotong data berurutan tanpa mengocok: jam pada data uji selalu di belakang jam pada data latih. Nama itu satu kalimat, bukan istilah baru.

## Coba sendiri dulu, baru kode

Pakai empat angka pada gambar: 2, 4, 6, dan 8. Dua terakhir adalah data uji.

1. Berapa `(2 + 4 + 6 + 8) / 4`?
2. Berapa `(2 + 4) / 2`?
3. Rata-rata mana yang boleh dipakai saat model belajar?

Hitung dengan tangan dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

`fit` adalah langkah menghitung angka dari baris yang diberikan, misalnya rata-rata. `transform` menerapkan angka itu ke baris lain. SelectKBest memilih beberapa kolom. f_classif mengukur seberapa beda rata-rata kolom antara dua kelas. LogisticRegression menyusun batas antara dua golongan dari jumlah berbobot. DecisionTreeClassifier menyusun aturan jika-maka. KFold memotong lipatan. cross_val_score mengulang skor tiap giliran. Nama-nama ini bukan istilah baru.

Tiga situasi, semuanya sintetis dan tanpa unduhan.

1. Empat angka kecil, lalu StandardScaler. Rata-rata yang dihitung dari seluruh angka dibanding rata-rata dari data latih saja.
2. Empat ratus baris dan dua ribu kolom dari `standard_normal`: undian sebaran normal baku, rata-rata 0 dan simpangan baku 1. Jawaban dari `integers(0, 2)`, yaitu bilangan bulat dari 0 sampai sebelum 2, jadi hanya 0 atau 1. `default_rng(SEED)` membuat Generator NumPy. Seed berupa bilangan bulat membuat undian itu berulang. Cara yang salah memilih kolom sebelum data dibagi. Cara yang benar membagi dulu, lalu memilih kolom hanya dari data latih. Kolom dan jawaban diundi terpisah, jadi skor yang jujur berada di sekitar setengah.
3. Catatan jam. Urutan yang dikocok dibanding TimeSeriesSplit. Lalu pohon yang membaca nomor jam: sekali dengan jam dikocok, sekali dengan data uji yang benar-benar belakangan.

Overfitting dicek pada data dari `make_classification`. Notebook modul ini mengisi parameter berikut:

- `n_samples`: banyak baris. Kasus utama 400, latihan 300.
- `n_features`: banyak kolom. Kasus utama 30, latihan 25.
- `n_informative`: banyak kolom yang membedakan kelas. Kasus utama 3, latihan 2.
- `n_redundant=0` dan `n_repeated=0`: tidak ada kolom salinan.
- `n_clusters_per_class=1`: satu kelompok untuk tiap kelas.
- `class_sep`: jarak antar kelompok. Makin besar, soal makin mudah. Kasus utama 0.7, latihan 0.6.
- `flip_y`: bagian baris yang labelnya ditukar. Kasus utama 0.1, latihan 0.12.
- `random_state=SEED`: undian yang sama berulang.

Pohon tanpa batas kedalaman dibanding pohon yang hanya bercabang dua kali. Cross-validation pohon tanpa batas dijalankan hanya pada data latih. Data uji yang sudah disisihkan tidak ikut giliran.

## Kesalahan yang paling sering terjadi

1. Rata-rata kolom, atau pemilihan kolom, dihitung dari seluruh baris sebelum data uji disisihkan. Skor lalu terlihat lebih bagus dari kenyataan.
2. Catatan yang berurutan waktu dikocok. Jam masa depan masuk data latih.
3. Hanya skor data latih yang dibaca. Pohon yang menghafal terlihat sempurna di situ.
4. Satu kali pembagian acak dianggap jawaban akhir. Cross-validation memutar bagian yang ditahan, lalu merata-rata skornya.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Venv adalah lingkungan terpisah yang menyimpan pemasangan paket Python untuk satu proyek, supaya versi paket proyek ini tidak tertukar dengan proyek lain. uv adalah alat yang memasang paket ke venv sesuai berkas kunci di root repo. `pyproject.toml` dan `uv.lock` adalah berkas di root yang mencatat paket dan kuncinya.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb` di folder ini, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian acak, lewat `random_state=SEED`, supaya hasil yang sama muncul setiap kali notebook diulang.

CPU only. Versi Python ada di `.python-version`. Versi paket ada di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan dua istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya. Overfitting disebut juga: apakah itu istilah baru modul ini?
2. Pada nilai 2, 4, 6, 8 dengan dua terakhir sebagai data uji, rata-rata mana yang boleh?
3. Mengapa mengocok catatan jam bisa membuat skor terlihat lebih bagus?
4. Pada keluaran notebook, pohon mana yang menghafal? Sebut skor data latih dan skor data ujinya.
5. Apa yang dirata-rata pada cross-validation?
6. Data modul ini diunduh saat notebook dijalankan. Benar atau salah?
7. Untuk apa `SEED = 42`?

### Kunci jawaban

1. **data leakage:** informasi yang seharusnya tidak tersedia saat model belajar (misalnya dari data uji atau dari masa depan) ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan. **cross-validation:** cara mengukur model dengan memutar bagian yang disisihkan: data dibagi beberapa lipatan, tiap lipatan bergiliran menjadi data uji, lalu skor lipatan dirata-rata. Overfitting bukan istilah baru modul ini. Artinya tetap: model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru.
2. Rata-rata dua nilai pertama, yaitu data latih. Keluaran: `mean_latih 3.0`. Rata-rata seluruh nilai adalah `mean_semua 5.0`, dan itu sudah melihat data uji.
3. Jam masa depan ikut masuk data latih, jadi model sudah melihat pola di sekitar jam yang lalu dipakai sebagai ujian. Pada keluaran, `skor_kocok` lebih tinggi daripada `skor_urut`.
4. Pohon tanpa batas. `skor_latih_dalam 1.0` dan `skor_uji_dalam` lebih rendah. Pohon pendek punya `selisih_dangkal` yang kecil. Salin kedua selisih dari blok di bawah.
5. Skor tiap lipatan yang bergiliran menjadi data uji. Hasilnya baris `rata_lipatan`.
6. Salah. Baris dibuat di memori dengan generator NumPy dan `make_classification`. Tidak ada berkas yang diunduh.
7. Supaya setiap undian acak di notebook ini memakai angka tetap yang sama, dan hasil yang terambil berulang.

### Angka yang disalin dari keluaran notebook

Jawaban di atas yang berupa angka disalin dari keluaran, bukan dihitung ulang di teks.

Dari `notebook.ipynb`:

```
mean_semua 5.0
mean_latih 3.0
mean_scaler_salah 5.0
mean_scaler_benar 3.0
baris_acak 400
kolom_acak 2000
kolom_terpilih 15
skor_salah 0.74
baris_latih 300
baris_uji 100
skor_benar 0.47
acak_uji_min 0
acak_latih_max 79
masa_depan_di_latih 60
giliran 0 latih_akhir 19 uji_awal 20 urut 1
giliran 1 latih_akhir 39 uji_awal 40 urut 1
giliran 2 latih_akhir 59 uji_awal 60 urut 1
baris_jam 240
skor_kocok 0.6666666666666666
skor_urut 0.55
baris_pola 400
kolom_pola 30
n_latih 280
n_uji 120
skor_latih_dalam 1.0
skor_uji_dalam 0.6666666666666666
skor_latih_dangkal 0.8107142857142857
skor_uji_dangkal 0.8083333333333333
selisih_dalam 0.33333333333333337
selisih_dangkal 0.0023809523809523725
lipatan 0 0.6785714285714286
lipatan 1 0.7142857142857143
lipatan 2 0.7321428571428571
lipatan 3 0.5892857142857143
lipatan 4 0.6964285714285714
rata_lipatan 0.6821428571428572
```

Dari `latihan-kunci.ipynb`:

```
latihan_mean_semua 4.0
latihan_mean_latih 2.0
latihan_rata_boleh data latih
latihan_acak_uji_min 0
latihan_acak_latih_max 11
latihan_masa_depan_di_latih 9
latihan_giliran 0 latih_akhir 3 uji_awal 4 urut 1
latihan_giliran 1 latih_akhir 7 uji_awal 8 urut 1
latihan_boleh_kocok tidak
latihan_n_latih 210
latihan_n_uji 90
latihan_skor_latih_dalam 1.0
latihan_skor_uji_dalam 0.7333333333333333
latihan_skor_latih_dangkal 0.8380952380952381
latihan_skor_uji_dangkal 0.8111111111111111
latihan_selisih_dalam 0.2666666666666667
latihan_selisih_dangkal 0.026984126984127
latihan_menghafal dalam
```

## Sumber

- scikit-learn developers. *3.1. Cross-validation: evaluating estimator performance.* <https://scikit-learn.org/stable/modules/cross_validation.html>
- scikit-learn developers. *12. Common pitfalls and recommended practices*, bagian 12.2 Data leakage. <https://scikit-learn.org/stable/common_pitfalls.html>
- scikit-learn developers. `TimeSeriesSplit`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html>
- scikit-learn developers. `KFold` dan `cross_val_score`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html>
- scikit-learn developers. `make_classification`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html>
- scikit-learn developers. `SelectKBest`, `StandardScaler`, `LogisticRegression`, dan `DecisionTreeClassifier`. <https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html>
- James, G., Witten, D., Hastie, T., dan Tibshirani, R. *An Introduction to Statistical Learning: with Applications in R*, Second Edition. Springer, 2021. Situs resmi menuliskan classification dan resampling methods di antara babnya. <https://www.statlearning.com/>
