# Kamus istilah

Satu istilah = satu arti, konsisten di semua modul. **Pyra** menulis entri baru saat membuat modul (maksimal tiga istilah baru per modul); **Squal** memeriksa konsistensi arti dan perumpamaan. Kolom yang masih kosong diisi Pyra.

| Istilah | Arti (satu arti konsisten di semua modul) | Perumpamaan | Modul pengenal | Di mana perumpamaan berhenti berlaku |
|---|---|---|---|---|
| data latih | Bagian data yang dipakai model untuk belajar. |  | 2 |  |
| data uji | Bagian data yang disisihkan dan tidak dilihat model saat belajar, dipakai untuk mengukur seberapa baik model pada data baru. |  | 2 |  |
| baseline | Cara menebak paling sederhana (misalnya selalu menebak rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; model yang baik harus mengalahkannya. |  | 2 |  |
| overfitting | Model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru. |  | 5 |  |
| data leakage | Informasi yang seharusnya tidak tersedia saat model belajar (misalnya dari data uji atau dari masa depan) ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan. |  | 2 |  |
