# Template modul

## Struktur folder
```
phase1-ml/modul-NN-nama/
  README.md             # teori 1 halaman + sumber + cek pemahaman
  notebook.ipynb        # materi + kasus nyata
  latihan.ipynb         # latihan
  latihan-kunci.ipynb   # kunci jawaban (dijalankan Ursa)
  tests/                # tes (pytest --nbmake, dll.)
  requirements.txt      # pinned, hasil `uv export` dari uv.lock
```
Python 3.12, CPU only.

## Isi `README.md` modul
1. Judul, tujuan belajar, dan **Tingkat** (`beginner` / `intermediate` / `advanced`)
2. Teori (maksimal 1 halaman)
3. Kasus nyata: sumber data (bawaan scikit-learn atau sintetis dari kode)
4. Cara menjalankan
5. Cek pemahaman (jawaban benar yang bisa diverifikasi)
6. Sumber (buku atau dokumentasi resmi)

## Checklist (Definition of Done)
- [ ] (a) venv baru dari `requirements.txt` pinned; Restart & Run All tanpa error dan tanpa sel dilewati; tiap notebook < 2 menit; `pytest --nbmake` lulus
- [ ] (b) seed tetap; setiap angka yang dikutip di teks berasal dari output notebook, bukan ditulis tangan
- [ ] (c) data: dataset bawaan scikit-learn atau sintetis yang dibangkitkan kode; tanpa unduhan; tanpa data ANTAM
- [ ] (d) latihan punya kunci (`latihan-kunci.ipynb`) yang dijalankan Ursa; cek pemahaman punya jawaban benar yang bisa diverifikasi
- [ ] (e) sumber dikutip (buku atau dokumentasi resmi), tanpa kutipan karangan
- [ ] (f) bisa dibaca dan dikerjakan dalam SATU kali duduk: teori maksimal 1 halaman, notebook pendek
- [ ] (g) Ursa PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya; Squal memberi verdict dokumentasi PASS / PASS BERSYARAT / BLOCK (bukan security); Frieren mereview alur belajar sebelum ke mas

## Gaya penulisan
Pembaca sasaran: anak SMP.
- Istilah baru dijelaskan dulu dengan contoh sehari-hari, baru kemudian nama teknisnya.
- Satu sel kode = satu ide, dengan komentar singkat berbahasa Indonesia.
- Rumus hanya bila perlu, selalu disertai contoh angka kecil.
