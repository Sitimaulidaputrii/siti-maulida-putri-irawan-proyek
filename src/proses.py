BATAS_LULUS = 75

def hitung_rata_rata(nilai):
    if not nilai:
        return 0

    return sum(nilai) / len(nilai)

def hitung_statistik(data):
    nilai = [siswa["nilai"] for siswa in data]

    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None
    }

def cek_lulus(nilai, batas=BATAS_LULUS):
    return nilai >= batas

def hitung_ketuntasan(data):
    mencapai = []
    belum = []

    for siswa in data:
        if cek_lulus(siswa["nilai"]):
            mencapai.append(siswa)
        else:
            belum.append(siswa)

    return mencapai, belum