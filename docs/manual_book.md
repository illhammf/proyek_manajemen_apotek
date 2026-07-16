# Manual Book Sistem Manajemen Apotek

## 1. Persiapan

Pastikan Python sudah terpasang di komputer. Buka folder proyek menggunakan VS Code.

## 2. Menjalankan Program

Buka terminal VS Code, lalu jalankan:

```bash
python main.py
```

## 3. Menu Program

Program menampilkan menu utama:

1. Lihat data obat.
2. Tambah obat.
3. Cari obat.
4. Update stok obat.
5. Hapus obat.
6. Lihat data pelanggan.
7. Tambah pelanggan.
8. Buat transaksi penjualan.
9. Laporan stok.
10. Laporan penjualan.
11. Simpan data.
0. Keluar.

## 4. Menambah Obat

Pilih menu 2. Masukkan kode obat, nama obat, kategori, harga, stok, tanggal expired, dan tipe obat. Tipe obat terdiri dari `bebas` dan `resep`.

## 5. Mencari Obat

Pilih menu 3. Masukkan nama atau kategori obat. Sistem akan menampilkan obat yang sesuai.

## 6. Update Stok Obat

Pilih menu 4. Masukkan kode obat dan stok baru. Sistem akan memperbarui stok jika kode obat ditemukan.

## 7. Membuat Transaksi

Pilih menu 8. Masukkan kode transaksi, ID pelanggan, dan ID apoteker. Setelah itu masukkan kode obat dan jumlah pembelian. Ketik `selesai` untuk menyelesaikan input item.

Setelah transaksi disimpan, stok obat otomatis berkurang.

## 8. Laporan

Menu 9 menampilkan laporan stok obat. Menu 10 menampilkan laporan penjualan.

## 9. Penyimpanan Data

Menu 11 menyimpan data ke folder `data` dalam format JSON. Saat program dijalankan ulang, data akan dimuat kembali.

## 10. Pengujian

Jalankan pengujian dengan perintah:

```bash
python tests/test_apotek.py
```
