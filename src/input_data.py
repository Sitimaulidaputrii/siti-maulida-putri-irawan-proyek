def validasi_data(nama, nilai_teks):
    nama = nama.strip()

    if not nama:
        return None, "Nama kosong"

    try:
        nilai = float(nilai_teks.strip())
    except ValueError:
        return None, "Nilai bukan angka"

    if nilai < 0 or nilai > 100:
        return None, "Nilai harus berada pada rentang 0 sampai 100"

    return {"nama": nama, "nilai": nilai}, None

def baca_data(path):
    data_valid = []
    data_ditolak = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",", 1)

                if len(bagian) != 2:
                    data_ditolak.append({
                        "baris": nomor_baris,
                        "isi": baris,
                        "alasan": "Format harus Nama,Nilai"
                    })
                    continue

                data, pesan_error = validasi_data(
                    bagian[0], bagian[1]
                )

                if pesan_error:
                    data_ditolak.append({
                        "baris": nomor_baris,
                        "isi": baris,
                        "alasan": pesan_error
                    })
                else:
                    data_valid.append(data)

    except FileNotFoundError:
        return None, [], f"File tidak ditemukan: {path}"

    return data_valid, data_ditolak, None