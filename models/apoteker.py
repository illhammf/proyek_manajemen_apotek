from models.person import Person


class Apoteker(Person):
    """Class turunan dari Person untuk petugas apotek."""

    def __init__(self, id_person: str, nama: str, alamat: str, telepon: str, nomor_sip: str, shift: str):
        super().__init__(id_person, nama, alamat, telepon)
        self.__nomor_sip = nomor_sip
        self.__shift = shift

    def get_nomor_sip(self):
        return self.__nomor_sip

    def set_nomor_sip(self, nomor_sip: str):
        if not nomor_sip.strip():
            raise ValueError("Nomor SIP tidak boleh kosong.")
        self.__nomor_sip = nomor_sip

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift: str):
        self.__shift = shift

    def validasi_resep(self, resep):
        """Memvalidasi resep. Resep dianggap valid jika punya dokter dan minimal 1 obat."""
        return resep is not None and resep.get_dokter() != "" and len(resep.get_daftar_obat()) > 0

    def tampilkan_info(self):
        """Override dari Person. Ini contoh polymorphism."""
        return f"Apoteker: {self.get_nama()} | SIP: {self.__nomor_sip} | Shift: {self.__shift}"

    def to_dict(self):
        data = super().to_dict()
        data.update({"nomor_sip": self.__nomor_sip, "shift": self.__shift})
        return data

    @staticmethod
    def from_dict(data):
        return Apoteker(
            data["id_person"], data["nama"], data["alamat"], data["telepon"],
            data.get("nomor_sip", "-"), data.get("shift", "Pagi")
        )
