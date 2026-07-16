from services.apotek import Apotek
from models.obat import ObatBebas, ObatResep
from models.pelanggan import Pelanggan
from models.apoteker import Apoteker
from models.resep import Resep


# ==========================================================
# PROGRAM UTAMA SISTEM MANAJEMEN APOTEK
# Jalankan file ini di VS Code dengan perintah:
# python main.py
# ==========================================================


def garis():
    print("=" * 60)


def tampilkan_menu():
    garis()
    print("SISTEM MANAJEMEN APOTEK SEHAT")
    garis()
    print("1. Lihat data obat")
    print("2. Tambah obat")
    print("3. Cari obat")
    print("4. Update stok obat")
    print("5. Hapus obat")
    print("6. Lihat data pelanggan")
    print("7. Tambah pelanggan")
    print("8. Buat transaksi penjualan")
    print("9. Laporan stok")
    print("10. Laporan penjualan")
    print("11. Simpan data")
    print("0. Keluar")
    garis()


def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka.")


def lihat_obat(apotek):
    daftar = apotek.get_semua_obat()
    if not daftar:
        print("Belum ada data obat.")
        return
    for obat in daftar:
        print(f"{obat.get_kode_obat()} | {obat.get_nama()} | {obat.get_kategori()} | Rp{obat.get_harga():,.0f} | Stok: {obat.get_stok()} | {obat.info_jual()}")


def tambah_obat(apotek):
    kode = input("Kode obat: ")
    nama = input("Nama obat: ")
    kategori = input("Kategori: ")
    harga = float(input("Harga: "))
    stok = int(input("Stok: "))
    expired = input("Tanggal expired YYYY-MM-DD: ")
    tipe = input("Tipe obat [bebas/resep]: ").lower()

    if tipe == "resep":
        obat = ObatResep(kode, nama, kategori, harga, stok, expired)
    else:
        obat = ObatBebas(kode, nama, kategori, harga, stok, expired)

    apotek.tambah_obat(obat)
    print("Data obat berhasil ditambahkan.")


def cari_obat(apotek):
    kata = input("Masukkan nama/kategori obat: ")
    hasil = apotek.cari_obat(kata)
    if not hasil:
        print("Obat tidak ditemukan.")
        return
    for obat in hasil:
        print(f"{obat.get_kode_obat()} | {obat.get_nama()} | Stok: {obat.get_stok()}")


def update_stok(apotek):
    kode = input("Kode obat: ")
    stok = input_angka("Stok baru: ")
    if apotek.update_stok_obat(kode, stok):
        print("Stok berhasil diperbarui.")
    else:
        print("Kode obat tidak ditemukan.")


def hapus_obat(apotek):
    kode = input("Kode obat yang akan dihapus: ")
    if apotek.hapus_obat(kode):
        print("Data obat berhasil dihapus.")
    else:
        print("Kode obat tidak ditemukan.")


def lihat_pelanggan(apotek):
    for pelanggan in apotek.get_semua_pelanggan():
        print(pelanggan.tampilkan_info())


def tambah_pelanggan(apotek):
    idp = input("ID pelanggan: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    telepon = input("Telepon: ")
    member = input("Member? [y/n]: ").lower() == "y"
    apotek.tambah_pelanggan(Pelanggan(idp, nama, alamat, telepon, member))
    print("Pelanggan berhasil ditambahkan.")


def buat_transaksi(apotek):
    kode = input("Kode transaksi: ")
    id_pelanggan = input("ID pelanggan: ")
    id_apoteker = input("ID apoteker: ")
    transaksi = apotek.buat_transaksi(kode, id_pelanggan, id_apoteker)

    while True:
        kode_obat = input("Kode obat [ketik selesai untuk berhenti]: ")
        if kode_obat.lower() == "selesai":
            break
        obat = apotek.cari_obat_by_kode(kode_obat)
        if obat is None:
            print("Obat tidak ditemukan.")
            continue
        jumlah = input_angka("Jumlah: ")
        transaksi.tambah_detail(obat, jumlah)
        print("Item berhasil ditambahkan.")

    apotek.simpan_transaksi(transaksi)
    print(transaksi.cetak_struk())


def main():
    apotek = Apotek("Apotek Sehat", "Jl. Kesehatan No. 10")
    apotek.muat_data()
    apotek.seed_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                lihat_obat(apotek)
            elif pilihan == "2":
                tambah_obat(apotek)
            elif pilihan == "3":
                cari_obat(apotek)
            elif pilihan == "4":
                update_stok(apotek)
            elif pilihan == "5":
                hapus_obat(apotek)
            elif pilihan == "6":
                lihat_pelanggan(apotek)
            elif pilihan == "7":
                tambah_pelanggan(apotek)
            elif pilihan == "8":
                buat_transaksi(apotek)
            elif pilihan == "9":
                print(apotek.generate_laporan_stok())
            elif pilihan == "10":
                print(apotek.generate_laporan_penjualan())
            elif pilihan == "11":
                apotek.simpan_data()
                print("Data berhasil disimpan ke folder data.")
            elif pilihan == "0":
                apotek.simpan_data()
                print("Terima kasih. Program selesai.")
                break
            else:
                print("Pilihan tidak tersedia.")
        except Exception as error:
            print(f"Terjadi error: {error}")


if __name__ == "__main__":
    main()
