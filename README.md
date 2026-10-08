# studi_kasus_6_Nabilah-rahmadhani

nama: Nabilah Rahmadhani

NIM: 2609116041

kelas: B

# Penjelasan Kode Program

Program ini merupakan sistem sederhana untuk mengelola data nilai mahasiswa menggunakan bahasa pemrograman Python. Data mahasiswa disimpan dalam file json, sehingga data yang ditambahkan dapat tersimpan secara permanen dan tetap tersedia ketika program dijalankan kembali.

1. Import Library
<img width="265" height="35" alt="image" src="https://github.com/user-attachments/assets/75c8e185-5545-4960-931e-8ad865ed1e1c" />

json digunakan untuk membaca dan menyimpan data dalam format JSON. Sementara itu, PrettyTable digunakan untuk membuat tampilan menu program dalam bentuk tabel agar lebih rapi.

2. Membaca File JSON
<img width="449" height="35" alt="image" src="https://github.com/user-attachments/assets/78501c4f-630d-4451-82cc-a95e82bfa266" />

Bagian ini digunakan untuk membuka file mahasiswa.json dalam mode baca ("r"). Fungsi json.load() digunakan untuk mengambil data dari file JSON dan menyimpannya ke dalam variabel data.

3. Fungsi tampilkan_data()
   
<img width="536" height="123" alt="image" src="https://github.com/user-attachments/assets/e3749e6a-41c0-4fc1-8f8c-4a8881f36dc6" />

Fungsi ini digunakan untuk menampilkan seluruh data mahasiswa yang terdapat dalam file JSON. Program melakukan pengecekan terlebih dahulu menggunakan if not data untuk mengetahui apakah data mahasiswa tersedia. Jika tersedia, data ditampilkan menggunakan perulangan for.

4. Fungsi simpan_file()
<img width="462" height="68" alt="image" src="https://github.com/user-attachments/assets/c43744a8-3279-4bb4-8c76-c1c39eba1e9d" />
 
Fungsi ini digunakan untuk menyimpan data ke dalam file mahasiswa.json. Mode w digunakan untuk menulis atau memperbarui isi file, sedangkan json.dump() mengubah data Python menjadi format JSON. indent=4 digunakan agar isi file JSON tersusun lebih rapi.

5. Fungsi tambah_data()

<img width="475" height="318" alt="image" src="https://github.com/user-attachments/assets/2075f876-d6b4-463d-af66-c211d0491ab9" />

Fungsi ini digunakan untuk menambahkan data mahasiswa baru. Pengguna diminta memasukkan nama, NIM, program studi, mata kuliah, dan nilai. Nilai diperiksa menggunakan isdigit() agar hanya berupa angka. Setelah data dimasukkan, data ditambahkan ke dalam list menggunakan:
Setelah data ditambahkan, fungsi simpan_file() langsung dipanggil sehingga data baru otomatis tersimpan secara permanen ke dalam file mahasiswa.json.

6. Perulangan while

 <img width="488" height="282" alt="image" src="https://github.com/user-attachments/assets/b366d206-d182-4bf5-96ee-b1f59a100fa4" />

Perulangan ini digunakan agar program terus berjalan dan menampilkan menu sampai pengguna memilih pilihan 3 (Keluar)
program ini berfungsi untuk membaca, menampilkan, dan menambahkan data nilai mahasiswa. Data baru yang dimasukkan akan langsung disimpan ke file mahasiswa.json, sehingga data tidak hilang ketika program ditutup dan dijalankan kembali.

# TAMPILAN AWAL

<img width="295" height="135" alt="Screenshot 2026-10-08 023853" src="https://github.com/user-attachments/assets/12a5cfd5-2106-4607-ac2c-1f2d84b4512a" />

PrettyTable` digunakan untuk membuat tampilan menu dalam bentuk tabel sehingga lebih terstruktur dan mudah dibaca.

# MENU 1

<img width="356" height="68" alt="Screenshot 2026-10-08 023916" src="https://github.com/user-attachments/assets/e3e10a42-eaad-4dea-8a52-104ea8148826" />

menampilkan seluruh data mahasiswa

# MENU 2
<img width="326" height="209" alt="Screenshot 2026-10-08 024412" src="https://github.com/user-attachments/assets/35aba493-d908-452b-9d12-ac90e6fb42fc" />

menambahkan sebuah data nilai mahasiswa baru

# MENU 3
<img width="347" height="130" alt="Screenshot 2026-10-08 024422" src="https://github.com/user-attachments/assets/8754b0ff-a2de-49f8-80c8-c32b3dd3f635" />

sistem akan keluar dari program





