// Program kecil di luar Python. Ia mengirim satu pertanyaan ke peladen lokal.
// C# adalah bahasa program ini. Kamu tidak perlu menghafalnya.
// Mode cepat tidak menjalankan berkas ini. Alat agen tidak ada di sini.

using System.Net.Http.Json;
using System.Text.Json.Serialization;

if (args.Length != 1)
{
    Console.Error.WriteLine("pakai: PemanggilAgen pertanyaan");
    return 1;
}

const string Alamat = "http://127.0.0.1:8765/jawab";
const double Batas = 0.3;

using var klien = new HttpClient();
klien.Timeout = TimeSpan.FromSeconds(5);
using var respons = await klien.PostAsJsonAsync(Alamat, new Pertanyaan(args[0]));
var isi = await respons.Content.ReadFromJsonAsync<Jawaban>();
if (isi is null)
{
    Console.Error.WriteLine("jawaban kosong");
    return 1;
}

bool lulus = isi.Status == "bersumber" && isi.Skor + 1e-9 >= Batas;
Console.WriteLine(lulus ? "dalam_batas" : "di_bawah_batas");
Console.WriteLine(isi.Sumber);
return lulus ? 0 : 1;

sealed record Pertanyaan([property: JsonPropertyName("pertanyaan")] string Teks);

sealed record Jawaban(
    [property: JsonPropertyName("status")] string Status,
    [property: JsonPropertyName("sumber")] string Sumber,
    [property: JsonPropertyName("skor")] double Skor
);
