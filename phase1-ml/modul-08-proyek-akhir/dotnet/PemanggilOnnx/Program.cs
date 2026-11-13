// Program kecil di luar Python. Ia membaca berkas ONNX lalu menulis tebakan.
// C# adalah bahasa program ini. Kamu tidak perlu menghafalnya.

using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

if (args.Length != 3)
{
    Console.Error.WriteLine("pakai: PemanggilOnnx model.onnx baris.json keluar.json");
    return 1;
}

const string Petunjuk = "jalankan notebook dulu dan jalankan perintah dari folder modul 8";

if (!File.Exists(args[0]))
{
    Console.Error.WriteLine($"berkas tidak ditemukan: {args[0]}; {Petunjuk}");
    return 1;
}

if (!File.Exists(args[1]))
{
    Console.Error.WriteLine($"berkas tidak ditemukan: {args[1]}; {Petunjuk}");
    return 1;
}

var opsi = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
Muatan? muatan;
try
{
    muatan = JsonSerializer.Deserialize<Muatan>(File.ReadAllText(args[1]), opsi);
}
catch (JsonException)
{
    Console.Error.WriteLine("baris.json rusak");
    return 1;
}

if (muatan is null || muatan.Fitur.Length == 0)
{
    Console.Error.WriteLine("berkas masukan kosong");
    return 1;
}

int baris = muatan.Fitur.Length;
if (muatan.Fitur[0] is null)
{
    Console.Error.WriteLine("panjang baris tidak cocok: baris 0 kosong, kolom tidak ada");
    return 1;
}

int kolom = muatan.Fitur[0].Length;
for (int i = 0; i < baris; i++)
{
    int panjang = muatan.Fitur[i]?.Length ?? -1;
    if (panjang != kolom)
    {
        Console.Error.WriteLine(
            $"panjang baris tidak cocok: baris {i} punya {Math.Max(panjang, 0)} angka, kolom {kolom}");
        return 1;
    }
}

var datar = new float[baris * kolom];
for (int i = 0; i < baris; i++)
{
    for (int j = 0; j < kolom; j++)
    {
        datar[(i * kolom) + j] = muatan.Fitur[i][j];
    }
}

using var sesi = new InferenceSession(args[0]);
var tensor = new DenseTensor<float>(datar, new[] { baris, kolom });
var masukan = new List<NamedOnnxValue>
{
    NamedOnnxValue.CreateFromTensor(muatan.NamaMasukan, tensor),
};

long[]? label = null;
float[][]? probabilitas = null;
using (var hasil = sesi.Run(masukan))
{
    foreach (var item in hasil)
    {
        if (item.Name == "label")
        {
            label = item.Value switch
            {
                DenseTensor<long> panjang => panjang.ToArray(),
                DenseTensor<int> pendek => pendek.Select(angka => (long)angka).ToArray(),
                _ => throw new InvalidOperationException("tipe label tidak dikenal"),
            };
        }
        else if (item.Name == "probabilities")
        {
            var tabel = (DenseTensor<float>)item.Value;
            int nKelas = tabel.Dimensions[1];
            probabilitas = new float[baris][];
            for (int i = 0; i < baris; i++)
            {
                probabilitas[i] = new float[nKelas];
                for (int k = 0; k < nKelas; k++)
                {
                    probabilitas[i][k] = tabel[i, k];
                }
            }
        }
    }
}

if (label is null || probabilitas is null)
{
    Console.Error.WriteLine("keluaran ONNX tidak lengkap");
    return 1;
}

var teks = JsonSerializer.Serialize(new Keluar(label, probabilitas));
File.WriteAllText(args[2], teks);
return 0;

sealed class Muatan
{
    [JsonPropertyName("nama_masukan")]
    public string NamaMasukan { get; set; } = "";

    [JsonPropertyName("fitur")]
    public float[][] Fitur { get; set; } = [];
}

sealed record Keluar(
    [property: JsonPropertyName("label")] long[] Label,
    [property: JsonPropertyName("probabilitas")] float[][] Probabilitas
);
