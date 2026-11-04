# Modul 1: Persiapan

**Tujuan belajar:** Menyiapkan meja kerja Python yang bisa diulang, lalu membaca angka sebagai array dan tabel sebagai DataFrame.

**Tingkat:** beginner

## Cerita pembuka

Kamu menimbang bahan kue. Kalau timbangannya berganti-ganti, atau catatannya tercampur dengan catatan dapur lain, besok hasilnya beda walaupun resepnya sama.

Modul ini menata meja kerja supaya langkah yang sama bisa diulang. Kita memakai Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), memasang perkakas di satu tempat yang terpisah dari proyek lain, dan menulis catatan yang mencampur penjelasan dengan kode. Setelah meja siap, kita latihan memegang angka dan tabel. Contoh tabelnya sudah ikut terpasang bersama scikit-learn. Tidak ada berkas yang diunduh. Modul ini tidak memakai data asli perusahaan.

## Teori

Di modul ini hanya ada tiga istilah baru. Notebook, Git, dan angka tetap `SEED` dijelaskan dengan bahasa biasa dan belum masuk kamus.

### venv

Kalau semua proyek berbagi satu tumpukan paket, versi paket bisa tertukar. Besok kode yang sama bisa gagal karena paketnya berubah.

Bayangkan kotak perkakas berlabel untuk satu pekerjaan. Isinya tidak tercampur dengan kotak pekerjaan lain. Nama teknisnya **venv**: lingkungan terpisah yang menyimpan pemasangan paket Python untuk satu proyek, supaya versi paket proyek ini tidak tertukar dengan proyek lain.

**Batas analogi:** kotak perkakas tidak menyimpan catatan atau bahan. venv juga tidak menyimpan notebook, data, atau riwayat perubahan berkas. Menghapus folder `.venv` tidak menghapus kode. venv tidak mengunci seluruh lingkungan sendirian; daftar versi yang terkunci ada di `uv.lock`. Kita membuat venv dan memasang paket dengan uv, mengikuti berkas kunci itu.

### array

Gambar dulu. Empat tinggi tanaman, dalam sentimeter:

```
5    7    6    6
```

Isinya sejenis, jadi seluruh baris bisa dijumlahkan sekaligus. Nama teknisnya **array**: kumpulan nilai sejenis dengan bentuk yang tetap, yang dihitung sekaligus.

Perumpamaan: seperti nampan telur. Setiap lubang berisi satu butir yang sejenis, jadi seluruh nampan bisa dijumlahkan sekaligus.

**Batas analogi:** berhenti berlaku bila nilai tidak sejenis, misalnya angka campur teks. Nampan menggambarkan satu baris atau satu kisi; array bisa punya lebih dari dua dimensi. Gambar ini juga tidak menjelaskan hitungan antara dua array yang bentuknya berbeda.

Rumus rata-rata, setelah gambar di atas, dengan angka yang sama:

`rata-rata = (5 + 7 + 6 + 6) / 4`

Hasil baginya kamu hitung sendiri di bagian berikutnya. Notebook mencetak hasilnya; kunci di bawah menyalin cetakan itu.

### DataFrame

Buku kas punya judul kolom di atas dan satu baris untuk satu catatan. Nama teknisnya **DataFrame**. Artinya: tabel di memori: setiap kolom punya nama, setiap baris satu catatan.

Perumpamaan: seperti halaman buku kas.

**Batas analogi:** bukan spreadsheet. Mengubah satu kolom tidak memperbarui kolom lain secara otomatis. Urutan baris bukan urutan waktu, kecuali datanya memang disusun begitu. Menutup program tanpa menyimpan berkas tidak meninggalkan tabel di disk. Kalau satu kolom dicampur angka dan teks, rata-rata kolom itu bisa gagal.

## Coba sendiri dulu, baru kode

Pakai empat angka pada gambar di atas: 5, 7, 6, dan 6.

1. Berapa jumlahnya?
2. Berapa hasil `(5 + 7 + 6 + 6) / 4`?

Hitung dengan tangan dulu. Jangan gulir ke kunci. Setelah itu buka `notebook.ipynb`. Sel pertama hanya menyimpan `SEED`. Sel hitungan ada di bawahnya.

## Kasus nyata

Kita membaca dataset bunga iris lewat `sklearn.datasets.load_iris`. Dokumentasi scikit-learn menyatakan dataset mainan ini tidak perlu diunduh dari situs lain: berkasnya sudah ikut terpasang. Modul ini tidak memakai data asli perusahaan.

Ada empat ukuran (panjang dan lebar kelopak pelindung, panjang dan lebar mahkota) plus jenis bunganya. Notebook memasukkan angka itu ke DataFrame, menghitung rata-rata satu kolom, lalu mengambil lima baris dengan `random_state=SEED`.

## Kesalahan yang paling sering terjadi

