# Modul 7: Tanpa label

**Tujuan belajar:** Mengelompokkan baris tanpa kolom jawaban, merangkum banyak kolom angka menjadi lebih sedikit, dan menandai baris yang jauh dari mayoritas.

**Tingkat:** advanced

**Issue:** #7

Modul ini menutup tingkat advanced. Di modul ini hanya ada tiga istilah baru: clustering, PCA, dan deteksi anomali.

## Cerita pembuka

Kamu membuka laci kaus. Tidak ada tulisan nama pemilik.

Kaus yang panjang dan lebarnya mirip kamu kumpulkan jadi satu tumpukan. Beberapa kaus punya banyak catatan angka sekaligus: panjang, lebar, tebal, dan berat. Supaya tidak pusing, kamu ingin dua angka ringkas yang tetap menyimpan sebagian besar perbedaan antar kaus. Lalu ada satu kaus bolong. Ukurannya tidak mirip tumpukan mana pun. Kamu sisihkan untuk dilihat, bukan dipaksa masuk tumpukan.

Modul ini belajar tiga hal itu pada angka kecil. Bukan data asli perusahaan. Tidak ada berkas yang diunduh.

## Teori

Pustaka adalah kumpulan fungsi siap pakai. Paket adalah program tambahan yang dipasang ke Python. scikit-learn adalah paket yang berisi alat modul ini. Indeks adalah nomor baris, mulai dari 0.

Gambar dulu. Empat titik, sumbu mendatar x dan sumbu tegak y:

```
y
9 |           D
8 |         C
2 | B
1 | A
  +------------- x
    1         8 9
```

A di (1, 1), B di (1, 2), C di (8, 8), D di (9, 8). Kelompoknya kamu tentukan sendiri di bagian "coba sendiri".

### clustering

Mengumpulkan yang mirip, tanpa label nama pemilik, itulah **clustering**: membagi catatan menjadi beberapa kelompok berdasarkan kemiripan kolom angka, tanpa memakai kolom jawaban.

Perumpamaan: seperti memisahkan cucian berdasarkan warna dan jenis kain, tanpa label nama pemilik.

**Batas analogi:** pada KMeans jumlah kelompok harus disebut dari awal, sedangkan tumpukan cucian boleh bertambah sendiri. Kemiripan diukur dengan kuadrat jarak angka, bukan dengan mata, dan nama kelompok tidak keluar dari metode. Kelompok yang panjang atau melengkung bisa gagal terpotong rapi.

KMeans adalah satu cara clustering, bukan istilah baru: tiap titik ditaruh ke pusat terdekat, pusat digeser ke rata-rata anggotanya, lalu langkah itu diulang. `n_init` adalah berapa kali pusat awal dicoba. Kita tulis 10 supaya angka itu tidak mengikuti bawaan yang bisa berubah.

Rumus sesudah gambar. Tanda ^2 artinya dikali dirinya. Di kode, pangkat ditulis `**`.

`kuadrat = (selisih x)^2 + (selisih y)^2`

A ke B dan A ke C kamu hitung sendiri di bagian berikutnya. Notebook mencetak hasilnya. KMeans membandingkan kuadrat jarak ini, bukan akarnya. Akar hanya supaya jarak lurusnya kelihatan.

### PCA

Banyak kolom angka yang bergerak bersama bisa diringkas. Nama teknisnya **PCA**: merangkum banyak kolom angka menjadi lebih sedikit kolom baru yang tetap menyimpan sebagian besar variasi. Kependekan ini dari principal component analysis. Dalam bahasa Indonesia sering disebut analisis komponen utama. Itu satu istilah, bukan dua.

Perumpamaan: seperti merangkum nota belanja menjadi dua kolom baru dari pola angkanya, bukan dari judul yang kamu pilih lebih dulu.

