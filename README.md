# Sistem Manajemen Apotek Berbasis Object-Oriented Programming

Proyek ini dibuat untuk tugas Bahasa Pemrograman dengan studi kasus Sistem Manajemen Apotek. Program ditulis menggunakan Python dan menerapkan konsep Object-Oriented Programming.

## Fitur Utama

1. Mengelola data obat.
2. Mengelola data pelanggan.
3. Mengelola data apoteker.
4. Mencari obat berdasarkan nama atau kategori.
5. Memperbarui stok obat.
6. Menghapus data obat.
7. Membuat transaksi penjualan obat.
8. Menghitung diskon member.
9. Mengurangi stok otomatis setelah transaksi lunas.
10. Membuat laporan stok dan laporan penjualan.
11. Menyimpan data ke file JSON.

## Cara Menjalankan di VS Code

Buka folder proyek ini di VS Code, lalu jalankan perintah berikut di terminal:

```bash
python main.py
```

Jika menggunakan Windows dan perintah `python` tidak aktif, gunakan:

```bash
py main.py
```

## Cara Menjalankan Pengujian

```bash
python tests/test_apotek.py
```

## Struktur Folder

```text
Sistem_Manajemen_Apotek_OOP/
├── main.py
├── models/
│   ├── person.py
│   ├── apoteker.py
│   ├── pelanggan.py
│   ├── obat.py
│   ├── resep.py
│   └── transaksi.py
├── services/
│   ├── apotek.py
│   └── file_manager.py
├── tests/
│   └── test_apotek.py
├── docs/
├── presentation/
├── poster/
└── data/
```

## Akun dan Data Awal

Program menggunakan data awal otomatis, yaitu dua apoteker, dua pelanggan, dan tiga obat.

## Penerapan OOP

- Class: lebih dari 6 class.
- Object: setiap class utama dibuat dan digunakan.
- Inheritance: `Apoteker` dan `Pelanggan` mewarisi `Person`; `ObatBebas` dan `ObatResep` mewarisi `Obat`.
- Encapsulation: atribut private memakai `__nama`, `__alamat`, `__stok`, dan atribut lain.
- Polymorphism: method `tampilkan_info()` dan `info_jual()` dioverride.
- Composition: `Transaksi` memiliki object `Pelanggan`, `Apoteker`, dan `DetailTransaksi`.
- Constructor: setiap class memakai `__init__()`.
- Method: lebih dari 20 method relevan.
