class Resep:
    """Class komposisi untuk transaksi obat resep."""

    def __init__(self, kode_resep: str, dokter: str, pasien: str):
        self.__kode_resep = kode_resep
        self.__dokter = dokter
        self.__pasien = pasien
        self.__daftar_obat = []

    def get_kode_resep(self):
        return self.__kode_resep

    def get_dokter(self):
        return self.__dokter

    def set_dokter(self, dokter: str):
        self.__dokter = dokter

    def get_pasien(self):
        return self.__pasien

    def set_pasien(self, pasien: str):
        self.__pasien = pasien

    def tambah_obat(self, nama_obat: str):
        self.__daftar_obat.append(nama_obat)

    def get_daftar_obat(self):
        return self.__daftar_obat

    def tampilkan_resep(self):
        daftar = ", ".join(self.__daftar_obat) if self.__daftar_obat else "Belum ada obat"
        return f"Resep {self.__kode_resep} | Dokter: {self.__dokter} | Pasien: {self.__pasien} | Obat: {daftar}"

    def to_dict(self):
        return {
            "kode_resep": self.__kode_resep,
            "dokter": self.__dokter,
            "pasien": self.__pasien,
            "daftar_obat": self.__daftar_obat,
        }

    @staticmethod
    def from_dict(data):
        resep = Resep(data["kode_resep"], data["dokter"], data["pasien"])
        for obat in data.get("daftar_obat", []):
            resep.tambah_obat(obat)
        return resep
