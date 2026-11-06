# Modul 6b: Pipeline

**Tujuan belajar:** Merangkai penskalaan, encoding, dan model menjadi satu `Pipeline`, dengan `ColumnTransformer` untuk kolom yang jenisnya beda. Rantai itu hanya belajar dari data latih, dan memberi tebakan yang sama bila diulang.

**Tingkat:** advanced

Ini bagian kedua modul 6. Bagian pertama, [rekayasa fitur](../modul-06a-rekayasa-fitur/), memperkenalkan fitur, encoding, dan penskalaan. Istilah itu dipakai lagi di sini dengan arti yang sama, bukan istilah baru.

## Cerita pembuka

Di dapur, kartu resep mengunci urutan: setel timbangan dari bahan latihan, ubah tulisan bumbu jadi tanda, baru masak. Kalau jatah tamu ikut menyetel timbangan, lalu kamu pura-pura tamu itu belum datang, timbangannya sudah curang.

Modul ini menuliskan urutan itu sebagai satu rantai. Rantai yang sama, diulang, memberi hasil yang sama. Datanya kita buat sendiri di notebook. Tidak ada yang diunduh. Ini bukan data asli perusahaan.

## Teori

Di bagian ini ada dua istilah baru: Pipeline dan ColumnTransformer.

Encoding, istilah bagian rekayasa fitur: mengubah kategori, yaitu teks berlabel terbatas, menjadi angka supaya model bisa menghitung. Penskalaan, istilah yang sama: mengubah angka sebuah kolom supaya rentangnya sebanding dengan kolom lain, memakai rata-rata dan sebaran yang dihitung hanya dari data yang boleh dilihat.

Model adalah cara menebak yang belajar dari data latih. Label adalah jawaban yang ingin ditebak pada tiap baris, misalnya kolom `kembali`. Itu berbeda dari teks berlabel pada encoding, yaitu nama kategori seperti panas atau dingin. Regresi logistik adalah model yang menebak salah satu dari dua label. Namanya dari modul klasifikasi. Di sini ia hanya berdiri di ujung rantai.

`fit` artinya langkah itu belajar dari data latih. `transform` artinya langkah yang sudah belajar mengubah data, tanpa belajar ulang. Praolah adalah sebutan untuk langkah yang mengubah data sebelum model.

Gambar dulu, tiga gelas latih dan satu gelas yang disisihkan:

```
latih    200    50    180
uji      40
```

Gelas 40 tidak boleh ikut menyetel rata-rata.

### Pipeline

Kartu resep urutannya tetap. Timbangan disetel dari bahan latihan. Jatah tamu tidak ikut menyetel.

Nama teknisnya **Pipeline**: satu rantai langkah berurutan. Langkah di depan mengubah data, langkah terakhir biasanya model. Saat belajar, setiap langkah hanya melihat data latih, lalu langkah itu dipakai apa adanya pada data uji.

Perumpamaan: seperti kartu resep.

**Batas analogi:** Pipeline tidak memilih resep yang benar. Urutan yang salah tetap jalan selama bentuk langkahnya sah. Pipeline tidak membuat tebakan menjadi bagus. Ia tidak memperbaiki kebocoran yang sudah terjadi di luar rantai, sebelum data dibagi. Langkah selain yang terakhir harus bisa mengubah data. Kartu resep tidak menjelaskan isi tiap langkah.

Data leakage, istilah modul evaluasi: informasi yang seharusnya tidak tersedia saat model belajar ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan. Di modul ini yang kita ukur langsung adalah rata-rata di dalam rantai. Rata-rata itu tidak sama dengan rata-rata seluruh kolom. Kita tidak mengklaim skornya otomatis lebih jujur hanya dari selisih rata-rata; yang ditunjukkan adalah data uji tidak ikut menyetel timbangan.

### ColumnTransformer

Dua wajan di meja yang sama. Kolom angka ditimbang di wajan kiri. Kolom kategori diubah menjadi saklar di wajan kanan. Keduanya lalu ditaruh di satu piring.

Nama teknisnya **ColumnTransformer**: satu langkah yang menerapkan cara ubah berbeda pada kelompok kolom berbeda, lalu menyambung hasilnya menjadi satu tabel angka.

