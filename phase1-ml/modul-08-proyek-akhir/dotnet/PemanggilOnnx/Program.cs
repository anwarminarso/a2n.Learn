// Program kecil di luar Python. Ia membaca berkas ONNX lalu menulis tebakan.
// C# adalah bahasa program ini. Kamu tidak perlu menghafalnya.

using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

if (args.Length != 3)
{
    return Gagal("pakai: PemanggilOnnx model.onnx baris.json keluar.json");
}

const string Petunjuk = "jalankan notebook dulu dan jalankan perintah dari folder modul 8";

if (!File.Exists(args[0]))
{
    return Gagal($"berkas tidak ditemukan: {args[0]}; {Petunjuk}");
}

if (!File.Exists(args[1]))
{
    return Gagal($"berkas tidak ditemukan: {args[1]}; {Petunjuk}");
}

string teksJson;
try
{
    teksJson = File.ReadAllText(args[1]);
}
catch (UnauthorizedAccessException)
{
    return Gagal($"berkas tidak terbaca: {args[1]}");
}
catch (IOException)
{
    return Gagal($"berkas tidak terbaca: {args[1]}");
}

JsonDocument dokumen;
try
{
    dokumen = JsonDocument.Parse(teksJson);
}
catch (JsonException)
{
    return Gagal("baris.json rusak");
}

