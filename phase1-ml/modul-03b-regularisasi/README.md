# Modul 3b: Regularisasi (Ridge dan Lasso)

**Tujuan belajar:** Menahan angka pengali pada garis tebakan supaya tidak membesar hanya karena kebetulan satu kumpulan baris, lalu membedakan denda kuadrat dan denda nilai mutlak.

**Tingkat:** intermediate

Modul 3b tidak menutup tingkat. Ujian tingkat untuk label ini ada di modul 5b, bukan di sini.

## Cerita pembuka

Kamu meracik jus. Banyak bahan, dan satu gelas percobaan kebetulan terasa pas. Kalau takaran tiap bahan bebas membesar hanya supaya gelas itu tertiru, gelas berikutnya bisa terlalu manis atau hambar.

Yang ingin ditebak: kadar manis, satu angka. Bahan yang dicatat membantu tebakan, tetapi tidak semuanya berguna. Modul ini tidak memakai data asli perusahaan. Angka pada cerita adalah gambar, bukan hasil pengukuran.

## Pengingat

Hanya ada tiga istilah baru: regularisasi, Ridge, dan Lasso. Kalimat di bawah menjelaskan kata lain satu kali. Kata-kata itu bukan istilah baru.

Petunjuk adalah angka yang dibaca untuk menyusun tebakan.

Koefisien adalah angka pengali pada satu petunjuk di garis tebakan.

Penalti adalah tambahan yang membesar bila koefisien membesar.

Simpangan baku mengukur sebaran angka di sekitar rata-ratanya.

Regresi linear menebak jawaban angka sebagai jumlah petunjuk yang masing-masing dikalikan koefisien, ditambah satu bilangan geser.

intercept_ adalah nama tempat scikit-learn menyimpan bilangan geser.

coef_ adalah nama tempat scikit-learn menyimpan koefisien.

Fungsi kerugian adalah angka kesalahan yang diperkecil saat model belajar; pada regresi linear tanpa penalti, angka itu adalah jumlah kuadrat selisih antara tebakan dan jawaban. Selama banyak baris data latih tidak berubah, garis yang memperkecil jumlah kuadrat itu sama dengan garis yang memperkecil rata-ratanya.

Data latih dan data uji berarti data dibagi dua: data latih dipakai model untuk belajar; data uji disisihkan dan tidak dilihat model saat belajar, dipakai untuk mengukur seberapa baik model pada data baru.

fit adalah langkah saat model belajar dari data yang diberikan kepadanya.

Overfitting berarti model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru.