Perumpamaan: seperti dua wajan, lalu satu piring.

**Batas analogi:** ColumnTransformer tidak mengerti arti kolom. Kolom teks yang masuk ke penskalaan gagal. Kolom yang tidak disebut dibuang bila `remainder='drop'`, dan itu nilai bawaannya. Ia tidak menggantikan Pipeline; ia biasanya menjadi salah satu langkah di dalam Pipeline. Gambar wajan tidak menjelaskan urutan kolom pada hasil sambungan.

## Coba sendiri dulu, baru kode

Pakai gambar tiga gelas latih: 200, 50, dan 180. Gelas uji: 40.

1. Bolehkah 40 ikut menyetel rata-rata?
2. Berapa jumlah tiga gelas latih?
3. Berapa rata-ratanya?

Hitung dengan tangan. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`.

## Kasus nyata

Notebook membuat empat puluh baris di memori dengan pengacak yang dikunci `SEED`. Tidak ada unduhan. Ini bukan data asli perusahaan.

Kolomnya: `gelas_ml` (angka), `suhu` (tulisan panas atau dingin), `catatan_pinggir` (coretan yang sama pada setiap baris), dan `kembali` (label). Aturan main yang kita tanam: label berisi ya bila gelas di bawah 100 mililiter.

ColumnTransformer menskalakan `gelas_ml`, mengubah `suhu` dengan one-hot, dan membuang `catatan_pinggir`. Pipeline menaruh penggabung itu di depan, regresi logistik di belakang, lalu belajar hanya dari data latih. `random_state=SEED` mengunci undian pada pembagian baris dan pada model. `random_state` adalah tombol undian.

## Kesalahan yang paling sering terjadi

1. Mengubah seluruh tabel di luar Pipeline, termasuk data uji, lalu hanya memasukkan model ke dalam rantai. Kebocoran sudah terjadi sebelum rantai jalan. Pipeline tidak menghapus langkah yang sudah kamu lakukan di luar.
2. Lupa menyebut kolom yang dipakai. Dengan `remainder='drop'`, kolom itu hilang. Coretan memang sengaja dibuang. Kolom yang dipakai model tidak boleh ikut terbuang.
3. Menaruh penskalaan pada kolom teks. Langkahnya gagal karena teks tidak punya rata-rata.
4. Menaruh model di depan pengubah data. Langkah sebelum terakhir harus bisa mengubah tabel. Regresi logistik tidak melakukan itu, jadi urutan itu tidak sah.
5. Kategori baru muncul di data uji, sementara OneHotEncoder masih pada nilai bawaan. Langkahnya berhenti dengan `ValueError`. `ValueError` adalah tanda bahwa isi yang masuk tidak diterima.
6. Mengira tebakan yang sama saat diulang berarti tebakan itu benar. Sama hanya berarti rantainya stabil. Pada tabel main, tebakan uji cocok 10 dari 10 karena aturannya kita yang menanam. Pada kunci latihan, tebakan berulang tetapi hanya 1 dari 2 yang cocok. Angka itu disalin dari keluaran, bukan dari ingatan.
7. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Paket adalah kumpulan kode siap pakai yang dipasang ke proyek. uv adalah perkakas yang memasang paket sesuai berkas kunci di root repo. Pustaka adalah paket yang kita panggil dari kode, misalnya pandas.

`SEED` adalah angka tetap yang mengunci undian. Sel pertama setiap notebook berisi `SEED = 42`. Setiap `random_state` memakai `SEED`.

Indeks adalah nomor baris, mulai dari 0.

Restart & Run All menjalankan semua sel dari sel pertama, tanpa ada yang dilewati.

Versi Python mengikuti berkas `.python-version`. Catatan versinya ada di [dokumen kontribusi](../../docs/CONTRIBUTING.md), bukan di modul ini. CPU only.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`.

## Cek pemahaman

