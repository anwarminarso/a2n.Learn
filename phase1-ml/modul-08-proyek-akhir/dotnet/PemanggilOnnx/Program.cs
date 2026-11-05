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

var opsi = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
var muatan = JsonSerializer.Deserialize<Muatan>(File.ReadAllText(args[1]), opsi);
if (muatan is null || muatan.Fitur.Length == 0)
{
    Console.Error.WriteLine("berkas masukan kosong");
    return 1;
}

int baris = muatan.Fitur.Length;
int kolom = muatan.Fitur[0].Length;
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
