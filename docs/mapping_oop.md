# Mapping Konsep OOP

## 1. Class

Class utama yang digunakan:

1. Person
2. Apoteker
3. Pelanggan
4. Obat
5. ObatBebas
6. ObatResep
7. Resep
8. DetailTransaksi
9. Transaksi
10. Apotek
11. FileManager
12. Laporan

## 2. Object

Object dibuat saat program berjalan, misalnya:

- `Apotek("Apotek Sehat", "Jl. Kesehatan No. 10")`
- `Apoteker("APT001", "Rina Marlina", ...)`
- `Pelanggan("PLG001", "Andi Saputra", ...)`
- `ObatBebas("OBT001", "Paracetamol 500mg", ...)`
- `ObatResep("OBT003", "Amoxicillin 500mg", ...)`

## 3. Inheritance

Inheritance diterapkan pada:

- `Apoteker(Person)`
- `Pelanggan(Person)`
- `ObatBebas(Obat)`
- `ObatResep(Obat)`

## 4. Encapsulation

Atribut private digunakan agar data tidak diakses langsung dari luar class. Contoh:

- `self.__nama`
- `self.__alamat`
- `self.__telepon`
- `self.__harga`
- `self.__stok`
- `self.__riwayat_transaksi`

Akses data dilakukan melalui getter dan setter.

## 5. Polymorphism

Polymorphism diterapkan melalui method override:

- `tampilkan_info()` pada `Apoteker` dan `Pelanggan`.
- `info_jual()` pada `ObatBebas` dan `ObatResep`.

## 6. Composition

Composition diterapkan pada class `Transaksi`.

Class `Transaksi` memiliki:

- Object `Pelanggan`.
- Object `Apoteker`.
- List object `DetailTransaksi`.

Class `Apotek` juga menyimpan kumpulan object dari class lain.

## 7. Constructor

Semua class utama memakai constructor `__init__()` untuk menginisialisasi atribut.

## 8. Method

Total method lebih dari 20. Method tersebar di class Person, Apoteker, Pelanggan, Obat, Resep, Transaksi, Apotek, FileManager, dan Laporan.
