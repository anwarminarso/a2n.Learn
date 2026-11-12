# Aturan data

- Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan.
- Data publik yang sudah disetujui: dokumentasikan sumber dan lisensinya di README modul; jangan mengarang nama dataset atau lisensi.
- **Dilarang** menyimpan secret (password, token, connection string).
- File data mentah tidak di-commit (lihat `.gitignore`), kecuali salinan kecil data publik yang sudah disetujui.

Salinan kecil data publik (pengecualian yang sudah disetujui Frieren atau mas Anwar, dengan sumber dan lisensi jelas) disimpan di `data/public/`; folder itu dikecualikan dari `.gitignore`, jadi tidak perlu `git add -f`.

## Fase 2

Placeholder di `phase2-ai/` menambah aturan berikut. Materi belum ditulis.

- Dataset publik berlisensi jelas atau sintetis dari generator di repo. Tanpa data asli perusahaan.
- Model dan dataset Hugging Face di-pin ke revisi. Hanya format safetensors. `trust_remote_code=False`. Lisensi tiap model dicatat.
- Dataset, adapter LoRA, dan indeks vektor dari data non-publik tidak boleh masuk repo atau di-push ke Hugging Face.
