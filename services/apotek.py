from models.apoteker import Apoteker
from models.pelanggan import Pelanggan
from models.obat import Obat, ObatBebas, ObatResep
from models.resep import Resep
from models.transaksi import Transaksi
from services.file_manager import FileManager, Laporan


class Apotek:
    """Class pusat yang mengelola seluruh data dan proses bisnis apotek."""

    def __init__(self, nama_apotek: str, alamat: str):
        self.__nama_apotek = nama_apotek
        self.__alamat = alamat
        self.__apoteker = []
        self.__pelanggan = []
        self.__obat = []
        self.__resep = []
        self.__riwayat_transaksi = []

    def get_nama_apotek(self):
        return self.__nama_apotek

    def get_alamat(self):
        return self.__alamat

    def tambah_apoteker(self, apoteker: Apoteker):
        self.__apoteker.append(apoteker)

    def tambah_pelanggan(self, pelanggan: Pelanggan):
        self.__pelanggan.append(pelanggan)

    def tambah_obat(self, obat: Obat):
        self.__obat.append(obat)

    def tambah_resep(self, resep: Resep):
        self.__resep.append(resep)

    def get_semua_apoteker(self):
        return self.__apoteker

    def get_semua_pelanggan(self):
        return self.__pelanggan

    def get_semua_obat(self):
        return self.__obat

    def get_riwayat_transaksi(self):
        return self.__riwayat_transaksi

    def cari_obat(self, kata_kunci: str):
        kata = kata_kunci.lower()
        return [obat for obat in self.__obat if kata in obat.get_nama().lower() or kata in obat.get_kategori().lower()]

    def cari_obat_by_kode(self, kode_obat: str):
        for obat in self.__obat:
            if obat.get_kode_obat() == kode_obat:
                return obat
        return None

    def cari_pelanggan_by_id(self, id_person: str):
        for pelanggan in self.__pelanggan:
            if pelanggan.get_id_person() == id_person:
                return pelanggan
        return None

    def cari_apoteker_by_id(self, id_person: str):
        for apoteker in self.__apoteker:
            if apoteker.get_id_person() == id_person:
                return apoteker
        return None

    def update_stok_obat(self, kode_obat: str, stok_baru: int):
        obat = self.cari_obat_by_kode(kode_obat)
        if obat is None:
            return False
        obat.set_stok(stok_baru)
        return True

    def hapus_obat(self, kode_obat: str):
        jumlah_awal = len(self.__obat)
        self.__obat = [obat for obat in self.__obat if obat.get_kode_obat() != kode_obat]
        return len(self.__obat) < jumlah_awal

    def buat_transaksi(self, kode_transaksi: str, id_pelanggan: str, id_apoteker: str, metode_bayar: str = "Tunai"):
        pelanggan = self.cari_pelanggan_by_id(id_pelanggan)
        apoteker = self.cari_apoteker_by_id(id_apoteker)
        if pelanggan is None:
            raise ValueError("Pelanggan tidak ditemukan.")
        if apoteker is None:
            raise ValueError("Apoteker tidak ditemukan.")
        return Transaksi(kode_transaksi, pelanggan, apoteker, metode_bayar)

    def simpan_transaksi(self, transaksi: Transaksi):
        transaksi.proses_pembayaran()
        self.__riwayat_transaksi.append(transaksi.to_dict())

    def generate_laporan_stok(self):
        return Laporan.laporan_stok(self.__obat)

    def generate_laporan_penjualan(self):
        return Laporan.laporan_penjualan(self.__riwayat_transaksi)

    def simpan_data(self, folder_data="data"):
        FileManager.save_json(f"{folder_data}/apoteker.json", [a.to_dict() for a in self.__apoteker])
        FileManager.save_json(f"{folder_data}/pelanggan.json", [p.to_dict() for p in self.__pelanggan])
        FileManager.save_json(f"{folder_data}/obat.json", [o.to_dict() for o in self.__obat])
        FileManager.save_json(f"{folder_data}/resep.json", [r.to_dict() for r in self.__resep])
        FileManager.save_json(f"{folder_data}/transaksi.json", self.__riwayat_transaksi)

    def muat_data(self, folder_data="data"):
        self.__apoteker = [Apoteker.from_dict(d) for d in FileManager.load_json(f"{folder_data}/apoteker.json", [])]
        self.__pelanggan = [Pelanggan.from_dict(d) for d in FileManager.load_json(f"{folder_data}/pelanggan.json", [])]
        self.__obat = [Obat.from_dict(d) for d in FileManager.load_json(f"{folder_data}/obat.json", [])]
        self.__resep = [Resep.from_dict(d) for d in FileManager.load_json(f"{folder_data}/resep.json", [])]
        self.__riwayat_transaksi = FileManager.load_json(f"{folder_data}/transaksi.json", [])

    def seed_data(self):
        """Data awal agar aplikasi langsung bisa dicoba saat demo."""
        if not self.__apoteker:
            self.tambah_apoteker(Apoteker("APT001", "Rina Marlina", "Jl. Melati 1", "081234567890", "SIP-APT-001", "Pagi"))
            self.tambah_apoteker(Apoteker("APT002", "Budi Santoso", "Jl. Mawar 2", "081222333444", "SIP-APT-002", "Sore"))
        if not self.__pelanggan:
            self.tambah_pelanggan(Pelanggan("PLG001", "Andi Saputra", "Jl. Kenanga 3", "082111223344", True))
            self.tambah_pelanggan(Pelanggan("PLG002", "Siti Aminah", "Jl. Anggrek 4", "085555667788", False))
        if not self.__obat:
            self.tambah_obat(ObatBebas("OBT001", "Paracetamol 500mg", "Analgesik", 6000, 50, "2027-12-31"))
            self.tambah_obat(ObatBebas("OBT002", "Vitamin C", "Suplemen", 12000, 35, "2027-06-30"))
            self.tambah_obat(ObatResep("OBT003", "Amoxicillin 500mg", "Antibiotik", 18000, 40, "2027-03-31"))
