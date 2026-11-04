---
name: Modul pembelajaran
about: Satu issue per modul
title: "[Modul N] <nama>"
labels: ["module", "ml"]
---

## Tingkat
<!-- beginner / intermediate / advanced; tambahkan label level:* yang sesuai -->

## Tujuan belajar

## Deliverables
- [ ] Teori 1 halaman (`README.md`) + sumber
- [ ] `notebook.ipynb`
- [ ] Kasus nyata dengan data bawaan scikit-learn atau sintetis
- [ ] `latihan.ipynb` + `latihan-kunci.ipynb`
- [ ] Cek pemahaman dengan jawaban yang bisa diverifikasi
- [ ] `tests/` + `requirements.txt` pinned, Python 3.12, CPU only

## Dependensi

## Pemilik
Pyra (penulis) · Ursa (uji jalan) · Squal (audit dok) · Frieren (review alur) · Iris (merge)

## Acceptance criteria (Definition of Done)
- [ ] (a) venv baru dari `requirements.txt` pinned; Restart & Run All tanpa error dan tanpa sel dilewati; tiap notebook < 2 menit; `pytest --nbmake` lulus
- [ ] (b) seed tetap; setiap angka yang dikutip di teks berasal dari output notebook, bukan ditulis tangan
- [ ] (c) data: dataset bawaan scikit-learn atau sintetis yang dibangkitkan kode; tanpa unduhan; tanpa data ANTAM
- [ ] (d) latihan punya kunci (`latihan-kunci.ipynb`) yang dijalankan Ursa; cek pemahaman punya jawaban benar yang bisa diverifikasi
- [ ] (e) sumber dikutip (buku atau dokumentasi resmi), tanpa kutipan karangan
- [ ] (f) bisa dibaca dan dikerjakan dalam SATU kali duduk: teori maksimal 1 halaman, notebook pendek
- [ ] (g) Ursa PASS/FAIL hanya dari log mentah sesi yang benar-benar menjalankannya; Squal memberi verdict dokumentasi PASS / PASS BERSYARAT / BLOCK (bukan security); Frieren mereview alur belajar sebelum ke mas

## Aturan data
Hanya data bawaan scikit-learn atau sintetis. Tanpa data ANTAM, tanpa secret.

## Estimasi
1 minggu, dapat dipadatkan sesuai jam per minggu yang mas pilih.
