# Modul 5b: Metrik penilaian dan ujian Intermediate

**Tujuan belajar:** Membaca confusion matrix, memilih precision atau recall sesuai harga kesalahan, dan menutup tingkat intermediate dengan ujian singkat.

**Tingkat:** intermediate

**Istilah baru:** confusion matrix, precision, dan recall.

## Cerita pembuka

Kamu menyortir mangga di meja. Keranjang "matang" untuk yang boleh dijual. Keranjang lain untuk yang ditahan.

Menghitung saja "berapa banyak yang kamu taruh di keranjang yang benar" bisa menipu. Kamu bisa menahan hampir semua mangga. Jarang ada yang salah taruh, tetapi mangga matang banyak yang tertinggal.

Dua pertanyaan yang lebih jujur: di antara mangga dalam keranjang matang, berapa yang memang matang? Dan di antara semua mangga matang yang ada, berapa yang berhasil masuk keranjang?

Alarm jemuran memakai pertanyaan yang sama. Hujan lebih jarang daripada langit cerah. Alarm yang tidak pernah berbunyi sering "cocok", tetapi jemuran tetap basah.

Angka di modul ini dibuat di memori. Tidak ada berkas yang diunduh. Bukan data asli perusahaan.

## Teori

Pustaka adalah kumpulan fungsi siap pakai, bukan rak buku. Paket adalah bundel kode yang dipasang ke lingkungan proyek. NumPy dan scikit-learn adalah pustaka sekaligus paket.

Kelas di sini artinya golongan jawaban, bukan ruang belajar. Kelas positif adalah golongan yang kita cari. Data latih dipakai untuk belajar. Data uji disisihkan. Baseline selalu menebak kelas yang paling banyak. Satu angka "seberapa sering cocok" menyembunyikan jenis salahnya.

Di bagian ini ada tiga istilah baru.

Gambar dulu. Satu keranjang matang:

```
                    tebakan positif    tebakan negatif
benar positif              8                  1
benar negatif              2                  9
```

Delapan buah matang masuk. Dua buah mentah ikut masuk. Satu buah matang tertinggal. Sembilan buah mentah benar ditolak.

### confusion matrix

Tabel empat hitungan itu bernama **confusion matrix**: tabel hitungan untuk dua kelas: berapa kali tebakan positif benar, tebakan positif salah, tebakan negatif salah, dan tebakan negatif benar.

Perumpamaan: seperti empat keranjang di meja sortir buah. Keranjang memisahkan buah matang yang lolos, buah mentah yang keliru masuk, buah matang yang tertinggal, dan buah mentah yang benar ditolak.

**Batas analogi:** empat keranjang hanya untuk dua golongan. Tiga golongan atau lebih butuh lebih dari empat kotak. Keranjang menghitung banyaknya buah, bukan harga kesalahan.

Di kode, baris confusion matrix adalah jawaban benar dan kolom adalah tebakan, mengikuti dokumentasi scikit-learn. Notebook mencetak nama tiap kotak supaya posisinya tidak tertukar.

### precision

**Precision** adalah di antara semua tebakan positif, bagian yang benar-benar positif.

Rumus, setelah gambar di atas:

`precision = 8 / (8 + 2)`

Perumpamaan: di antara buah yang kamu taruh di keranjang matang, bagian yang memang matang.

**Batas analogi:** tidak menghitung buah matang yang tidak masuk keranjang. Keranjang berisi satu buah matang dan tidak ada yang lain punya precision sempurna, walaupun banyak buah matang tertinggal.

### recall

**Recall** adalah di antara semua yang benar-benar positif, bagian yang berhasil ditebak positif.

Rumus:

`recall = 8 / (8 + 1)`

Perumpamaan: di antara semua buah matang yang ada, bagian yang berhasil masuk keranjang matang.

**Batas analogi:** tidak menghitung buah mentah yang ikut masuk. Memasukkan semua buah membuat recall sempurna dan keranjang itu tidak berguna. Precision dan recall tidak saling menggantikan.

Hasil bagi dua rumus itu kamu hitung sendiri dulu. Notebook mencetaknya. Angka gabungan dari precision dan recall ada di dokumentasi, dan di luar modul ini.

Overfitting, arti yang sudah tetap: model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru. Metrik di modul ini dihitung pada data uji. Selisih skor latih dan uji menunjukkan apakah model menghafal.

Data leakage, arti yang sudah tetap: informasi yang belum boleh dipakai saat belajar ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan. Modul ini tidak mengubah arti itu.

## Coba sendiri dulu, baru kode

Pakai gambar delapan, dua, satu, dan sembilan.

1. Berapa `8 / (8 + 2)`?
2. Berapa `8 / (8 + 1)`?
3. Kalau yang kamu takutkan adalah buah matang tertinggal, angka mana yang kamu lihat dulu?

