---
name: Modul pembelajaran
about: Satu issue per modul
title: "[Modul N] <nama>"
labels: ["module", "ml"]
---

## Tingkat
<!-- beginner / intermediate / advanced / pro; tambahkan label level:* yang sesuai -->

## Tujuan belajar

## Deliverables
- [ ] Teori 1 halaman (`README.md`) + sumber
- [ ] `notebook.ipynb`
- [ ] Kasus nyata sesuai aturan data
- [ ] `latihan.ipynb` + `latihan-kunci.ipynb`
- [ ] Cek pemahaman dengan jawaban yang bisa diverifikasi
- [ ] `tests/` + `pyproject.toml` + `uv.lock` + `requirements.txt` (`uv export`), Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only

## Dependensi

## Pemilik
Pyra (penulis) · Ursa (uji jalan) · Squal (audit dok) · Frieren (review alur) · Iris (merge)

## Acceptance criteria (Definition of Done)
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
2. Maksimal **tiga istilah baru** per modul; tiap istilah punya perumpamaan dan masuk [`docs/kamus-istilah.md`](../../docs/kamus-istilah.md).
3. "Coba sendiri dulu, baru kode".
4. Bagian "Kesalahan yang paling sering terjadi".
5. Cek pemahaman dengan kunci jawaban.

Aturan tulis: cerita dulu baru istilah; gambar dulu baru rumus.

## Aturan audit dan QA
- Analogi boleh menyederhanakan, tetapi tidak boleh membuat penjelasan salah; modul menyebut di mana analogi berhenti berlaku.
- Setiap istilah punya satu arti yang konsisten di semua modul dan tercatat di `docs/kamus-istilah.md` (Squal mengaudit dokumentasi saja, bukan keamanan).
- Ursa menjalankan ujian akhir tiap tingkat (ujian level) sebagai bagian dari PASS.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data ANTAM. Tanpa secret.

## Estimasi
Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.