1. Sebutkan dua istilah baru bagian ini, masing-masing dalam satu kalimat sesuai artinya.
2. Bolehkah gelas 40 ikut menyetel rata-rata? Berapa jumlah dan rata-rata tiga gelas latih menurut keluaran?
3. Apakah `catatan_pinggir` ada di nama kolom hasil ColumnTransformer?
4. Apakah dua kali menjalankan rantai yang sama memberi tebakan yang sama?
5. Apakah rata-rata di dalam rantai sama dengan rata-rata seluruh kolom `gelas_ml`?
6. Pada tabel main, tebakan uji cocok 10 dari 10. Apakah itu bukti model selalu benar di luar tabel ini?

### Kunci jawaban

1. **Pipeline:** satu rantai langkah berurutan. Langkah di depan mengubah data, langkah terakhir biasanya model. Saat belajar, setiap langkah hanya melihat data latih, lalu langkah itu dipakai apa adanya pada data uji. **ColumnTransformer:** satu langkah yang menerapkan cara ubah berbeda pada kelompok kolom berbeda, lalu menyambung hasilnya menjadi satu tabel angka.
2. Tidak boleh. Jumlah tiga gelas latih `430`. Rata-ratanya `143.33333333333334`.
3. Tidak. Keluaran `ada_catatan False`. Nama kolom hasil hanya `angka__gelas_ml`, `kategori__suhu_dingin`, dan `kategori__suhu_panas`.
4. Ya. Keluaran `sama True`.
5. Tidak. `rata_dalam_rantai 128.16666666666666`, `rata_semua 130.55`, `beda True`.
6. Tidak. Aturan "gelas di bawah 100" kita yang menanam di tabel main. Cocok 10 dari 10 hanya berlaku untuk tabel itu. Kunci latihan, pada tabel yang lebih kecil, mencetak `cocok 1` dan `dari 2`.

Jawaban "coba sendiri" ada di keluaran: gelas 40 tidak ikut, jumlah 430, rata-rata 143.33333333333334.

### Angka yang disalin dari keluaran notebook

Dari `notebook.ipynb`:

```
jumlah_latih 430
rata_latih 143.33333333333334
n_baris 40
n_latih 30
n_uji 10
langkah ['praolah', 'model']
tebakan ['tidak', 'tidak', 'tidak', 'tidak', 'tidak', 'tidak', 'tidak', 'tidak', 'tidak', 'ya']
sama True
nama_fitur ['angka__gelas_ml', 'kategori__suhu_dingin', 'kategori__suhu_panas']
ada_catatan False
rata_dalam_rantai 128.16666666666666
rata_semua 130.55
beda True
cocok 10
dari 10
```

Dari `latihan-kunci.ipynb`:

```
jumlah_latih 90
rata_latih 30.0
rata_empat 40.0
beda True
tebakan ['ya', 'ya']
sama True
nama_fitur ['angka__gelas_ml', 'kategori__suhu_dingin', 'kategori__suhu_panas']
ada_catatan False
cocok 1
dari 2
error True
```

Latihan 1 memakai 10, 30, 50, dan 70. Jumlah tiga angka pertama 90. Rata-ratanya 30.0. Rata-rata empat angka itu 40.0, jadi angka 70 tidak boleh ikut. Array latihan menyimpan delapan nilai: 10, 30, 50, 70, 90, 110, 130, dan 150. Empat gelas pada latihan 1 adalah empat nilai pertama array itu. Latihan 2 dan 3 memakai kedelapan nilai. Coretan tidak ikut (`ada_catatan False`). Dua kali jalan memberi tebakan yang sama, yaitu `['ya', 'ya']`, tetapi hanya 1 dari 2 yang cocok dengan label uji. Tulisan "hangat" yang tidak ada saat belajar membuat langkah berhenti (`error True`).

## Sumber

- scikit-learn developers. *8.1. Pipelines and composite estimators.* <https://scikit-learn.org/stable/modules/compose.html>
- scikit-learn developers. *sklearn.pipeline.Pipeline.* <https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html>
- scikit-learn developers. *sklearn.compose.ColumnTransformer.* <https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html>
- scikit-learn developers. *sklearn.linear_model.LogisticRegression.* <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., dan Duchesnay, É. "Scikit-learn: Machine Learning in Python." Journal of Machine Learning Research, 12(85):2825–2830, 2011. <https://jmlr.org/papers/v12/pedregosa11a.html>
