# Modul 6a: Rekayasa fitur

**Tujuan belajar:** Mengubah catatan mentah menjadi fitur yang bisa dihitung: kolom baru dari hitungan, encoding untuk tulisan berkategori, dan penskalaan untuk angka. Rata-rata penskalaan hanya diambil dari data latih.

**Tingkat:** advanced

Ini bagian pertama. Bagian kedua, [Pipeline](../modul-06b-pipeline/), merangkai langkah-langkah ini. Penomoran bagian mengikuti urutan belajar.

## Cerita pembuka

Kamu mencatat minuman di rumah. Satu baris, satu gelas: berapa mililiternya, dan tulisan "panas" atau "dingin". Besok kamu ingin menebak apakah gelas itu diminum habis.

Alat hitung hanya mengerti angka. Tulisan "panas" belum bisa dijumlah. Angka 200 dan angka 1 juga tidak sebanding: yang besar menelan yang kecil.

Modul ini mengubah catatan itu supaya alat hitung bisa memakainya. Tabelnya kita buat sendiri di notebook. Tidak ada yang diunduh. Ini bukan data asli perusahaan.

## Teori

Di bagian ini ada tiga istilah baru: fitur, encoding, dan penskalaan. Rekayasa fitur adalah nama pekerjaannya: menyusun fitur. Nama itu dijelaskan di kalimat ini dan belum masuk kamus.

Gambar dulu, empat gelas:

```
gelas_ml    200     50     180     40
suhu        dingin  panas  dingin  panas
```

### fitur

Perumpamaan: bahan yang masuk ke adonan ikut dihitung. Catatan di pinggir kertas, misalnya nama juru masak, tidak ikut diaduk.

Nama teknisnya **fitur**: kolom, atau hasil hitungan dari kolom, yang dipakai model untuk menebak. Kolom jawaban yang ditebak bukan fitur.

**Batas analogi:** tidak semua kolom tabel adalah fitur. Kolom jawaban dan nama baris bukan fitur. Fitur hasil hitungan bisa mengulang informasi yang sudah ada, atau gagal bila pembaginya nol. Gambar adonan tidak menjelaskan bahwa model hanya melihat angka.

Contoh hitungan, setelah gambar di atas. Satu liter sama dengan 1000 mililiter:

`gelas_liter = gelas_ml / 1000`

Hasilnya kamu hitung sendiri di bagian berikutnya. Notebook mencetak hasilnya.

### encoding

Perumpamaan: dua saklar untuk "panas" dan "dingin". Satu menyala, yang lain mati. Bukan termometer.

Nama teknisnya **encoding**: mengubah kategori, yaitu teks berlabel terbatas, menjadi angka supaya model bisa menghitung. Berlabel di sini berarti kategori punya nama, misalnya panas atau dingin, bukan kolom jawaban yang ditebak.

**Batas analogi:** angka 0 dan 1 di sini bukan urutan "lebih panas". Tiga kategori berarti tiga saklar, bukan skala 1 sampai 3. Encoding tidak mengubah kolom yang memang sudah angka. Kategori yang tidak ada saat belajar tidak punya saklar, kecuali caranya disiapkan untuk kategori baru.

Cara di notebook namanya one-hot: satu kolom baru per kategori, berisi 1 jika cocok dan 0 jika tidak. Mengisi satu kolom dengan 0, 1, lalu 2 mengarang urutan. Itu bukan encoding yang kita pakai.

### penskalaan

Perumpamaan: gram dan ons disamakan dulu sebelum beratnya dibandingkan, supaya yang satuannya besar tidak selalu menang.

Nama teknisnya **penskalaan**: mengubah angka sebuah kolom supaya rentangnya sebanding dengan kolom lain, memakai rata-rata dan sebaran yang dihitung hanya dari data yang boleh dilihat.

**Batas analogi:** hasilnya bukan gram dan bukan ons. Tiap angka digeser ke rata-rata nol, lalu dibagi sebarannya. Penskalaan tidak menambah informasi dan tidak cocok untuk kolom teks. Rata-rata dan sebaran hanya dari data latih; kalau data uji ikut, itu data leakage. Kolom yang nilainya semua sama tidak bisa dibagi.

Data latih dipakai untuk belajar. Data uji disisihkan. Pada empat gelas ini skor tidak diukur; yang terlihat hanya rata-ratanya berubah.

Sebaran adalah simpangan baku: seberapa jauh angka tersebar dari rata-rata.

`(angka - rata-rata) / sebaran`

StandardScaler membagi dengan banyaknya data, bukan banyaknya data dikurangi satu. `fit` belajar dari data latih. `transform` mengubah data tanpa belajar ulang. Angka hasilnya ada di keluaran notebook.

## Coba sendiri dulu, baru kode

Pakai gambar empat gelas di atas.

1. Berapa jumlah 200, 50, 180, dan 40?
2. Berapa hasil jumlah itu dibagi 4?
3. 200 mililiter sama dengan berapa liter? Bagi dengan 1000.
4. Baris pertama suhunya dingin. Kalau ada kolom untuk dingin dan kolom untuk panas, berisi 1 atau 0, kolom mana yang berisi 1?

