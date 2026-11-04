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
- [ ] (a) Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), sesuai `.python-version`; lingkungan baru dari `pyproject.toml` + `uv.lock` (pytest, nbmake, dan ipykernel versinya dikunci di `uv.lock`; `requirements.txt` hasil `uv export` di-commit per modul); Restart & Run All tanpa error dan tanpa sel dilewati; tiap notebook < 2 menit; `pytest --nbmake` lulus
- [ ] (b) seed seragam: konstanta `SEED = 42` di sel pertama setiap notebook dan dipakai di setiap `random_state`/pemanggilan acak; setiap angka yang dikutip di teks berasal dari output notebook, bukan ditulis tangan
- [ ] (c) data: Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data ANTAM.
- [ ] (d) latihan punya kunci (`latihan-kunci.ipynb`) yang dijalankan Ursa; cek pemahaman punya jawaban benar yang bisa diverifikasi
- [ ] (e) sumber dikutip (buku atau dokumentasi resmi), tanpa kutipan karangan
- [ ] (f) bisa dibaca dan dikerjakan dalam SATU kali duduk: teori maksimal 1 halaman, notebook pendek
- [ ] (g) Ursa PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya; Squal memberi verdict dokumentasi PASS / PASS BERSYARAT / BLOCK (bukan security); Frieren mereview alur belajar sebelum ke mas
- [ ] (h) analogi tidak membuat penjelasan salah, dan batas berlakunya disebut
- [ ] (i) maksimal tiga istilah baru, masing-masing dengan satu arti konsisten dan tercatat di `docs/kamus-istilah.md`
- [ ] (j) bila modul menutup satu tingkat: ujian level dijalankan Ursa dan termasuk dalam PASS
- [ ] (k) gaya bahasa SMP: istilah baru dijelaskan dengan contoh sehari-hari dulu, satu sel kode = satu ide dengan komentar Indonesia, rumus hanya bila perlu dan selalu dengan contoh angka kecil

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
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data ANTAM.

## Tempo
Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.

## Versi Python
- **Python 3.14** (versi stabil terbaru yang masih bugfix; EOL 2030-10). Wheel dicek Pyra pada 2026-11-04 untuk Linux x86_64 dan Windows (macOS dan ARM belum dicek). Tidak perlu fallback saat ini.
- `.python-version` dipin ke patch 3.14.x terbaru yang dipakai Pyra saat mengunci `uv.lock` (nomor patch dicatat di file itu). Sampai Pyra mengunci, file ini berisi `3.14`.
- Versi paket tidak ditulis di dokumen ini; Pyra menguncinya di `uv.lock` tiap modul (di-commit).
- Python 3.15 belum dipakai. Python 3.10 sudah EOL (2026-10-01), jangan dipakai.
- Aturan untuk kerusakan di masa depan: bila salah satu dependensi tidak punya wheel untuk 3.14, turun ke 3.13; jangan pernah 3.12 atau lebih lama. Catat keputusan dan tanggalnya di tabel di bawah.
- Ursa menjalankan notebook dan ujian level dengan versi Python yang persis sama dengan `.python-version`.
- Sumber status versi: https://devguide.python.org/versions/

### Catatan keputusan
| Tanggal | Keputusan | Dasar |
|---|---|---|
| 2026-11-04 | Python 3.14, tanpa fallback | Pengecekan wheel oleh Pyra (Linux x86_64, Windows) |
