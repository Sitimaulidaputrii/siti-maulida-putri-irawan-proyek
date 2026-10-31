# Program Rekap dan Analisis Nilai Siswa

## Deskripsi

Program ini dibuat untuk membantu pengguna mengolah dan menganalisis nilai siswa secara sederhana. Program membaca data siswa dari file teks, memvalidasi data, menghitung statistik nilai, dan menentukan siswa yang mencapai atau belum mencapai Kriteria Ketuntasan Minimal (KKM).
Pengguna sasaran program ini adalah guru atau pengguna yang membutuhkan bantuan untuk merekap nilai siswa.

## Fitur

- Membaca data siswa dari file teks.
- Memvalidasi nama dan nilai siswa.
- Menolak data yang tidak valid serta menampilkan alasannya.
- Menghitung jumlah siswa, rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan ketuntasan siswa berdasarkan KKM 75.
- Menampilkan hasil analisis di terminal.
- Menyimpan hasil analisis ke file laporan.

## Persyaratan 

- Python 3.x
- Visual Studio Code

## Cara Menjalankan 

Pastikan terminal berada di folder utama proyek, kemudian jalankan:

```bash
python main.py
```

## Struktur Folder 

Siti Maulida Putri Irawan-proyek/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/

Keterangan:
- main.py: menjalankan program utama dan menghubungkan setiap modul.
- src/input_data.py: membaca dan memvalidasi data siswa.
- src/output.py: menghitung statistik nilai dan menentukan ketuntasan.
- data/contoh_data.py: menyimpan data contoh siswa.
- tests/test_case.md: mencatat hasil pengujian program.
- docs/screenshot/: menyimpan dokumentasi berupa tangkapan layar.

## Test Case

| ID | Input | Expected | Actual | Status |
| --- | --- | --- | --- | --- |
| T1 | Andi,80 | data diterima dengan nilai 80 | Andi diterima dengan nilai 80 | PASS |
| T2 | Eko,75 | Status mencapai KKM | Eko mencapai KKM | PASS |
| T3 | Budi,65 | Status belum mencapai KKM | Budi belum mencapai KKM | PASS |
| T4 | Citra.110 | Data ditolak | Data ditolakk karena nilai di luar rentang | PASS |
| T5 | Budi,abc | Data ditolak | Data ditolak karena nilai bukan angka | PASS |
| T6 | ,80 | Data ditolak | Data ditolak karena nama kosong | PASS |
| T7 | Andi | Data ditolak | Data ditolak karena format harus Nama,Nilai | PASS |

## Known Issues 

Belum ditemukan masalah utama pada fitur yang telah diuji. Program masih perlu diuji pada kondisi lain, seperti ketika file data tidak ditemukan atau ketika seluruh data tidak valid.

## Anggota dan Kontribusi

Nama anggota: 
Kontribusi: merancang program, menulis kode, menguji fitur, dan menyusun dokumentasi

## Referensi/Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi proyek Python di VS Code, Git, dan GitHub.
- Python Software Foundation. Dokumentasi resmi Python:  https://docs.python.org/3/ 
- Bantuan ChatGPT