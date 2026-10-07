import json
from prettytable import PrettyTable

with open("mahasiswa.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

def tampilkan_data():
    print("========== DATA NILAI MAHASISWA ==========")
    if not data:
        print("Belum ada data mahasiswa")
        return
    else:
        for i, mahasiswa in enumerate(data, start=1):
            print(f"{i}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Prodi: {mahasiswa['prodi']}, Mata Kuliah: {mahasiswa['mata kuliah']}, Nilai: {mahasiswa['nilai']}")

def simpan_file():
    with open("mahasiswa.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4, )
        return "Tersimpan mahasiswa ke mahasiswa.json"

def tambah_data():
    print("========== TAMBAH DATA MAHASISWA ==========")
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    matkul = input("Masukkan mata kuliah: ")
    while True:
        nilai = input("Masukkan nilai mahasiswa: ")
        if nilai.isdigit():
            nilai = int(nilai)
            break
        print("Nilai harus berupa angka. Coba lagi.")

    data.append({
        "nama": nama,
        "nim": nim,
        "prodi": prodi,
        "mata kuliah": matkul,
        "nilai": nilai
    })
    simpan_file()
    return "Data telah ditambahkan!"

while True:
    print("========== MENU ==========")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    tabel.add_row(["1", "Tampilkan data mahasiswa"])
    tabel.add_row(["2", "Tambah data mahasiswa"])
    tabel.add_row(["3", "Keluar"])
    print(tabel)

    pilihan = input("Masukkan pilihan (1/2/3): ")
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        print(tambah_data())
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid!")
