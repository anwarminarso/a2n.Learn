# Kamus istilah

Satu istilah = satu arti, konsisten di semua modul. **Pyra** menulis entri baru saat membuat modul (maksimal tiga istilah baru per modul); **Squal** memeriksa konsistensi arti dan perumpamaan. Kolom yang masih kosong diisi Pyra.

| Istilah | Arti (satu arti konsisten di semua modul) | Perumpamaan | Modul pengenal | Di mana perumpamaan berhenti berlaku |
|---|---|---|---|---|
| data latih dan data uji | Data dibagi dua: data latih dipakai model untuk belajar; data uji disisihkan dan tidak dilihat model saat belajar, dipakai untuk mengukur seberapa baik model pada data baru. Satu entri karena satu ide. |  | 2 |  |
| baseline | Cara menebak paling sederhana (misalnya selalu menebak rata-rata atau kelas yang paling banyak) yang dipakai sebagai pembanding; model yang baik harus mengalahkannya. |  | 2 |  |
| ukuran kesalahan | Satu angka yang menyatakan seberapa jauh tebakan model dari jawaban yang benar. Nama istilah dan arti finalnya ditetapkan Pyra saat menulis modul 2. |  | 2 |  |
| overfitting | Model terlalu menyesuaikan diri dengan data latih, termasuk kebetulan-kebetulannya, sehingga hasilnya bagus di data latih tetapi buruk di data baru. |  | 3 |  |
| data leakage | Informasi yang seharusnya tidak tersedia saat model belajar (misalnya dari data uji atau dari masa depan) ikut terpakai, sehingga skor terlihat lebih bagus dari kenyataan. |  | 5 |  |

Catatan pengenalan istilah: modul 2 hanya menyebut ide overfitting dengan bahasa biasa ("model menghafal") tanpa menjadikannya istilah resmi, jadi hitungannya tetap tiga istilah. Overfitting menjadi istilah resmi di modul 3 (kurva terlalu lentur pada regresi) dan diperdalam di modul evaluasi. Data leakage diperkenalkan di modul 5, bersama cross-validation.
