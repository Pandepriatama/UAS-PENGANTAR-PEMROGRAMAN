from prettytable import PrettyTable
import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="programming"
)

active = True

while active:
    programming = koneksi.cursor()

    programming.execute('select*from mahasiswa')

    data = programming.fetchall()
    t = PrettyTable(['id', 'nama', 'nim'])

    for row in data:
        t.add_row(row)
    print(t)

    print("1. Insert data ")
    print("2. Update data ")
    print("3. Delete data ")
    print("4. Keluar ")
    inputuser = input("\nMasukkan Pilihan : ")

    if inputuser == '1':
        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM  : ")

        if len(nama) == 0 and len(nim) == 0:
            print("Data Kosong")
        else:
            koneksiTest = koneksi.cursor()

            koneksiTest.execute(
                "insert into mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))

            koneksi.commit()

            print("Data Sudah Berhasil Ditambahkan")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) :")
        if cek == 'No':
            active = False
    if inputuser == '2':
        idupdate = input("Masukkan Id yang ingin anda update : ")
        print("Pilih tabel yang ingin anda update : ")
        print("1. Nama")
        print("2. NIM")
        print("3. Ubah Seluruhnya")
        aksiupdate = input("Pilih 1-3 : ")
        if aksiupdate == '1':
            namaupdate = input("Masukkan Nama Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data Nama Berhasil Diupdate")
        elif aksiupdate == '2':
            nimupdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nim = '{nimupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data NIM Berhasil Diupdate")
        elif aksiupdate == '3':
            namaupdate = input("Masukkan Nama Baru : ")
            nimupdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaupdate}', nim = '{nimupdate}' where id = '{idupdate}'")
            koneksi.commit()
            print("Data Berhasil Diupdate")
        else:
            print("Masukkan 1-3")

        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            active = False
    if inputuser == '3':
        iddelete = input("Masukkan ID yang ingin di hapus : ")
        koneksiTest = koneksi.cursor()
        koneksiTest.execute(
            f"delete from mahasiswa where id='{iddelete}'")
        koneksi.commit()
        print("Data Berhasil Dihapus")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            active = False
    if inputuser == '4':
        active = False
