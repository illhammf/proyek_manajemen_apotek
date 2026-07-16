import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from services.apotek import Apotek
from models.obat import ObatBebas, ObatResep
from models.pelanggan import Pelanggan
from models.apoteker import Apoteker
from models.resep import Resep


def build_apotek():
    apotek = Apotek("Apotek Test", "Alamat Test")
    apotek.tambah_apoteker(Apoteker("APT001", "Rina", "Alamat", "081234567890", "SIP001", "Pagi"))
    apotek.tambah_pelanggan(Pelanggan("PLG001", "Andi", "Alamat", "081111111111", True))
    apotek.tambah_obat(ObatBebas("OBT001", "Paracetamol", "Analgesik", 5000, 10, "2027-01-01"))
    apotek.tambah_obat(ObatResep("OBT002", "Amoxicillin", "Antibiotik", 15000, 5, "2027-01-01"))
    return apotek


def test_tambah_dan_cari_obat():
    apotek = build_apotek()
    hasil = apotek.cari_obat("para")
    assert len(hasil) == 1
    assert hasil[0].get_nama() == "Paracetamol"


def test_update_stok_obat():
    apotek = build_apotek()
    assert apotek.update_stok_obat("OBT001", 25) is True
    assert apotek.cari_obat_by_kode("OBT001").get_stok() == 25


def test_transaksi_mengurangi_stok():
    apotek = build_apotek()
    transaksi = apotek.buat_transaksi("TRX001", "PLG001", "APT001")
    transaksi.tambah_detail(apotek.cari_obat_by_kode("OBT001"), 2)
    apotek.simpan_transaksi(transaksi)
    assert apotek.cari_obat_by_kode("OBT001").get_stok() == 8
    assert transaksi.get_status() == "Lunas"


def test_diskon_member():
    apotek = build_apotek()
    transaksi = apotek.buat_transaksi("TRX002", "PLG001", "APT001")
    transaksi.tambah_detail(apotek.cari_obat_by_kode("OBT001"), 2)
    assert transaksi.hitung_total_kotor() == 10000
    assert transaksi.hitung_diskon() == 500
    assert transaksi.hitung_total_bayar() == 9500


def test_validasi_resep():
    apotek = build_apotek()
    apoteker = apotek.cari_apoteker_by_id("APT001")
    resep = Resep("RSP001", "dr. Hasan", "Andi")
    resep.tambah_obat("Amoxicillin")
    assert apoteker.validasi_resep(resep) is True


if __name__ == "__main__":
    test_tambah_dan_cari_obat()
    test_update_stok_obat()
    test_transaksi_mengurangi_stok()
    test_diskon_member()
    test_validasi_resep()
    print("Semua pengujian berhasil.")