Hitung dengan tangan. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`.

## Kasus nyata

Notebook membuat dua belas baris di memori dengan pengacak yang dikunci `SEED`. Tidak ada unduhan. Ini bukan data asli perusahaan.

Aturan main yang kita tanam: jawaban `kembali` berisi ya bila `gelas_ml` di bawah 100. Kolom itu bukan fitur. Penskalaan pada kasus ini hanya belajar dari data latih, yaitu bagian yang sudah disisihkan oleh pembagian baris.

## Kesalahan yang paling sering terjadi

1. Kategori tanpa urutan diisi 0, 1, 2 pada satu kolom. Jarak antarangka itu karangan.
2. Rata-rata penskalaan dihitung dari seluruh tabel, termasuk data uji. Itu data leakage. Di tabel empat gelas, rata-ratanya berubah. Skor model tidak kita ukur di situ.
3. Kolom jawaban ikut dipakai sebagai fitur. Model lalu "menebak" sesuatu yang sudah ada di tangannya.
4. Fitur baru membagi dengan nol, misalnya mililiter yang isinya 0.
5. Penskalaan dipasang pada kolom teks. Teks tidak punya rata-rata.
6. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Paket adalah kumpulan kode siap pakai yang dipasang ke proyek. uv adalah perkakas yang memasang paket sesuai berkas kunci di root repo. Pustaka adalah paket yang kita panggil dari kode, misalnya pandas.

`SEED` adalah angka tetap yang mengunci undian. Sel pertama setiap notebook berisi `SEED = 42`. Angka itu dipakai pada setiap undian, lewat `random_state=SEED`, supaya pembagian baris yang sama berulang. `random_state` adalah tombol undian itu.

Indeks adalah nomor baris, mulai dari 0.

Restart & Run All menjalankan semua sel dari sel pertama, tanpa ada yang dilewati.

Versi Python mengikuti berkas `.python-version`. Versi paket ada di `uv.lock` di root repo. CPU only.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`.

## Cek pemahaman

1. Sebutkan tiga istilah baru bagian ini, masing-masing dalam satu kalimat sesuai artinya.
2. Apakah kolom `kembali` termasuk fitur?
3. Mengapa one-hot bukan deretan 0, 1, 2 pada satu kolom?
4. Bolehkah rata-rata penskalaan dihitung dari data uji? Sebutkan istilah modul evaluasi yang dilanggar bila itu dilakukan.
5. Pada tabel empat gelas, berapa jumlah dan rata-ratanya menurut keluaran notebook?
6. Apa isi encoding baris pertama data latih, dan apa isi baris uji?
7. Apakah rata-rata tiga gelas latih sama dengan rata-rata empat gelas?

### Kunci jawaban

1. **fitur:** kolom, atau hasil hitungan dari kolom, yang dipakai model untuk menebak. Kolom jawaban yang ditebak bukan fitur. **encoding:** mengubah kategori, yaitu teks berlabel terbatas, menjadi angka supaya model bisa menghitung. **penskalaan:** mengubah angka sebuah kolom supaya rentangnya sebanding dengan kolom lain, memakai rata-rata dan sebaran yang dihitung hanya dari data yang boleh dilihat.
2. Tidak. Kolom jawaban bukan fitur. Keluaran menuliskan `kolom_jawaban kembali`.
3. Karena 0, 1, 2 mengarang urutan dan jarak. One-hot membuat satu kolom per kategori, 1 jika cocok dan 0 jika tidak.
4. Tidak boleh. Itu data leakage: informasi yang seharusnya tidak tersedia saat belajar ikut terpakai.
5. Jumlah `470`, rata-rata `117.5`, disalin dari keluaran di bawah.
6. Baris latih pertama `[1.0, 0.0]` pada kolom `suhu_dingin` lalu `suhu_panas`. Baris uji `[0.0, 1.0]`.
7. Tidak sama. Rata-rata latih `143.33333333333334`, rata-rata empat gelas `117.5`, dan `beda True`.

Jawaban "coba sendiri": jumlah 470, rata-rata 117.5, 200 mililiter menjadi 0.2 liter, dan kolom dingin yang berisi 1 pada baris pertama. Semuanya ada di keluaran di bawah, bukan dihitung ulang di teks ini.

### Angka yang disalin dari keluaran notebook

Dari `notebook.ipynb`:

```
jumlah 470
rata_rata 117.5
liter [0.2, 0.05, 0.18, 0.04]
urutan_palsu [0, 1, 0, 1]
baris_latih [0, 1, 2]
baris_uji [3]
nama_latih ['suhu_dingin', 'suhu_panas']
kode_latih_pertama [1.0, 0.0]
kode_uji [0.0, 1.0]
rata_latih 143.33333333333334
sebaran_latih 66.4997911442
uji_skala -1.5538895920629654
rata_semua 117.5
beda True
kolom_fitur ['gelas_ml', 'suhu']
kolom_jawaban kembali
n_latih 9
n_uji 3
kasus_rata_latih 137.77777777777777
kasus_rata_semua 121.91666666666667
kasus_beda True
```

Dari `latihan-kunci.ipynb`:

```
jumlah 260
rata_rata 65.0
nama ['suhu_dingin', 'suhu_panas']
baris_pertama [0.0, 1.0]
rata_latih 66.66666666666667
rata_semua 65.0
beda True
liter 0.1
```

Latihan memakai angka lain: 100, 20, 80, dan 60. Jumlahnya 260. Rata-ratanya 65.0. Baris pertama suhunya panas, jadi encoding-nya `[0.0, 1.0]` pada kolom dingin lalu panas. Rata-rata tiga angka pertama 66.66666666666667, bukan rata-rata empat angka 65.0. 100 mililiter sama dengan 0.1 liter.

## Sumber

- scikit-learn developers. *8.3. Preprocessing data.* <https://scikit-learn.org/stable/modules/preprocessing.html>
- scikit-learn developers. *sklearn.preprocessing.OneHotEncoder.* <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html>
- scikit-learn developers. *sklearn.preprocessing.StandardScaler.* <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., dan Duchesnay, É. "Scikit-learn: Machine Learning in Python." Journal of Machine Learning Research, 12(85):2825–2830, 2011. <https://jmlr.org/papers/v12/pedregosa11a.html>
