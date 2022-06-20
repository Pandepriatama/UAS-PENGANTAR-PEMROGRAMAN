TiUndiknas = [
    {
        "nama": "pande priatama",
        "nim": "42130090",
        "jurusan": "teknologi informasi"
    },
    {
        "nama": "adi saputra",
        "nim": "421313248",
        "jurusan": "teknologi informasi"
    },
    {
        "nama": "ary mahendra",
        "nim": "42130086",
        "jurusan": "teknologi informasi"
    }

]

print("Silahkan Pilih Nama Mahasiswa TI Undiknas Berikut : ")
print("1. pande priatama")
print("2. adi saputra")
print("1. ary mahendra")

input = input("\nMasukkan Angka 1-3 :")


if input == '1':
    print("nama = ", TiUndiknas[0]['nama'])
    print("nim = ", TiUndiknas[0]['nim'])
    print("jurusan = ", TiUndiknas[0]['jurusan'])

elif input == '2':
    print("nama = ", TiUndiknas[1]['nama'])
    print("nim = ", TiUndiknas[1]['nim'])
    print("jurusan = ", TiUndiknas[1]['jurusan'])
else:
    print("nama = ", TiUndiknas[2]['nama'])
    print("nim = ", TiUndiknas[2]['nim'])
    print("jurusan = ", TiUndiknas[2]['jurusan'])
