import json
from pathlib import Path


class FileManager:
    """Class utility untuk membaca dan menyimpan data JSON."""

    @staticmethod
    def load_json(path_file: str, default_data):
        path = Path(path_file)
        if not path.exists():
            return default_data
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save_json(path_file: str, data):
        path = Path(path_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


class Laporan:
    """Class untuk membuat laporan sederhana dari data apotek."""

    @staticmethod
    def laporan_stok(obat_list):
        lines = ["LAPORAN STOK OBAT", "=" * 40]
        for obat in obat_list:
            lines.append(
                f"{obat.get_kode_obat()} | {obat.get_nama()} | {obat.get_kategori()} | "
                f"Stok: {obat.get_stok()} | Nilai: Rp{obat.hitung_nilai_stok():,.0f}"
            )
        return "\n".join(lines)

    @staticmethod
    def laporan_penjualan(transaksi_list):
        total = sum(t.get("total_bayar", 0) for t in transaksi_list)
        lines = ["LAPORAN PENJUALAN", "=" * 40]
        for trx in transaksi_list:
            lines.append(f"{trx['kode_transaksi']} | {trx['tanggal']} | Rp{trx['total_bayar']:,.0f} | {trx['status']}")
        lines.append("-" * 40)
        lines.append(f"TOTAL PENDAPATAN: Rp{total:,.0f}")
        return "\n".join(lines)