Baseline adalah cara menebak paling sederhana (misalnya selalu menebak rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; model yang baik harus mengalahkannya.

Rata-rata selisih mutlak adalah rata-rata jarak antara tebakan dan jawaban, jarak berarti selisih yang tanda minusnya dibuang, jumlah jarak dibagi banyak baris yang diukur, semakin kecil semakin dekat, nilai terbaik adalah nol, dan fungsi scikit-learn untuk hitungan yang sama bernama mean_absolute_error.

alpha adalah angka yang mengalikan penalti; makin besar nilainya, makin kuat penalti itu.

StandardScaler menggeser tiap petunjuk supaya rata-ratanya nol dan simpangan bakunya satu, memakai rata-rata dan simpangan baku data yang dipelajari saat fit; transform memakai angka itu pada data lain.

Pustaka adalah kumpulan fungsi siap pakai yang dipanggil dari kode.

Array adalah kumpulan nilai sejenis dengan bentuk yang tetap, yang dihitung sekaligus.

NumPy adalah pustaka untuk hitungan pada array.

Derau adalah gangguan acak pada jawaban.

Gauss pada derau ini adalah sebaran berbentuk lonceng: nilai kecil lebih sering daripada nilai besar.

Parameter noise pada make_regression adalah simpangan baku derau Gauss yang ditambahkan ke jawaban.

Parameter bias pada make_regression adalah geseran tetap, yaitu bilangan geser pada model linear yang membuat jawaban.

## Teori

### regularisasi

Pada jus, denda membesar bila takaran membesar. Garis tebakan yang tanpa denda bebas membesarkan koefisien agar kebetulan data latih tertiru. Nama teknisnya **regularisasi**.

Artinya: penalti yang ditambahkan pada fungsi kerugian regresi linear supaya koefisien tidak bebas membesar mengikuti kebetulan di data latih.

Perumpamaan: seperti denda pada takaran bumbu: makin jauh takaran dari nol, makin besar dendanya, jadi resep tidak meniru setiap kebetulan satu gelas percobaan.

**Batas analogi:** denda pada cerita tidak dijumlahkan dengan rasa yang meleset. Pada model, penalti dijumlahkan dengan fungsi kerugian, lalu jumlah itu yang diperkecil. Gambar bumbu tidak membedakan kuadrat dan nilai mutlak. Penalti mengenai koefisien, bukan bilangan geser.

### Ridge

Gambar dulu. Dua calon koefisien, hanya bagian penaltinya:

```
calon A    2     2
kuadrat    4     4    jumlah 8
mutlak     2     2    jumlah 4

calon B    3     0
kuadrat    9     0    jumlah 9
mutlak     3     0    jumlah 3
```

Jumlah kuadrat calon A lebih kecil. Nama teknis penalti kuadrat ini **Ridge**.

Artinya: regularisasi yang penalinya jumlah kuadrat koefisien. Koefisien mengecil ke arah nol, tetapi penalti kuadrat ini pada umumnya tidak membuat koefisien tepat nol.

Pada scikit-learn, yang diperkecil adalah jumlah kuadrat selisih ditambah alpha kali jumlah kuadrat koefisien. Makin besar alpha, makin kuat penalti itu.

Perumpamaan: seperti tali yang menarik tiap takaran mendekati nol: makin jauh, tarikannya makin cepat membesar, tetapi takaran tidak dipaksa putus menjadi nol.

**Batas analogi:** tali tidak menghitung kuadrat. Penalti Ridge adalah jumlah kuadrat koefisien, dikali alpha. Koefisien bisa sangat kecil tanpa menjadi tepat nol. Alpha yang sama bukan kekuatan yang sama dengan Lasso, karena bagian selisih kuadrat pada rumus scikit-learn disusun berbeda.

### Lasso

Pada gambar yang sama, jumlah nilai mutlak calon B lebih kecil, dan satu koefisiennya nol. Nama teknis penalti nilai mutlak ini **Lasso**.

Artinya: regularisasi yang penalinya jumlah nilai mutlak koefisien, dan penalti itu bisa membuat sebagian koefisien tepat nol.

Pada scikit-learn, yang diperkecil adalah jumlah kuadrat selisih dibagi dua kali banyak baris, ditambah alpha kali jumlah nilai mutlak koefisien. Pembagi itu tidak ada pada rumus Ridge, jadi alpha yang sama bukan kekuatan yang sama.

Perumpamaan: seperti boleh membuang satu bumbu sampai takarannya tepat nol bila bumbu itu tidak membantu.

**Batas analogi:** membuang bumbu pada gambar adalah pilihan orang. Nol pada Lasso muncul dari penalti nilai mutlak, bukan dari mencoret kolom dengan tangan. Tidak semua koefisien harus nol. Koefisien nol pada data ini tidak membuktikan petunjuk itu tak berguna pada data lain.

Gambar di atas hanya bagian penalti, belum ditambah selisih tebakan. Notebook mencetak jumlahnya; kunci di bawah menyalin cetakan itu.

## Coba sendiri dulu, baru kode

Pakai gambar dua calon di atas. Hitung dengan tangan, lalu cocokkan dengan gambar itu.

1. Berapa `2² + 2²` dan `3² + 0²`?
2. Berapa `|2| + |2|` dan `|3| + |0|`?
3. Penalti kuadrat yang lebih kecil milik calon yang mana?
4. Penalti nilai mutlak yang lebih kecil milik calon yang mana?

Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

Jawaban dan petunjuk dibuat di memori oleh `sklearn.datasets.make_regression`, dengan `random_state=SEED`. Bukan unduhan. Bukan data asli perusahaan.

Parameter yang diisi, sesuai dokumentasi fungsi itu:

- `n_samples=50`: banyak baris.
- `n_features=30`: banyak petunjuk.
- `n_informative=5`: banyak petunjuk yang dipakai untuk membangun model linear yang menghasilkan jawaban. Petunjuk selebihnya tidak masuk model pembuat data.
- `noise=15.0`: simpangan baku derau Gauss yang ditambahkan ke jawaban.
- `bias=2.5`: geseran tetap pada model linear yang membuat jawaban.
- `random_state=SEED`: mengunci undian pembuatan data.

Parameter yang tidak diisi:

- `n_targets` bawaan 1, jadi jawabannya satu angka per baris.
- `effective_rank` bawaan `None`: masukan yang dikembalikan terpusat, variasinya satu, dan terkondisi baik.
- `tail_strength` hanya dipakai bila `effective_rank` diisi. Di sini tidak.
- `shuffle` bawaan `True`: urutan baris dan kolom diacak. `random_state` mengunci pengacakan itu.
- `coef` bawaan `False`: koefisien pembuat data tidak dikembalikan. Modul ini tidak mengklaim nol pada Lasso sama dengan petunjuk yang tidak dipakai pembuat data.

Setelah data terbuat, kolom pertama dikalikan 50. Ini langkah modul, bukan parameter `make_regression`. Karena `effective_rank` kosong, kolom itu tadinya variasinya satu; kali 50 membuat sebarannya jauh lebih lebar. Penalti peka skala, jadi petunjuk yang sebarannya jauh lebih besar bisa menguasai hitungan.

`train_test_split` memisahkan baris dengan `test_size=0.25` dan `random_state=SEED`. Seperempat baris menjadi data uji. Dokumentasi fungsi itu: bila ukuran latih juga kosong, bagian uji menjadi 0.25. Modul ini menuliskan 0.25 supaya angkanya terlihat.

DummyRegressor(strategy="mean") selalu menebak rata-rata jawaban data latih; strategy adalah pilihan cara baseline, dan mean berarti rata-rata. Nama fungsi itu bukan istilah baru. Di kasus ini baseline hanya pembanding. Contoh kelas yang paling banyak tidak dihitung.

LinearRegression adalah regresi linear tanpa penalti pada fungsi kerugian.

StandardScaler dipasang pada data latih, lalu model belajar dari hasil itu. Saat fit, rata-rata dan simpangan baku dihitung dari data latih saja. Dokumentasi StandardScaler menyatakan simpangan baku itu setara `numpy.std(x, ddof=0)`, yaitu pembagi banyak baris. Kata bahasa Inggris "biased estimator" pada catatan itu adalah pembagi tersebut, bukan parameter `bias` pada `make_regression`.

alpha Ridge pada kasus adalah 5. alpha Lasso pada kasus adalah 0.5. Keduanya pilihan modul ini untuk satu perbandingan, bukan alpha terbaik untuk setiap data. Dokumentasi menyarankan `LinearRegression` bila tidak ingin penalti; `alpha=0` pada Ridge atau Lasso tidak disarankan.

Yang dibandingkan pada data uji: rata-rata selisih mutlak. Makin kecil, makin dekat. Ridge pada data ini lebih kecil daripada regresi tanpa penalti. Lasso punya koefisien yang tepat nol. Ridge pada data ini tidak.

## Kesalahan yang paling sering terjadi

1. Menilai garis hanya dari data latih. Regresi tanpa penalti bisa dekat di data latih dan jauh di data uji. Itu overfitting. Angka yang menilai ada pada data uji.
2. Mengira penalti kuadrat membuat koefisien tepat nol. Pada kasus, jumlah koefisien Ridge yang tepat nol tercetak nol.
3. Mengira koefisien Lasso yang nol pasti tak berguna untuk selamanya. Nol itu hasil penalti pada data ini.
4. Memakai angka alpha yang sama seolah rumus Ridge dan Lasso identik. Pembagi pada bagian selisih kuadratnya berbeda.
5. Menghitung rata-rata StandardScaler dari semua baris, termasuk data uji. StandardScaler pada kasus belajar dari data latih saja.
6. Menyamakan parameter `bias` pada `make_regression` dengan catatan "biased estimator" pada StandardScaler. Yang pertama geseran tetap. Yang kedua pembagi simpangan baku.
7. Mengisi `alpha=0` pada Ridge atau Lasso. Dokumentasi menyarankan LinearRegression bila tidak ada penalti.
8. Mengulang notebook tanpa `random_state=SEED`, sehingga baris data uji berganti.

## Cara menjalankan

Paket adalah kumpulan berkas yang dipasang supaya kode bisa memanggil fungsi pustaka.

uv adalah alat yang memasang paket sesuai daftar terkunci, lalu menjalankan perintah di lingkungan itu.

Sel pertama setiap notebook berisi `SEED = 42`, seperti di modul sebelumnya. Angka itu dipakai pada setiap undian acak, lewat `random_state=SEED`.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest
uv run pytest --nbmake
```

Buka `notebook.ipynb` di folder modul ini, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only. Daftar paket yang terkunci ada di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Pada gambar calon A (2 dan 2) dan calon B (3 dan 0), penalti kuadrat mana yang lebih kecil? Penalti nilai mutlak mana yang lebih kecil?
3. Ridge pada kasus membuat sedikitnya satu koefisien tepat nol. Benar atau salah?
4. Apakah rata-rata selisih mutlak Ridge pada data uji lebih kecil daripada regresi tanpa penalti?
5. Berapa koefisien Lasso pada kasus yang tepat nol, dan berapa koefisien Ridge yang tepat nol?
6. `noise` pada `make_regression` mengukur apa? `bias` mengukur apa?
7. Mengapa petunjuk diseragamkan sebelum penalti, dan dari baris mana rata-rata StandardScaler dihitung?
8. `alpha=0` pada Ridge adalah cara yang disarankan dokumentasi untuk menghapus penalti. Benar atau salah?
9. Berapa baris data latih dan baris data uji yang tercetak?
10. Modul ini menutup tingkat dan memuat ujian tingkat. Benar atau salah?

### Kunci jawaban

1. **regularisasi:** penalti yang ditambahkan pada fungsi kerugian regresi linear supaya koefisien tidak bebas membesar mengikuti kebetulan di data latih. **Ridge:** regularisasi yang penalinya jumlah kuadrat koefisien. Koefisien mengecil ke arah nol, tetapi penalti kuadrat ini pada umumnya tidak membuat koefisien tepat nol. **Lasso:** regularisasi yang penalinya jumlah nilai mutlak koefisien, dan penalti itu bisa membuat sebagian koefisien tepat nol.
2. Penalti kuadrat calon A lebih kecil (`tangan_kuadrat_a 8.0`, `tangan_kuadrat_b 9.0`). Penalti nilai mutlak calon B lebih kecil (`tangan_mutlak_b 3.0`, `tangan_mutlak_a 4.0`).
3. Salah. `kasus_nol_ridge 0`.
4. Ya. `kasus_ridge_lebih_baik True`. `kasus_mae_uji_ridge 15.56518243431388` lebih kecil daripada `kasus_mae_uji_tanpa 37.180797267888494`.
5. `kasus_nol_lasso 6` dan `kasus_nol_ridge 0`.
6. `noise` adalah simpangan baku derau Gauss yang ditambahkan ke jawaban. `bias` adalah geseran tetap pada model linear yang membuat jawaban.
7. Penalti peka skala: petunjuk yang sebarannya jauh lebih besar bisa menguasai hitungan. `kasus_skala_latih True`: rata-rata StandardScaler sama dengan rata-rata data latih, bukan semua baris.
8. Salah. Dokumentasi menyarankan LinearRegression bila tidak ada penalti.
9. `kasus_baris_latih 37` dan `kasus_baris_uji 13`.
10. Salah. Modul 3b tidak menutup tingkat. Ujian tingkat untuk label ini ada di modul 5b.

Jawaban "coba sendiri" disalin dari keluaran di bawah: `tangan_kuadrat_a 8.0`, `tangan_kuadrat_b 9.0`, `tangan_mutlak_a 4.0`, `tangan_mutlak_b 3.0`.

### Angka yang disalin dari keluaran notebook

Jawaban di atas dan angka di bawah ini disalin dari keluaran notebook yang sudah dijalankan, bukan dihitung ulang di teks.

Dari `notebook.ipynb`:

```
tangan_kuadrat_a 8.0
tangan_kuadrat_b 9.0
tangan_mutlak_a 4.0
tangan_mutlak_b 3.0
tangan_kuadrat_a_lebih_kecil True
tangan_mutlak_b_lebih_kecil True
kasus_baris 50
kasus_kolom 30
kasus_baris_latih 37
kasus_baris_uji 13
kasus_mae_basis 57.411810161225546
kasus_mae_uji_tanpa 37.180797267888494
kasus_mae_latih_tanpa 5.484318130333347
kasus_mae_uji_ridge 15.56518243431388
kasus_mae_latih_ridge 14.36052852635922
kasus_nol_ridge 0
kasus_ridge_lebih_baik True
kasus_mae_uji_lasso 14.731507595481556
kasus_mae_latih_lasso 8.010166534837767
kasus_nol_lasso 6
kasus_skala_latih True
kasus_indeks_uji [13, 39, 30, 45, 17, 48, 26, 25, 32, 19, 12, 4, 37]
kasus_indeks_uji_lagi [13, 39, 30, 45, 17, 48, 26, 25, 32, 19, 12, 4, 37]
kasus_sama True
```

Dari `latihan-kunci.ipynb`:

```
kunci_kuadrat_a 32.0
kunci_kuadrat_b 36.0
kunci_kuadrat_a_lebih_kecil True
kunci_mutlak_a 8.0
kunci_mutlak_b 6.0
kunci_mutlak_b_lebih_kecil True
kunci_baris 50
kunci_kolom 30
kunci_baris_latih 37
kunci_baris_uji 13
kunci_mae_uji_tanpa 37.180797267888494
kunci_mae_uji_ridge 12.503546642054934
kunci_nol_ridge 0
kunci_ridge_lebih_baik True
kunci_mae_uji_lasso 13.36338837752184
kunci_nol_lasso 13
kunci_skala_latih True
```

## Sumber

Nama l2 pada dokumentasi Ridge adalah sebutan untuk penalti kuadrat.

Nama l1 pada dokumentasi Lasso adalah sebutan untuk penalti nilai mutlak.

- scikit-learn developers. *1.1. Linear Models.* <https://scikit-learn.org/stable/modules/linear_model.html> Kalimat pada pembuka: prediksi ditulis `w0 + w1 x1 + ... + wp xp`, `w` disimpan sebagai `coef_`, dan `w0` sebagai `intercept_`. Bagian Ordinary Least Squares: `LinearRegression` meminimalkan jumlah kuadrat selisih antara jawaban teramati dan tebakan linear. Bagian Ridge: koefisien meminimalkan `||Xw - y||^2 + alpha ||w||^2`; makin besar alpha, makin besar penyusutannya. Bagian Lasso: model ini mampu membuat koefisien tepat nol. Rumus pada bagian itu: `1 / (2 n_samples) * ||Xw - y||^2 + alpha ||w||_1`. Daftar pustaka pada bagian Lasso menuliskan: Robert Tibshirani. (1996) Regression Shrinkage and Selection Via the Lasso. J. R. Stat. Soc. Ser. B Stat. Methodol., 58(1):267-288.
- scikit-learn developers. `Ridge`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html> Rumus pada halaman itu: `||y - Xw||^2_2 + alpha * ||w||^2_2`. Kalimat untuk `alpha`: "Constant that multiplies the L2 term, controlling regularization strength." Kalimat pada halaman yang sama: "When `alpha = 0`, the objective is equivalent to ordinary least squares, solved by the `LinearRegression` object. For numerical reasons, using `alpha = 0` with the `Ridge` object is not advised."
- scikit-learn developers. `Lasso`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html> Rumus pada halaman itu: `(1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1`. Kalimat untuk `alpha`: "Constant that multiplies the L1 term, controlling regularization strength." Contoh pada halaman itu mencetak satu koefisien `0.`.
- scikit-learn developers. `LinearRegression`. <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html> Halaman ini yang disarankan dokumentasi Ridge dan Lasso bila tidak ada penalti.
- scikit-learn developers. `make_regression`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html> `n_samples`: "The number of samples." `n_features`: "The number of features." `n_informative`: "The number of informative features, i.e., the number of features used to build the linear model used to generate the output." `n_targets`: "By default, the output is a scalar." `bias`: "The bias term in the underlying linear model." `effective_rank` bila `None`: "The input set is well conditioned, centered and gaussian with unit variance." `tail_strength`: "if effective_rank is not None." `noise`: "The standard deviation of the gaussian noise applied to the output." `shuffle`: "Shuffle the samples and the features." `coef`: "If True, the coefficients of the underlying linear model are returned." `random_state` mengunci pembuatan data.
- scikit-learn developers. `StandardScaler`. <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html> Rumus pada halaman itu: `z = (x - u) / s`. Kalimat pada halaman itu: "Centering and scaling happen independently on each feature by computing the relevant statistics on the samples in the training set. Mean and standard deviation are then stored to be used on later data using `transform`." Catatan pada halaman itu: "We use a biased estimator for the standard deviation, equivalent to `numpy.std(x, ddof=0)`." Kalimat pada halaman yang sama: "For instance many elements used in the objective function of a learning algorithm (such as the RBF kernel of Support Vector Machines or the L1 and L2 regularizers of linear models) assume that all features are centered around 0 and have variance in the same order."
- scikit-learn developers. `train_test_split`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html> Kalimat pada halaman itu: "Split arrays or matrices into random train and test subsets." Bila `train_size` juga `None`, `test_size` menjadi 0.25.
- scikit-learn developers. `DummyRegressor`. <https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html> Kalimat untuk strategi `"mean"`: "always predicts the mean of the training set".
- scikit-learn developers. `mean_absolute_error`. <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html> Kalimat pada halaman itu: "The mean absolute error is a non-negative floating point value, where best value is 0.0."
- Astral. *uv.* <https://docs.astral.sh/uv/>
