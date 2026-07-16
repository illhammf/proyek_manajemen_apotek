class Obat:
    """Class utama untuk data obat.

    Konsep OOP:
    - Encapsulation: nama, kategori, harga, stok, dan expired dibuat private.
    - Polymorphism: method info_jual() dioverride oleh ObatBebas dan ObatResep.
    """

    def __init__(self, kode_obat: str, nama: str, kategori: str, harga: float, stok: int, expired: str):
        self._kode_obat = kode_obat
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = float(harga)
        self.__stok = int(stok)
        self.__expired = expired

    def get_kode_obat(self):
        return self._kode_obat

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama: str):
        if not nama.strip():
            raise ValueError("Nama obat tidak boleh kosong.")
        self.__nama = nama

    def get_kategori(self):
        return self.__kategori

    def set_kategori(self, kategori: str):
        self.__kategori = kategori

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga: float):
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif.")
        self.__harga = float(harga)

    def get_stok(self):
        return self.__stok

    def set_stok(self, stok: int):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif.")
        self.__stok = int(stok)

    def get_expired(self):
        return self.__expired

    def set_expired(self, expired: str):
        self.__expired = expired

    def tambah_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah tambah stok harus lebih dari 0.")
        self.__stok += jumlah

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah pengurangan stok harus lebih dari 0.")
        if jumlah > self.__stok:
            raise ValueError("Stok obat tidak mencukupi.")
        self.__stok -= jumlah

    def hitung_nilai_stok(self):
        return self.__harga * self.__stok

    def info_jual(self):
        return f"{self.__nama} dapat dijual sesuai aturan apotek."

    def to_dict(self):
        return {
            "tipe": self.__class__.__name__,
            "kode_obat": self._kode_obat,
            "nama": self.__nama,
            "kategori": self.__kategori,
            "harga": self.__harga,
            "stok": self.__stok,
            "expired": self.__expired,
        }

    @staticmethod
    def from_dict(data):
        tipe = data.get("tipe", "Obat")
        if tipe == "ObatResep":
            return ObatResep(**{k: data[k] for k in ["kode_obat", "nama", "kategori", "harga", "stok", "expired"]})
        if tipe == "ObatBebas":
            return ObatBebas(**{k: data[k] for k in ["kode_obat", "nama", "kategori", "harga", "stok", "expired"]})
        return Obat(**{k: data[k] for k in ["kode_obat", "nama", "kategori", "harga", "stok", "expired"]})


class ObatBebas(Obat):
    """Turunan Obat untuk obat yang bisa dibeli tanpa resep."""

    def info_jual(self):
        return f"{self.get_nama()} adalah obat bebas. Bisa dijual tanpa resep dokter."


class ObatResep(Obat):
    """Turunan Obat untuk obat yang wajib menggunakan resep."""

    def info_jual(self):
        return f"{self.get_nama()} adalah obat resep. Penjualan wajib memakai resep dokter."
