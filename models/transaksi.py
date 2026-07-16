from datetime import datetime


class DetailTransaksi:
    """Item transaksi. Satu detail berisi satu objek Obat dan jumlah pembelian."""

    def __init__(self, obat, jumlah: int):
        self.__obat = obat
        self.__jumlah = int(jumlah)

    def get_obat(self):
        return self.__obat

    def get_jumlah(self):
        return self.__jumlah

    def set_jumlah(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah pembelian harus lebih dari 0.")
        self.__jumlah = int(jumlah)

    def hitung_subtotal(self):
        return self.__obat.get_harga() * self.__jumlah

    def to_dict(self):
        return {
            "kode_obat": self.__obat.get_kode_obat(),
            "nama_obat": self.__obat.get_nama(),
            "harga": self.__obat.get_harga(),
            "jumlah": self.__jumlah,
            "subtotal": self.hitung_subtotal(),
        }


class Transaksi:
    """Class transaksi penjualan obat.

    Konsep composition terlihat jelas di sini:
    - Transaksi memiliki object Pelanggan.
    - Transaksi memiliki object Apoteker.
    - Transaksi memiliki banyak object DetailTransaksi.
    """

    def __init__(self, kode_transaksi: str, pelanggan, apoteker, metode_bayar: str = "Tunai"):
        self.__kode_transaksi = kode_transaksi
        self.__tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__pelanggan = pelanggan
        self.__apoteker = apoteker
        self.__metode_bayar = metode_bayar
        self.__detail = []
        self.__status = "Draft"

    def get_kode_transaksi(self):
        return self.__kode_transaksi

    def get_tanggal(self):
        return self.__tanggal

    def get_pelanggan(self):
        return self.__pelanggan

    def get_apoteker(self):
        return self.__apoteker

    def get_status(self):
        return self.__status

    def tambah_detail(self, obat, jumlah: int):
        if jumlah > obat.get_stok():
            raise ValueError("Stok tidak cukup untuk transaksi.")
        self.__detail.append(DetailTransaksi(obat, jumlah))

    def hapus_detail(self, kode_obat: str):
        self.__detail = [d for d in self.__detail if d.get_obat().get_kode_obat() != kode_obat]

    def hitung_total_kotor(self):
        return sum(item.hitung_subtotal() for item in self.__detail)

    def hitung_diskon(self):
        return self.__pelanggan.hitung_diskon_member(self.hitung_total_kotor())

    def hitung_total_bayar(self):
        return self.hitung_total_kotor() - self.hitung_diskon()

    def proses_pembayaran(self):
        if not self.__detail:
            raise ValueError("Transaksi belum memiliki item obat.")
        for item in self.__detail:
            item.get_obat().kurangi_stok(item.get_jumlah())
        self.__status = "Lunas"

    def cetak_struk(self):
        garis = "=" * 46
        rows = [garis, "STRUK APOTEK SEHAT", garis]
        rows.append(f"Kode     : {self.__kode_transaksi}")
        rows.append(f"Tanggal  : {self.__tanggal}")
        rows.append(f"Pelanggan: {self.__pelanggan.get_nama()}")
        rows.append(f"Apoteker : {self.__apoteker.get_nama()}")
        rows.append("-" * 46)
        for item in self.__detail:
            rows.append(f"{item.get_obat().get_nama()} x{item.get_jumlah()} = Rp{item.hitung_subtotal():,.0f}")
        rows.append("-" * 46)
        rows.append(f"Total kotor : Rp{self.hitung_total_kotor():,.0f}")
        rows.append(f"Diskon      : Rp{self.hitung_diskon():,.0f}")
        rows.append(f"Total bayar : Rp{self.hitung_total_bayar():,.0f}")
        rows.append(f"Status      : {self.__status}")
        rows.append(garis)
        return "\n".join(rows)

    def to_dict(self):
        return {
            "kode_transaksi": self.__kode_transaksi,
            "tanggal": self.__tanggal,
            "pelanggan": self.__pelanggan.to_dict(),
            "apoteker": self.__apoteker.to_dict(),
            "metode_bayar": self.__metode_bayar,
            "status": self.__status,
            "detail": [item.to_dict() for item in self.__detail],
            "total_bayar": self.hitung_total_bayar(),
        }
