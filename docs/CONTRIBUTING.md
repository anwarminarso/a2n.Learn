# Kontribusi

## Gaya penulisan
Pembaca sasaran: anak SMP.
- Istilah baru dijelaskan dulu dengan contoh sehari-hari, baru kemudian nama teknisnya.
- Satu sel kode = satu ide, dengan komentar singkat berbahasa Indonesia.
- Rumus hanya bila perlu, selalu disertai contoh angka kecil.

## Peran
- **Pyra**: menulis notebook, kode, dan tes modul.
- **Ursa**: menjalankan setiap notebook dari nol; PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya.
- **Squal**: audit dokumentasi saja (ketepatan teori, urutan, istilah menyesatkan), bukan security. Verdict: PASS / PASS BERSYARAT / BLOCK.
- **Frieren**: review alur belajar sebelum modul sampai ke mas.
- **Iris**: struktur repo, issue, urutan, dan merge.

## Alur kerja
1. Satu modul = satu PR dari Pyra ke `develop` (branch fitur, mis. `modul/01-persiapan`).
2. Ursa menjalankan dari nol dan melaporkan PASS/FAIL di PR.
3. Squal mengaudit dokumentasi.
4. Frieren mereview alur belajar.
5. Iris merge dengan **merge commit** (bukan squash/rebase), lalu menghapus head branch.

Larangan: tidak menghapus `main`/`develop`, tidak force-push. Modul berikutnya dimulai hanya setelah modul sebelumnya lolos Ursa dan Squal.

## Definition of Done per modul
- [ ] (a) venv baru dari `requirements.txt` pinned; Restart & Run All tanpa error dan tanpa sel dilewati; tiap notebook < 2 menit; `pytest --nbmake` lulus
- [ ] (b) seed tetap; setiap angka yang dikutip di teks berasal dari output notebook, bukan ditulis tangan
- [ ] (c) data: dataset bawaan scikit-learn atau sintetis yang dibangkitkan kode; tanpa unduhan; tanpa data ANTAM
- [ ] (d) latihan punya kunci (`latihan-kunci.ipynb`) yang dijalankan Ursa; cek pemahaman punya jawaban benar yang bisa diverifikasi
- [ ] (e) sumber dikutip (buku atau dokumentasi resmi), tanpa kutipan karangan
- [ ] (f) bisa dibaca dan dikerjakan dalam SATU kali duduk: teori maksimal 1 halaman, notebook pendek
- [ ] (g) Ursa PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya; Squal memberi verdict dokumentasi PASS / PASS BERSYARAT / BLOCK (bukan security); Frieren mereview alur belajar sebelum ke mas