**Batas analogi:** dua kolom baru itu bukan judul nota yang lama, dan bukan nama yang kamu tentukan di muka. PCA tidak mengurangi jumlah baris, tidak membagi kelompok, dan tidak menandai baris aneh. Pada scikit-learn, PCA menggeser kolom ke rata-rata nol tetapi tidak menyamakan sebaran, jadi kolom berangka besar bisa menelan yang lain bila belum diskalakan.

`explained_variance_ratio_` adalah bagian variasi yang tersimpan di tiap kolom baru. Bukan istilah kamus.

### deteksi anomali

Satu kaus bolong tidak harus menjadi tumpukan baru. Nama teknisnya **deteksi anomali**: menandai catatan yang jauh dari pola mayoritas.

Perumpamaan: seperti menemukan satu kaus yang bolong di antara tumpukan kaus yang utuh.

**Batas analogi:** satu kaus bolong tetap satu barang untuk diperiksa, bukan kelompok baru. Modul ini memakai outlier detection: baris aneh sudah tercampur di tabel yang dipelajari, baris biasa ditandai 1, baris aneh ditandai -1. Ini bukan novelty detection, yaitu memeriksa barang baru pada tabel belajar yang dianggap bersih. Ambang jauh bergantung pada `contamination`, perkiraan bagian baris aneh. Tanda ini bukan penyebab kerusakan. Outlier detection, novelty detection, dan contamination bukan istilah baru.

IsolationForest adalah satu alat untuk deteksi anomali, bukan istilah baru: baris yang mudah dipisahkan dari mayoritas ditandai aneh.

## Coba sendiri dulu, baru kode

1. Pada gambar empat titik, mana yang sekelompok?
2. Berapa kuadrat jarak A ke B, dan A ke C?
3. Enam titik berurutan: (0, 0), (0, 1), (1, 0), (8, 8), (8, 9), (20, 0). Indeks mana yang jauh sendirian? Kalau dipaksa menjadi dua kelompok, apakah titik itu jadi kelompok sendiri?

Hitung dengan tangan. Baru buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

Kita membaca dataset bunga iris lewat `sklearn.datasets.load_iris`. Dokumentasi scikit-learn menyatakan dataset mainan ini tidak perlu diunduh: berkasnya sudah ikut terpasang. Modul ini tidak memakai data asli perusahaan.

Ada empat ukuran bunga. Kolom spesies tidak ikut, karena itu kolom jawaban. Jumlah kelompok 2 kita pilih untuk dicoba pada seluruh tabel. Tidak ada baris yang ditahan di kasus ini, jadi ini merangkum tabel, bukan ujian kebocoran.

PCA pada tabel yang sama menyimpan dua kolom baru. Scaler berada di dalam Pipeline supaya sebaran kolom disamakan dulu. `fit` artinya langkah itu belajar dari baris yang diberikan. Pipeline, dari modul 6b, adalah satu rantai langkah berurutan. Langkah di depan mengubah data, langkah terakhir biasanya model. Saat belajar, setiap langkah hanya melihat data latih, lalu langkah itu dipakai apa adanya pada data uji. Kalimat ini mengingatkan arti di modul 6b, bukan arti baru.

## Kesalahan yang paling sering terjadi

1. Memasukkan kolom jawaban, misalnya spesies, sebagai kolom angka. Itu data leakage: informasi yang seharusnya tidak tersedia saat belajar ikut terpakai. Di modul ini kita tidak mengukur skor ketepatan. Kebocorannya tetap, karena kolom yang tidak boleh ikut sudah ikut. Akibat yang disebut di kamus, skor terlihat lebih bagus dari kenyataan, bisa terjadi bila seseorang lalu membandingkan kelompok dengan spesies yang sudah ikut sebagai kolom.
2. Mengira clustering otomatis menandai titik yang jauh. Pada enam titik, titik jauh ikut kelompok titik di sekitar (8, 8). IsolationForest yang menandainya, bukan clustering.
3. Mengira PCA mengurangi jumlah baris. Baris tetap. Yang berkurang kolom.
4. Memasang scaler di luar Pipeline pada semua baris, termasuk data uji, baru kemudian memotong. Scaler sudah melihat baris yang seharusnya ditahan.
5. Memilih jumlah kelompok dengan mengintip kolom jawaban, lalu merasa kelompok itu "benar" karena namanya cocok.
6. Menjalankan sel dari bawah, atau lupa `SEED`, lalu menyalin angka dari ingatan.

