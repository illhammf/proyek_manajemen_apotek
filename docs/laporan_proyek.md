# Laporan Proyek Akhir

## Sistem Manajemen Apotek Berbasis Object-Oriented Programming

## 1. Latar Belakang

Apotek memerlukan sistem sederhana untuk mengelola obat, pelanggan, apoteker, transaksi, dan laporan. Pengelolaan manual berisiko menimbulkan kesalahan pencatatan stok dan transaksi. Sistem berbasis Python dapat membantu proses pengelolaan data secara lebih terstruktur.

Proyek ini menggunakan pendekatan Object-Oriented Programming. Pendekatan ini sesuai karena data apotek dapat dimodelkan sebagai object, seperti obat, pelanggan, apoteker, resep, dan transaksi.

## 2. Rumusan Masalah

1. Bagaimana merancang sistem manajemen apotek sederhana menggunakan Python?
2. Bagaimana menerapkan konsep OOP pada sistem manajemen apotek?
3. Bagaimana sistem dapat membantu pencatatan obat, pelanggan, transaksi, dan laporan?

## 3. Tujuan

1. Membuat aplikasi manajemen apotek berbasis Python.
2. Menerapkan class, object, inheritance, encapsulation, polymorphism, composition, constructor, dan method.
3. Menyediakan fitur pengelolaan obat, pelanggan, transaksi, stok, dan laporan.

## 4. Analisis Kebutuhan

### 4.1 Kebutuhan Fungsional

1. Sistem dapat menampilkan data obat.
2. Sistem dapat menambah data obat.
3. Sistem dapat mencari obat.
4. Sistem dapat memperbarui stok obat.
5. Sistem dapat menghapus obat.
6. Sistem dapat menampilkan dan menambah pelanggan.
7. Sistem dapat membuat transaksi penjualan.
8. Sistem dapat menghitung diskon member.
9. Sistem dapat membuat laporan stok.
10. Sistem dapat membuat laporan penjualan.
11. Sistem dapat menyimpan dan memuat data JSON.

### 4.2 Kebutuhan Nonfungsional

1. Program dapat dijalankan melalui terminal VS Code.
2. Kode program diberi komentar agar mudah dipahami.
3. Struktur folder dipisahkan berdasarkan fungsi.
4. Data dapat disimpan secara lokal.

## 5. Desain Class

Class yang digunakan adalah `Person`, `Apoteker`, `Pelanggan`, `Obat`, `ObatBebas`, `ObatResep`, `Resep`, `DetailTransaksi`, `Transaksi`, `Apotek`, `FileManager`, dan `Laporan`.

Class `Person` menjadi class induk untuk `Apoteker` dan `Pelanggan`. Class `Obat` menjadi class induk untuk `ObatBebas` dan `ObatResep`. Class `Apotek` menjadi class utama yang mengelola seluruh data.

## 6. Implementasi OOP

### 6.1 Class dan Object

Program memiliki lebih dari enam class. Object dibuat dari class tersebut saat program berjalan.

### 6.2 Inheritance

Inheritance diterapkan pada relasi `Apoteker` dan `Pelanggan` terhadap `Person`, serta `ObatBebas` dan `ObatResep` terhadap `Obat`.

### 6.3 Encapsulation

Atribut penting dibuat private menggunakan tanda `__`. Data diakses melalui getter dan setter.

### 6.4 Polymorphism

Polymorphism diterapkan pada method `tampilkan_info()` dan `info_jual()` yang memiliki perilaku berbeda di class turunan.

### 6.5 Composition

Composition diterapkan karena `Transaksi` memiliki object `Pelanggan`, object `Apoteker`, dan beberapa object `DetailTransaksi`.

## 7. Fitur Program

1. Manajemen obat.
2. Manajemen pelanggan.
3. Manajemen apoteker.
4. Transaksi penjualan obat.
5. Diskon member.
6. Laporan stok dan laporan penjualan.
7. Penyimpanan data JSON.

## 8. Pengujian

Pengujian dilakukan pada lima skenario:

1. Tambah dan cari obat.
2. Update stok obat.
3. Transaksi mengurangi stok.
4. Diskon member.
5. Validasi resep.

Seluruh skenario pengujian berjalan dengan baik.

## 9. Kesimpulan

Sistem Manajemen Apotek berhasil dibuat menggunakan Python dan pendekatan Object-Oriented Programming. Program memenuhi kebutuhan minimal proyek, yaitu memiliki lebih dari enam class, menerapkan object, inheritance, encapsulation, polymorphism, composition, constructor, dan lebih dari dua puluh method.

Sistem dapat digunakan untuk mengelola obat, pelanggan, apoteker, transaksi, stok, dan laporan. Struktur program juga sudah dipisahkan ke dalam folder `models`, `services`, `tests`, dan `docs` agar lebih mudah dipahami serta dikembangkan.
