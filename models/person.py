from abc import ABC, abstractmethod


class Person(ABC):
    """Class induk untuk semua aktor manusia di sistem apotek.

    Konsep OOP:
    - Inheritance: diwarisi oleh Apoteker dan Pelanggan.
    - Encapsulation: atribut nama, alamat, dan telepon dibuat private.
    - Polymorphism: method tampilkan_info() akan dioverride di class turunan.
    """

    def __init__(self, id_person: str, nama: str, alamat: str, telepon: str):
        self._id_person = id_person          # protected, boleh diakses class turunan
        self.__nama = nama                  # private
        self.__alamat = alamat              # private
        self.__telepon = telepon            # private

    def get_id_person(self):
        return self._id_person

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru: str):
        if not nama_baru.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self.__nama = nama_baru

    def get_alamat(self):
        return self.__alamat

    def set_alamat(self, alamat_baru: str):
        self.__alamat = alamat_baru

    def get_telepon(self):
        return self.__telepon

    def set_telepon(self, telepon_baru: str):
        if len(telepon_baru.strip()) < 8:
            raise ValueError("Nomor telepon minimal 8 karakter.")
        self.__telepon = telepon_baru

    @abstractmethod
    def tampilkan_info(self):
        """Method abstrak agar setiap turunan wajib punya format info sendiri."""
        pass

    def to_dict(self):
        """Mengubah object menjadi dictionary agar mudah disimpan ke JSON."""
        return {
            "id_person": self._id_person,
            "nama": self.__nama,
            "alamat": self.__alamat,
            "telepon": self.__telepon,
        }
