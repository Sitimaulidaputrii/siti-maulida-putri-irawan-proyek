def buat_laporan(data, statistik, mencapai, belum, ditolak):
    laporan = [
        "LAPORAN REKAP DAN ANALISIS NILAI SISWA",
        "KKM: 75",
        f"Jumlah siswa valid: {statistik['jumlah']}",
        f"Rata-rata nilai: {statistik['rata_rata']:.2f}",
        f"Nilai tertinggi: {statistik['maksimum']}",
        f"Nilai terendah: {statistik['minimum']}",
        f"Mencapai KKM: {len(mencapai)} siswa",
        f"Belum mencapai KKM: {len(belum)} siswa",
        "",
        "DAFTAR NILAI SISWA"
    ]

    for siswa in data:
        if siswa["nilai"] >= 75:
            status = "Mencapai KKM"
        else:
            status = "Belum mencapai KKM"

        laporan.append(
            f"{siswa['nama']}: {siswa['nilai']:g} ({status})"
        )

    laporan.append("")
    laporan.append(f"Jumlah baris ditolak: {len(ditolak)}")

    for item in ditolak:
        laporan.append(
            f"Baris {item['baris']}: "
            f"{item['isi']} - {item['alasan']}"
        )

    return "\n".join(laporan) + "\n"

def simpan_laporan(path, isi):
    with open(path, "w", encoding="utf-8") as file:
        file.write(isi)