1. Paket dipasang di luar venv proyek ini. Gejalanya: `import` gagal, atau versi paketnya bukan yang tertulis di `uv.lock`. Jalankan `uv sync` di folder modul, lalu jalankan perintah lewat `uv run`.
2. Sel notebook dijalankan dari bawah, atau layar masih menyimpan hasil lama. Pakai Restart & Run All supaya semua sel jalan dari sel pertama, tanpa ada yang dilewati.
3. Array diisi campuran angka dan teks. Isinya berubah jadi teks, dan rata-rata tidak bisa dihitung.
4. DataFrame dianggap spreadsheet. Mengisi satu kolom tidak mengubah kolom lain. Kolom baru harus kamu hitung sendiri.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Notebook adalah berkas catatan: penjelasan, satu potong kode, lalu hasilnya. Aplikasi yang membukanya bernama Jupyter. Git menyimpan riwayat berkas; folder `.venv` tidak ikut disimpan, dan jangan menaruh kata sandi di berkas. Sel pertama setiap notebook berisi `SEED = 42`. Angka tetap itu dipakai pada setiap undian acak, lewat `random_state=SEED`, supaya urutan yang terambil sama setiap kali notebook diulang.

Perintah ini dijalankan dari folder `phase1-ml/modul-01-persiapan`:

```bash
uv sync
uv run jupyter lab
```

Buka `notebook.ipynb`, kerjakan `latihan.ipynb`, lalu bandingkan dengan `latihan-kunci.ipynb`. Pada tiap notebook: Restart & Run All.

Tes:

```bash
uv run pytest
uv run pytest --nbmake
```

CPU only. Versi paket terkunci di `uv.lock`. Berkas `requirements.txt` dihasilkan dari `uv export` pada kunci itu, untuk yang memasang lewat pip. Jalan yang dipakai modul ini adalah uv. Catatan ini menyebut Python 3.14, tanpa nomor patch.

## Cek pemahaman

1. Sebutkan tiga istilah baru modul ini, masing-masing dalam satu kalimat sesuai artinya.
2. Menghapus folder `.venv` ikut menghapus notebook. Benar atau salah?
3. Mengapa `5, 7, 6, 6` bisa dijumlahkan sekaligus di dalam array?
4. "DataFrame adalah spreadsheet." Benar atau salah? Sebutkan satu batas analoginya.
5. Dataset iris di modul ini diunduh dari internet saat notebook dijalankan. Benar atau salah?
6. Untuk apa `SEED = 42`?
7. Berapa baris dan kolom tabel iris yang tercetak di notebook?

### Kunci jawaban

1. **venv:** lingkungan terpisah yang menyimpan pemasangan paket Python untuk satu proyek, supaya versi paket proyek ini tidak tertukar dengan proyek lain. **array:** kumpulan nilai sejenis dengan bentuk yang tetap, yang dihitung sekaligus. **DataFrame:** tabel di memori: setiap kolom punya nama, setiap baris satu catatan.
2. Salah. venv tidak menyimpan notebook.
3. Karena nilainya sejenis dan bentuknya tetap, jadi array menghitung seluruh isi sekaligus.
4. Salah. Satu batas: mengubah satu kolom tidak memperbarui kolom lain secara otomatis.
5. Salah. Dataset iris sudah ikut terpasang bersama scikit-learn; notebook tidak mengunduhnya.
6. Supaya setiap undian acak di notebook ini memakai angka tetap yang sama, dan urutan baris yang terambil berulang.
7. `baris 150` dan `kolom 5`, disalin dari keluaran di bawah.

### Angka yang disalin dari keluaran notebook

Jawaban "coba sendiri" dan angka di bawah ini disalin dari keluaran notebook yang sudah dijalankan, bukan dihitung ulang di teks. Angka panjang pada rata-rata kolom mahkota ikut disalin apa adanya; jangan dibulatkan dengan tangan.

Dari `notebook.ipynb`:

```
jumlah 24
rata_rata 6.0
rata_kolom 6.0
baris 150
kolom 5
rata_dari_tabel 3.7580000000000005
rata_dari_array 3.7580000000000005
indeks [73, 18, 118, 78, 76]
indeks_lagi [73, 18, 118, 78, 76]
sama True
```

Dari `latihan-kunci.ipynb`:

```
jumlah 20
rata_rata 5.0
rata_kolom 5.0
baris 150
kolom 5
indeks [73, 18, 118, 78, 76]
indeks_lagi [73, 18, 118, 78, 76]
sama True
```

## Sumber

- Python Software Foundation. *venv — Creation of virtual environments.* <https://docs.python.org/3/library/venv.html>
- Astral. *uv.* <https://docs.astral.sh/uv/>
- Project Jupyter. *Jupyter documentation.* <https://docs.jupyter.org/>
- NumPy developers. *NumPy: the absolute basics for beginners.* <https://numpy.org/doc/stable/user/absolute_beginners.html>
- pandas development team. *10 minutes to pandas.* <https://pandas.pydata.org/docs/user_guide/10min.html>
- scikit-learn developers. *Toy datasets* (Iris plants dataset) dan `load_iris`. <https://scikit-learn.org/stable/datasets/toy_dataset.html> dan <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html>
- Fisher, R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); juga dalam "Contributions to Mathematical Statistics" (John Wiley, NY, 1950). Kalimat sumber ini mengikuti halaman toy dataset scikit-learn.
- Chacon, S., dan Straub, B. *Pro Git*, bab "What is Git?". <https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F>
