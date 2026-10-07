# studi_kasus_6_Nabilah-rahmadhani

nama: Nabilah Rahmadhani

NIM: 2609116041

kelas: B

# Penjelasan Kode Program

Program ini merupakan sistem sederhana untuk mengelola data nilai mahasiswa menggunakan bahasa pemrograman Python. Data mahasiswa disimpan dalam file json, sehingga data yang ditambahkan dapat tersimpan secara permanen dan tetap tersedia ketika program dijalankan kembali.

1. Import Library
   
   ```python
   import json
   from prettytable import PrettyTable
   ```
   
   `json` digunakan untuk membaca dan menyimpan data dalam format JSON. Sementara itu, `PrettyTable` digunakan untuk membuat tampilan menu program dalam bentuk tabel agar lebih rapi.

2. **Membaca File JSON**
   
   ```python
   with open("mahasiswa.json", "r", encoding="utf-8") as f:
       data = json.load(f)
   ```
   
   Bagian ini digunakan untuk membuka file `mahasiswa.json` dalam mode baca (`"r"`). Fungsi `json.load()` digunakan untuk mengambil data dari file JSON dan menyimpannya ke dalam variabel `data`.

3. **Fungsi `tampilkan_data()`**
   
   ```python
   def tampilkan_data():
   ```
   
   Fungsi ini digunakan untuk menampilkan seluruh data mahasiswa yang terdapat dalam file JSON. Program melakukan pengecekan terlebih dahulu menggunakan `if not data` untuk mengetahui apakah data mahasiswa tersedia. Jika tersedia, data ditampilkan menggunakan perulangan `for`.

4. **Fungsi `simpan_file()`**
   
   ```python
   def simpan_file():
       with open("mahasiswa.json", "w", encoding="utf-8") as f:
           json.dump(data, f, indent=4)
   ```
   
   Fungsi ini digunakan untuk menyimpan data ke dalam file `mahasiswa.json`. Mode `"w"` digunakan untuk menulis atau memperbarui isi file, sedangkan `json.dump()` mengubah data Python menjadi format JSON. `indent=4` digunakan agar isi file JSON tersusun lebih rapi.

5. **Fungsi `tambah_data()`**
   
   ```python
   def tambah_data():
   ```
   
   Fungsi ini digunakan untuk menambahkan data mahasiswa baru. Pengguna diminta memasukkan nama, NIM, program studi, mata kuliah, dan nilai. Nilai diperiksa menggunakan `isdigit()` agar hanya berupa angka.

   Setelah data dimasukkan, data ditambahkan ke dalam list menggunakan:

   ```python
   data.append({
       "nama": nama,
       "nim": nim,
       "prodi": prodi,
       "mata kuliah": matkul,
       "nilai": nilai
   })
   ```

   Setelah data ditambahkan, fungsi `simpan_file()` langsung dipanggil sehingga data baru **otomatis tersimpan secara permanen** ke dalam file `mahasiswa.json`.

6. **Perulangan `while`**
   
   ```python
   while True:
   ```
   
   Perulangan ini digunakan agar program terus berjalan dan menampilkan menu sampai pengguna memilih pilihan **3 (Keluar)**.

7. **PrettyTable**
   
   ```python
   tabel = PrettyTable()
   tabel.field_names = ["No", "Menu"]
   ```
   
   `PrettyTable` digunakan untuk membuat tampilan menu dalam bentuk tabel sehingga lebih terstruktur dan mudah dibaca.

8. **Percabangan Menu**
   
   ```python
   if pilihan == "1":
       tampilkan_data()
   elif pilihan == "2":
       print(tambah_data())
   elif pilihan == "3":
       print("Terima kasih telah menggunakan program ini!")
       break
   ```
   
   Percabangan digunakan untuk menentukan tindakan berdasarkan pilihan pengguna. Pilihan **1** digunakan untuk menampilkan data, pilihan **2** untuk menambahkan data baru, dan pilihan **3** untuk keluar dari program. Perintah `break` digunakan untuk menghentikan perulangan `while`.

### Kesimpulan Singkat

Secara keseluruhan, program ini berfungsi untuk membaca, menampilkan, dan menambahkan data nilai mahasiswa. Data baru yang dimasukkan akan langsung disimpan ke file `mahasiswa.json`, sehingga data tidak hilang ketika program ditutup dan dijalankan kembali.

# TAMPILAN AWAL
<img width="295" height="135" alt="Screenshot 2026-10-08 023853" src="https://github.com/user-attachments/assets/12a5cfd5-2106-4607-ac2c-1f2d84b4512a" />

# MENU 1
<img width="356" height="68" alt="Screenshot 2026-10-08 023916" src="https://github.com/user-attachments/assets/e3e10a42-eaad-4dea-8a52-104ea8148826" />

# MENU 2
<img width="326" height="209" alt="Screenshot 2026-10-08 024412" src="https://github.com/user-attachments/assets/35aba493-d908-452b-9d12-ac90e6fb42fc" />

# MENU 3
<img width="347" height="130" alt="Screenshot 2026-10-08 024422" src="https://github.com/user-attachments/assets/8754b0ff-a2de-49f8-80c8-c32b3dd3f635" />