using (dokumen)
{
    JsonElement akar = dokumen.RootElement;
    if (akar.ValueKind == JsonValueKind.Null)
    {
        return Gagal("baris.json berisi null");
    }

    if (akar.ValueKind != JsonValueKind.Object)
    {
        return Gagal("baris.json rusak");
    }

    if (!Cari(akar, "nama_masukan", out JsonElement namaEl)
        || namaEl.ValueKind is JsonValueKind.Null or JsonValueKind.Undefined
        || namaEl.ValueKind != JsonValueKind.String
        || string.IsNullOrEmpty(namaEl.GetString()))
    {
        return Gagal("nama_masukan hilang atau kosong");
    }

    string namaMasukan = namaEl.GetString()!;

    if (!Cari(akar, "fitur", out JsonElement fiturEl) || fiturEl.ValueKind == JsonValueKind.Null)
    {
        return Gagal("fitur hilang atau null");
    }

    if (fiturEl.ValueKind != JsonValueKind.Array || fiturEl.GetArrayLength() == 0)
    {
        return Gagal("fitur hilang atau null");
    }

    int baris = fiturEl.GetArrayLength();
    int kolom = -1;
    var datar = new List<float>();
    int i = 0;
    foreach (JsonElement barisEl in fiturEl.EnumerateArray())
    {
        if (barisEl.ValueKind == JsonValueKind.Null)
        {
            return Gagal("fitur hilang atau null");
        }

        if (barisEl.ValueKind != JsonValueKind.Array)
        {
            return Gagal("baris.json rusak");
        }

        int panjang = barisEl.GetArrayLength();
        if (panjang == 0)
        {
            return Gagal($"panjang baris tidak cocok: baris {i} kosong, kolom tidak ada");
        }

        if (kolom < 0)
        {
            kolom = panjang;
        }
        else if (panjang != kolom)
        {
            return Gagal($"panjang baris tidak cocok: baris {i} punya {panjang} angka, kolom {kolom}");
        }

        foreach (JsonElement angkaEl in barisEl.EnumerateArray())
        {
            if (angkaEl.ValueKind != JsonValueKind.Number)
            {
                return Gagal("baris.json rusak");
            }

            double angka;
            try
            {
                angka = angkaEl.GetDouble();
            }
            catch (FormatException)
            {
                return Gagal("angka tidak hingga");
            }
            catch (OverflowException)
            {
                return Gagal("angka tidak hingga");
            }

            float sempit = (float)angka;
            if (!double.IsFinite(angka) || !float.IsFinite(sempit))
            {
                return Gagal("angka tidak hingga");
            }

            datar.Add(sempit);
        }

        i++;
    }

    string? folderKeluar = Path.GetDirectoryName(args[2]);
    if (!string.IsNullOrEmpty(folderKeluar) && !Directory.Exists(folderKeluar))
    {
        return Gagal($"folder keluaran tidak ada: {folderKeluar}");
    }

    InferenceSession sesi;
    try
    {
        sesi = new InferenceSession(args[0]);
    }
    catch (OnnxRuntimeException)
    {
        return Gagal("model.onnx rusak atau tidak terbaca, jalankan notebook ulang");
    }
    catch (UnauthorizedAccessException)
    {
        return Gagal("model.onnx rusak atau tidak terbaca, jalankan notebook ulang");
    }
    catch (IOException)
    {
        return Gagal("model.onnx rusak atau tidak terbaca, jalankan notebook ulang");
    }

    using (sesi)
    {
        if (!sesi.InputMetadata.TryGetValue(namaMasukan, out NodeMetadata? meta))
        {
            return Gagal("nama_masukan tidak ada pada model");
        }

        int dimensi = 0;
        foreach (int ukuran in meta.Dimensions)
        {
            if (ukuran > 0)
            {
                dimensi = ukuran;
            }
        }

        if (dimensi > 0 && kolom != dimensi)
        {
            return Gagal($"jumlah kolom tidak cocok: baris punya {kolom} angka, model minta {dimensi}");
        }

        long[]? label = null;
        float[][]? probabilitas = null;
        try
        {
            var tensor = new DenseTensor<float>(datar.ToArray(), new[] { baris, kolom });
            var masukan = new List<NamedOnnxValue>
            {
                NamedOnnxValue.CreateFromTensor(namaMasukan, tensor),
            };
            using var hasil = sesi.Run(masukan);
            try
            {
                foreach (var item in hasil)
                {
                    if (item.Name == "label")
                    {
                        label = item.Value switch
                        {
                            DenseTensor<long> panjangLabel => panjangLabel.ToArray(),
                            DenseTensor<int> pendek => pendek.Select(angka => (long)angka).ToArray(),
                            _ => throw new InvalidOperationException("tipe label tidak dikenal"),
                        };
                    }
                    else if (item.Name == "probabilities")
                    {
                        var tabel = (DenseTensor<float>)item.Value;
                        int nKelas = tabel.Dimensions[1];
                        probabilitas = new float[baris][];
                        for (int r = 0; r < baris; r++)
                        {
                            probabilitas[r] = new float[nKelas];
                            for (int k = 0; k < nKelas; k++)
                            {
                                probabilitas[r][k] = tabel[r, k];
                            }
                        }
                    }
                }
            }
            catch (InvalidOperationException)
            {
                return Gagal("keluaran ONNX tidak dikenal");
            }
            catch (InvalidCastException)
            {
                return Gagal("keluaran ONNX tidak dikenal");
            }
        }
        catch (OnnxRuntimeException ex)
        {
            return Gagal("masukan tidak cocok dengan model: " + ex.Message);
        }
        catch (ArgumentException ex)
        {
            return Gagal("masukan tidak cocok dengan model: " + ex.Message);
        }

        if (label is null || probabilitas is null)
        {
            return Gagal("keluaran ONNX tidak lengkap");
        }

        var teks = JsonSerializer.Serialize(new Keluar(label, probabilitas));
        try
        {
            File.WriteAllText(args[2], teks);
        }
        catch (UnauthorizedAccessException)
        {
            return Gagal($"keluaran tidak bisa ditulis: {args[2]}");
        }
        catch (IOException)
        {
            return Gagal($"keluaran tidak bisa ditulis: {args[2]}");
        }

        return 0;
    }
}

static int Gagal(string pesan)
{
    Console.Error.WriteLine(pesan);
    return 1;
}

static bool Cari(JsonElement akar, string nama, out JsonElement ketemu)
{
    foreach (JsonProperty properti in akar.EnumerateObject())
    {
        if (string.Equals(properti.Name, nama, StringComparison.OrdinalIgnoreCase))
        {
            ketemu = properti.Value;
            return true;
        }
    }

    ketemu = default;
    return false;
}

sealed record Keluar(
    [property: JsonPropertyName("label")] long[] Label,
    [property: JsonPropertyName("probabilitas")] float[][] Probabilitas
);
