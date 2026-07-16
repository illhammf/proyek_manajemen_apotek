from models.person import Person


class Pelanggan(Person):
    """Class turunan dari Person untuk pelanggan apotek."""

    def __init__(self, id_person: str, nama: str, alamat: str, telepon: str, status_member: bool = False):
        super().__init__(id_person, nama, alamat, telepon)
        self.__status_member = status_member

    def get_status_member(self):
        return self.__status_member

    def set_status_member(self, status: bool):
        self.__status_member = bool(status)

    def hitung_diskon_member(self, total: float):
        """Member mendapat diskon 5%."""
        return total * 0.05 if self.__status_member else 0

    def tampilkan_info(self):
        """Override dari Person. Format info pelanggan berbeda dari apoteker."""
        status = "Member" if self.__status_member else "Non-member"
        return f"Pelanggan: {self.get_nama()} | Status: {status} | Telp: {self.get_telepon()}"

    def to_dict(self):
        data = super().to_dict()
        data.update({"status_member": self.__status_member})
        return data

    @staticmethod
    def from_dict(data):
        return Pelanggan(
            data["id_person"], data["nama"], data["alamat"], data["telepon"],
            data.get("status_member", False)
        )
