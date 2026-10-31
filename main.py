from pathlib import Path

from src.input_data import baca_data
from src.proses import (
    BATAS_LULUS,
    hitung_statistik,
    hitung_ketuntasan
)
from src.output import buat_laporan, simpan_laporan

FOLDER_PROYEK = Path(__file__).resolve().parent
FILE_INPUT = FOLDER_PROYEK / "data" / "contoh_data.txt"
FILE_OUTPUT = FOLDER_PROYEK / "output" / "laporan_analisis.txt"

def main():
    data, ditolak, pesan_error = baca_data(FILE_INPUT)

    if pesan_error:
        print(pesan_error)
        return

    print("=== PROGRAM REKAP DAN ANALISIS NILAI SISWA ===")
    print(f"KKM: {BATAS_LULUS}")

    if not data:
        print("Tidak ada data valid yang dapat dianalisis.")
        statistik = {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None
        }
        mencapai, belum = [], []
    else:
        statistik = hitung_statistik(data)
        mencapai, belum = hitung_ketuntasan(data)

        print(f"Jumlah siswa valid: {statistik['jumlah']}")
        print(f"Rata-rata nilai: {statistik['rata_rata']:.2f}")
        print(f"Nilai tertinggi: {statistik['maksimum']:g}")
        print(f"Nilai terendah: {statistik['minimum']:g}")
        print(f"Mencapai KKM: {len(mencapai)} siswa")
        print(f"Belum mencapai KKM: {len(belum)} siswa")

    for siswa in data:
        status = (
            "Mencapai KKM"
            if siswa["nilai"] >= BATAS_LULUS
            else "Belum mencapai KKM"
        )
        print(f"- {siswa['nama']}: {siswa['nilai']:g} ({status})")

    if ditolak:
        print(f"\nData ditolak: {len(ditolak)} baris")
        for item in ditolak:
            print(
                f"- Baris {item['baris']}: "
                f"{item['isi']} — {item['alasan']}"
            )

    isi_laporan = buat_laporan(
        data, statistik, mencapai, belum, ditolak
    )

    FILE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    simpan_laporan(FILE_OUTPUT, isi_laporan)

    print(f"\nLaporan disimpan di: {FILE_OUTPUT}")

if __name__ == "__main__":
    main()