Hitung dengan tangan dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`.

## Kasus nyata

`fit` menghitung aturan dari data latih. `predict` menghasilkan tebakan. precision_score dan recall_score menghitung dua rasio dari tebakan. Nama fungsi ini bukan istilah tambahan. DecisionTreeClassifier menyusun aturan jika-maka. `make_classification` mengundi soal klasifikasi. Notebook dan ujian mengisi parameter berikut:

- `n_samples=400`: banyak baris.
- `n_features`: banyak kolom. Kasus utama 6, ujian 20.
- `n_informative=3`: banyak kolom yang membedakan kelas.
- `n_redundant=0` dan `n_repeated=0`: tidak ada kolom salinan.
- `n_clusters_per_class=1`: satu kelompok untuk tiap kelas.
- `weights=[0.85, 0.15]`: bagian baris yang ditargetkan untuk tiap kelas. Angka akhirnya bisa sedikit beda bila ada label yang ditukar.
- `class_sep`: jarak antar kelompok. Makin besar, soal makin mudah. Kasus utama 1.1, ujian 1.3.
- `flip_y`: bagian baris yang labelnya ditukar. Kasus utama 0.03, ujian 0.02.
- `random_state=SEED`: undian yang sama berulang.

Kasusnya alarm jemuran. Kelas positif adalah hujan. Sebagian besar jam tidak hujan. Baseline selalu menebak kelas yang paling banyak. Pohon dengan cabang dibatasi dibanding pohon tanpa batas. Precision, recall, dan empat kotak dihitung pada data uji.

## Kesalahan yang paling sering terjadi

1. Hanya menghitung bagian tebakan yang cocok ketika kelas positif jarang. Baseline bisa cocok sering, dengan recall nol.
2. Precision dan recall ditukar. Yang satu melihat isi keranjang. Yang lain melihat buah matang yang tertinggal.
3. Metrik dihitung pada data latih, lalu model dianggap aman dari overfitting. Bandingkan juga skor data uji.
4. Empat kotak dibaca tanpa menetapkan kelas positif mana. Di modul ini kelas positif adalah kejadian yang dicari.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Venv adalah lingkungan terpisah yang menyimpan pemasangan paket Python untuk satu proyek, supaya versi paket proyek ini tidak tertukar dengan proyek lain. uv adalah alat yang memasang paket ke venv sesuai berkas kunci di root repo. `pyproject.toml` dan `uv.lock` adalah berkas di root yang mencatat paket dan kuncinya.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb` di folder ini, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Ujian tingkat ada di `ujian.ipynb`, kuncinya di `ujian-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian acak, lewat `random_state=SEED`, supaya hasil yang sama muncul setiap kali notebook diulang.

CPU only. Versi Python ada di `.python-version`. Versi paket ada di `uv.lock` di root repo.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Pada gambar 8, 2, 1, dan 9, berapa precision dan recall?
3. `cocok_jarang` tinggi dan `recall_jarang` nol. Apakah tebakan itu cukup untuk alarm hujan?
4. "Precision menghitung buah matang yang tertinggal." Benar atau salah? Sebutkan satu batas analoginya.
5. "Kelas" di modul ini artinya ruang belajar. Benar atau salah?

### Kunci jawaban

1. **confusion matrix:** tabel hitungan untuk dua kelas: berapa kali tebakan positif benar, tebakan positif salah, tebakan negatif salah, dan tebakan negatif benar. **precision:** di antara semua tebakan positif, bagian yang benar-benar positif. **recall:** di antara semua yang benar-benar positif, bagian yang berhasil ditebak positif.
2. Precision `0.8`, yaitu `8 / (8 + 2)`. Recall `0.8888888888888888`, yaitu `8 / (8 + 1)`. Keduanya tercetak sebagai `precision_contoh` dan `recall_contoh`.
3. Tidak cukup. Tebakan itu tidak menemukan hujan. Untuk jemuran, recall yang nol berarti jemuran basah.
4. Salah. Satu batas: precision tidak menghitung buah matang yang tidak masuk keranjang.
5. Salah. Kelas di sini artinya golongan jawaban, bukan ruang belajar.

### Angka yang disalin dari keluaran notebook

Dari `notebook.ipynb`:

```
banyak_baris 20
precision_contoh 0.8
recall_contoh 0.8888888888888888
precision_pustaka 0.8
recall_pustaka 0.8888888888888888
sama True
cocok_jarang 0.95
recall_jarang 0.0
bagian_hujan 0.1725
n_latih 280
n_uji 120
cocok_baseline 0.825
recall_baseline 0.0
skor_latih_dangkal 0.9464285714285714
cocok_uji 0.8916666666666667
tepat_negatif 94
salah_positif 5
salah_negatif 8
tepat_positif 13
precision_uji 0.7222222222222222
recall_uji 0.6190476190476191
skor_latih_dalam 1.0
skor_uji_dalam 0.85
```

Dari `latihan-kunci.ipynb`:

```
latihan_precision 0.6666666666666666
latihan_recall 0.6
latihan_cocok 0.9
latihan_recall_jarang 0.0
```

## Sumber

- scikit-learn developers. *3.4. Metrics and scoring: quantifying the quality of predictions*, bagian 3.4.4.6 Confusion matrix dan 3.4.4.9 Precision, recall and F-measures. Angka gabungan di bagian F-measures berada di luar modul ini. <https://scikit-learn.org/stable/modules/model_evaluation.html>
- scikit-learn developers. `confusion_matrix`, `precision_score`, dan `recall_score`. <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html>
- scikit-learn developers. `make_classification`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html>
- James, G., Witten, D., Hastie, T., dan Tibshirani, R. *An Introduction to Statistical Learning: with Applications in R*, Second Edition. Springer, 2021. Situs resmi menuliskan classification di antara babnya. <https://www.statlearning.com/>

## Ujian tingkat intermediate

Ini penutup tingkat intermediate: proyek mini plus pertanyaan. Bahan ada di `ujian.ipynb`. Kunci yang dijalankan ada di `ujian-kunci.ipynb`, lewat `uv run pytest --nbmake` dari root repo.

**Proyek mini.** Alarm jemuran pada data sintetis baru, `random_state=SEED`, tanpa unduhan. Kelas positif adalah hujan. Hujan lebih jarang. Melewatkan hujan membuat jemuran basah. Alarm palsu hanya membuat jemuran diangkat terlalu cepat. Baseline selalu menebak kelas yang paling banyak. Bandingkan baseline itu dengan pohon `max_depth=2` pada data uji, termasuk precision, recall, dan empat kotak. Bandingkan juga pohon itu dengan pohon tanpa batas kedalaman.

### Soal

1. Metrik mana yang diutamakan, dan mengapa?
2. Berapa recall baseline?
3. Berapa precision dan recall pohon pendek pada data uji?
4. Pohon mana yang menghafal? Bandingkan selisih skor data latih dan data uji antara pohon tanpa batas dan pohon pendek.
5. Model mana yang dilaporkan?
6. Jika rata-rata kolom dihitung dari seluruh baris sebelum data dibagi, apa nama kesalahannya, dan rata-rata mana yang boleh?

### Aturan penilaian

- Nomor soal di bagian ini, di `ujian.ipynb`, dan di `ujian-kunci.ipynb` sama. Kunci memakai nomor itu.
- Proyek mini memakai `SEED` di sel pertama dan `random_state=SEED`. Tidak ada berkas yang diunduh.
- Pohon dan baseline belajar dari data latih. Data uji hanya untuk mengukur.
- Soal yang meminta angka lulus bila angkanya sama dengan keluaran `ujian-kunci.ipynb`.
- Sel kunci punya `assert`. Tes modul menjalankan sumber sel itu.
- Ujian lulus bila semua soal sesuai kunci dan assert di `ujian-kunci.ipynb` lulus.

### Kunci ujian

1. Recall. Melewatkan hujan lebih merugikan daripada alarm palsu sesekali. Baris `ujian_metrik_dipilih recall`.
2. `ujian_recall_baseline 0.0`. Baseline tidak menemukan hujan.
3. Precision pohon pendek pada data uji `ujian_precision 0.8`. Recall pohon pendek pada data uji `ujian_recall 0.631578947368421`.
4. Pohon tanpa batas yang menghafal. Selisih skor data latih dan data uji pohon itu `ujian_selisih_dalam 0.10833333333333328`. Selisih pohon pendek `ujian_selisih_dangkal 0.04761904761904767`.
5. Pohon pendek yang dilaporkan. Recall keduanya seri di 0.6316, jadi pemecah serinya akurasi data uji: pohon pendek 0.9167, pohon tanpa batas 0.8917. Selisih skor data latih dan data uji yang lebih kecil ikut menguatkan pilihan itu, sesuai soal 1 yang mengutamakan recall. Baris `ujian_model_dipilih dangkal`.
6. Data leakage. Rata-rata yang boleh adalah rata-rata data latih. Baris `ujian_nama_kebocoran data leakage` dan `ujian_rata_boleh data latih`.

Empat kotak, skor latih, dan skor uji ada pada baris di bawah. Angka ini disalin dari keluaran yang dijalankan, bukan ditulis tangan.

#### Angka yang disalin dari keluaran notebook

Dari `ujian-kunci.ipynb`. `ujian.ipynb` tidak menyimpan keluaran.

```
ujian_baris 400
ujian_bagian_hujan 0.16
ujian_n_latih 280
ujian_n_uji 120
ujian_cocok_baseline 0.8416666666666667
ujian_recall_baseline 0.0
ujian_skor_latih_dangkal 0.9642857142857143
ujian_skor_uji_dangkal 0.9166666666666666
ujian_tepat_negatif 98
ujian_salah_positif 3
ujian_salah_negatif 7
ujian_tepat_positif 12
ujian_precision 0.8
ujian_recall 0.631578947368421
ujian_skor_latih_dalam 1.0
ujian_skor_uji_dalam 0.8916666666666667
ujian_recall_dalam 0.631578947368421
ujian_selisih_dalam 0.10833333333333328
ujian_selisih_dangkal 0.04761904761904767
ujian_menghafal dalam
ujian_model_dipilih dangkal
ujian_metrik_dipilih recall
ujian_nama_kebocoran data leakage
ujian_rata_boleh data latih
```
