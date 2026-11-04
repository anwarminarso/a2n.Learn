# Template modul

## Struktur folder
```
pyproject.toml          # dependensi, satu berkas di root repo
uv.lock                 # versi paket terkunci (termasuk pytest, nbmake, ipykernel)
requirements.txt        # hasil `uv export` dari uv.lock di root
.python-version         # 3.14

phase1-ml/modul-NN-nama/
  README.md             # teori 1 halaman + sumber + cek pemahaman
  notebook.ipynb        # materi + kasus nyata
  latihan.ipynb         # latihan
  latihan-kunci.ipynb   # kunci jawaban (dijalankan Ursa)
  tests/                # tes (pytest --nbmake, dll.)
```
Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only. Setiap notebook mendefinisikan `SEED = 42` di sel pertama dan memakainya di setiap `random_state`.

## Isi `README.md` modul
1. Judul, tujuan belajar, dan **Tingkat** (`beginner` / `intermediate` / `advanced` / `pro`)
2. Cerita pembuka sehari-hari (maksimal satu layar)
3. Teori (maksimal 1 halaman; maksimal tiga istilah baru, masing-masing dengan perumpamaan dan **batas analogi**: di mana perumpamaan berhenti berlaku)
4. Coba sendiri dulu, baru kode
5. Kasus nyata: sumber data sesuai aturan data
6. Kesalahan yang paling sering terjadi
7. Cara menjalankan
8. Cek pemahaman dengan kunci jawaban
9. Sumber (buku atau dokumentasi resmi)

## Checklist (Definition of Done)
- [ ] (a) Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), sesuai `.python-version`; lingkungan baru dari `pyproject.toml` + `uv.lock` di root repo (pytest, nbmake, dan ipykernel versinya dikunci di `uv.lock`; `requirements.txt` hasil `uv export` di-commit di root); Restart & Run All tanpa error dan tanpa sel dilewati; tiap notebook < 2 menit; `pytest --nbmake` lulus
- [ ] (b) seed seragam: konstanta `SEED = 42` di sel pertama setiap notebook dan dipakai di setiap `random_state`/pemanggilan acak; setiap angka yang dikutip di teks berasal dari output notebook, bukan ditulis tangan
- [ ] (c) data: Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan.
- [ ] (d) latihan punya kunci (`latihan-kunci.ipynb`) yang dijalankan Ursa; cek pemahaman punya jawaban benar yang bisa diverifikasi
- [ ] (e) sumber dikutip (buku atau dokumentasi resmi), tanpa kutipan karangan
- [ ] (f) bisa dibaca dan dikerjakan dalam SATU kali duduk: teori maksimal 1 halaman, notebook pendek
- [ ] (g) Ursa PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya; Squal memberi verdict dokumentasi PASS / PASS BERSYARAT / BLOCK (bukan security); Frieren mereview alur belajar sebelum ke mas
- [ ] (h) analogi tidak membuat penjelasan salah, dan batas berlakunya disebut
- [ ] (i) maksimal tiga istilah baru, masing-masing dengan satu arti konsisten dan tercatat di `docs/kamus-istilah.md`
- [ ] (j) bila modul menutup satu tingkat: ujian level dijalankan Ursa dan termasuk dalam PASS
- [ ] (k) gaya bahasa ramah pemula: istilah baru dijelaskan dengan contoh sehari-hari dulu, satu sel kode = satu ide dengan komentar Indonesia, rumus hanya bila perlu dan selalu dengan contoh angka kecil

## Gaya penulisan
Pembaca sasaran: pemula tanpa latar belakang ML.
- Istilah baru dijelaskan dulu dengan contoh sehari-hari, baru kemudian nama teknisnya.
- Satu sel kode = satu ide, dengan komentar singkat berbahasa Indonesia.
- Rumus hanya bila perlu, selalu disertai contoh angka kecil.

## Format wajib modul
1. Cerita sehari-hari pembuka, maksimal satu layar.
2. Maksimal **tiga istilah baru** per modul; tiap istilah punya perumpamaan dan masuk [`docs/kamus-istilah.md`](kamus-istilah.md).
3. "Coba sendiri dulu, baru kode".
4. Bagian "Kesalahan yang paling sering terjadi".
5. Cek pemahaman dengan kunci jawaban.

Aturan tulis: cerita dulu baru istilah; gambar dulu baru rumus.

## Aturan audit dan QA
- Analogi boleh menyederhanakan, tetapi tidak boleh membuat penjelasan salah; modul menyebut di mana analogi berhenti berlaku.
- Setiap istilah punya satu arti yang konsisten di semua modul dan tercatat di `docs/kamus-istilah.md` (Squal mengaudit dokumentasi saja, bukan keamanan).
- Ursa menjalankan ujian akhir tiap tingkat (ujian level) sebagai bagian dari PASS.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan.

## Tempo
Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.