## Cara menjalankan

uv adalah program yang memasang paket sesuai daftar terkunci di root repo. Daftar itu ada di `uv.lock`. Folder `.venv` adalah lingkungan terpasangnya. Jangan membuat `pyproject.toml` baru di samping notebook.

Notebook adalah berkas yang mencampur penjelasan dan satu potong kode. Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian lewat `random_state=SEED`, supaya hasil yang memakai undian bisa diulang.

`fit` artinya langkah itu belajar dari baris yang diberikan. `predict` artinya langkah yang sudah belajar memberi hasil pada baris lain.

Perintah ini dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`), bukan dari folder modul:

```bash
uv sync --frozen
uv run pytest --nbmake
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Ujian ada di `ujian.ipynb` dan `ujian-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

CPU only.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. KMeans boleh menambah jumlah kelompok sendiri bila ada titik yang jauh. Benar atau salah?
3. Pada enam titik, apakah titik jauh menjadi kelompok sendiri menurut clustering? Menurut deteksi anomali?
4. PCA mengurangi jumlah baris. Benar atau salah?
5. Mengapa kolom spesies tidak ikut pada tabel iris?
6. Untuk apa `SEED = 42`?

### Kunci jawaban

1. **clustering:** membagi catatan menjadi beberapa kelompok berdasarkan kemiripan kolom angka, tanpa memakai kolom jawaban. **PCA:** merangkum banyak kolom angka menjadi lebih sedikit kolom baru yang tetap menyimpan sebagian besar variasi. **deteksi anomali:** menandai catatan yang jauh dari pola mayoritas.
2. Salah. Jumlah kelompok harus disebut dari awal.
3. Menurut clustering, tidak: baris `aneh_ikut_delapan` pada keluaran bernilai True, artinya titik jauh ikut kelompok di sekitar (8, 8). Menurut deteksi anomali, ya: baris `indeks_aneh` menunjuk satu baris, dan `hanya_satu` True.
4. Salah. `baris_awal` dan `baris_baru` pada keluaran sama. Yang berubah adalah kolom.
5. Karena spesies adalah kolom jawaban. Memasukkannya membuat kelompok mengulang jawaban itu.
6. Supaya setiap undian di notebook ini memakai angka tetap yang sama, dan hasil yang bergantung pada undian bisa diulang.

Jawaban "coba sendiri": A dengan B, dan C dengan D. Itu terlihat pada `sama_AB`, `sama_CD`, dan `berbeda`. Kuadrat jarak ada pada `kuadrat_dekat` dan `kuadrat_jauh`. Titik jauh pada enam titik adalah baris `indeks_aneh`, tetapi clustering tidak menaruhnya sendiri.

### Angka yang disalin dari keluaran notebook

Dari `notebook.ipynb`:

```
kuadrat_dekat 1
kuadrat_jauh 98
akar_jauh 9.899494936611665
label [0, 0, 1, 1]
sama_AB True
sama_CD True
berbeda True
sama True
baris 150
kolom 4
nama ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
ukuran 0 100
ukuran 1 50
variasi_1 0.729624454132999
variasi_2 0.2285076178670174
variasi_tersimpan 0.9581320720000164
baris_awal 150
baris_baru 150
kolom_awal 4
kolom_baru 2
label_kelompok [1, 1, 1, 0, 0, 0]
sama_dekat_nol True
sama_dekat_delapan True
aneh_ikut_delapan True
label_aneh [1, 1, 1, 1, 1, -1]
indeks_aneh 5
hanya_satu True
```

Dari `latihan-kunci.ipynb`:

```
label_kelompok [1, 1, 1, 0, 0, 0]
sama_dekat_nol True
sama_dekat_delapan True
aneh_ikut_delapan True
label_aneh [1, 1, 1, 1, 1, -1]
indeks_aneh 5
hanya_satu True
nama ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
jumlah_kolom 4
ada_spesies False
baris_awal 150
baris_baru 150
kolom_awal 4
kolom_baru 2
baris_tetap True
siap True
```

## Ujian tingkat advanced

Modul 6 dan modul 7 satu tingkat. Ujian ini yang menutupnya. Kalimat kriteria dari roadmap:

Satu Pipeline lengkap dari data mentah sampai hasil, bebas data leakage, dan memberi hasil yang sama setiap kali diulang.

### Mini-proyek

Bahan di `ujian.ipynb`: generator `make_blobs` membuat angka di memori. Pemanggilan di notebook memakai `n_samples=120`, `centers=3`, dan `n_features=2`, lalu `test_size=0.25` menahan sebagian baris. Banyak baris yang tercetak ada di keluaran, bukan dijumlah dengan tangan. Bukan unduhan. Bukan data asli perusahaan. Nomor gumpalan dari generator dibuang, tidak menjadi kolom. Data uji adalah bagian yang ditahan. Data latih dipakai untuk belajar. Data uji disisihkan dan tidak dilihat saat belajar. Di ujian ini tidak ada kolom jawaban untuk diukur, jadi data uji dipakai agar Pipeline memberi label pada baris baru, dan agar scaler bisa diperiksa tidak melihat baris itu.

Yang dibangun:

1. Satu Pipeline. Langkah `skala` adalah StandardScaler. Langkah `kelompok` adalah KMeans, 3 kelompok, `n_init=10`, `random_state=SEED`.
2. Masukan berupa angka mentah. Scaler tidak di-fit pada seluruh baris di luar Pipeline.
3. `fit` hanya pada data latih. `predict` pada data uji.

StandardScaler menggeser tiap kolom supaya rata-ratanya 0 dan sebarannya 1. `n_samples_seen_` adalah banyak baris yang dilihat scaler saat belajar. `train_test_split` memotong baris menjadi data latih dan data uji dengan undian yang dikunci `random_state`.

### Pertanyaan ujian

1. Sebutkan tiga syarat lulus mini-proyek ini.
2. Scaler di dalam Pipeline melihat semua baris, termasuk data uji. Benar atau salah?
3. Nomor kelompok dari generator boleh menjadi kolom masukan. Benar atau salah?
4. Dua Pipeline yang dibuat terpisah dengan `random_state=SEED` pada data latih yang sama memberi label data uji yang sama. Benar atau salah?
5. Deteksi anomali membagi semua baris menjadi kelompok yang sama rata. Benar atau salah?

### Kriteria lulus

Mini-proyek lulus bila ketiga hal ini benar, dicek di `ujian-kunci.ipynb`:

1. Ada satu Pipeline dari angka mentah sampai label kelompok. Nama langkahnya `skala` lalu `kelompok`.
2. Bebas data leakage: `n_samples_seen_` pada scaler sama dengan jumlah baris data latih, bukan jumlah seluruh baris. Nomor kelompok generator tidak menjadi kolom. Kolom masukan tetap 2.
3. Hasil sama setiap diulang: dua Pipeline baru dengan `random_state=SEED` memberi label data uji yang sama.

Pertanyaan lulus bila kelima jawaban sama dengan kunci di bawah.

Ujian tingkat advanced lulus bila mini-proyek lulus dan semua pertanyaan ujian sesuai kunci. Tiga baris `lulus_*` pada keluaran adalah hasil cek kunci ini, bukan keputusan Ursa atau Squal.

### Kunci jawaban ujian

1. Pipeline lengkap dari angka mentah sampai label kelompok; scaler hanya melihat data latih; dua kali dijalankan dengan `SEED` yang sama memberi label data uji yang sama.
2. Salah. Bandingkan `sampel_skala` dengan `sampel_skala_keliru` pada keluaran. Yang di dalam Pipeline sama dengan `baris_latih`. Yang keliru sama dengan seluruh baris.
3. Salah. Nomor itu dibuang. `kolom_masukan` pada keluaran tetap 2.
4. Benar. Baris `sama` dan `lulus_ulang` pada keluaran True.
5. Salah. Deteksi anomali menandai yang jauh dari mayoritas, bukan membagi semua baris menjadi kelompok rata.

### Angka yang disalin dari keluaran ujian

Dari `ujian-kunci.ipynb`:

```
baris_latih 90
baris_uji 30
kolom 2
nama_langkah ['skala', 'kelompok']
sampel_skala 90
kolom_masukan 2
sama True
sampel_skala_keliru 120
lulus_pipeline True
lulus_tanpa_bocor True
lulus_ulang True
```

## Sumber

- scikit-learn developers. *K-means*. <https://scikit-learn.org/stable/modules/clustering.html#k-means>
- scikit-learn developers. `sklearn.cluster.KMeans`. <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>
- Arthur, David, dan Vassilvitskii, Sergei. "k-means++: The advantages of careful seeding." Proceedings of the eighteenth annual ACM-SIAM symposium on Discrete algorithms, Society for Industrial and Applied Mathematics (2007). Kalimat ini mengikuti bagian referensi K-means pada panduan scikit-learn.
- scikit-learn developers. *Principal component analysis (PCA)*. <https://scikit-learn.org/stable/modules/decomposition.html#pca>
- scikit-learn developers. `sklearn.decomposition.PCA`. <https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html>
- Pearson, K. (1901). "On Lines and Planes of Closest Fit to Systems of Points in Space." Philosophical Magazine, 2(11), 559-572. doi:10.1080/14786440109462720.
- Hotelling, H. (1933). "Analysis of a complex of statistical variables into principal components." Journal of Educational Psychology, 24, 417-441 dan 498-520.
- scikit-learn developers. *Isolation Forest*. <https://scikit-learn.org/stable/modules/outlier_detection.html#isolation-forest>
- scikit-learn developers. `sklearn.ensemble.IsolationForest`. <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html>
- Liu, F. T., Ting, K. M., dan Zhou, Z.-H. "Isolation forest." 2008 Eighth IEEE International Conference on Data Mining (ICDM), 2008, pp. 413-422. Kalimat ini mengikuti bagian Isolation Forest pada panduan scikit-learn.
- scikit-learn developers. `sklearn.pipeline.Pipeline`. <https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html> dan *Pipeline*. <https://scikit-learn.org/stable/modules/compose.html#pipeline>
- scikit-learn developers. `sklearn.preprocessing.StandardScaler`. <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>
- scikit-learn developers. `sklearn.datasets.make_blobs`. <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html>
- scikit-learn developers. `sklearn.model_selection.train_test_split`. <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>
- scikit-learn developers. *Toy datasets* (Iris plants dataset) dan `load_iris`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html>
- Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annals of Eugenics, 7, Part II, 179-188 (1936); juga dalam "Contributions to Mathematical Statistics" (John Wiley, NY, 1950). Kalimat sumber ini mengikuti halaman toy dataset scikit-learn, dengan nama jurnal yang sudah dikoreksi.

## Catatan istilah

Hanya tiga entri kamus baru. KMeans, StandardScaler, PCA sebagai nama alat, IsolationForest, Pipeline, `n_init`, `contamination`, outlier detection, dan novelty detection dijelaskan satu kalimat dan tidak menjadi entri. Arti Pipeline sama dengan modul 6b: satu rantai langkah berurutan. Langkah di depan mengubah data, langkah terakhir biasanya model. Saat belajar, setiap langkah hanya melihat data latih, lalu langkah itu dipakai apa adanya pada data uji. Modul 6a dan modul 6b ada di pohon ini. Ujian hanya mengingatkan arti itu, tanpa menambah entri kamus. Modul ini tidak dipecah: tiga topik roadmap tepat tiga istilah.
