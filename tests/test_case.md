# Test Case - Program Rekap dan Analisis Nilai Siswa

| ID | Fitur yang Diuji | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- | --- | --- |
| T1 | Data normal | Andi,80 | Data diterima dengan nilai 80 | Andi diterima dengan nilai 80 | PASS |
| T2 | Nilai batas KKM | Eko,75 | Status mencapai KKM | Eko mencapai KKM | PASS |
| T3 | Nilai di bawah KKM | Budi,65 | Status belum mencapai KKM | Belum mencapai KKM | PASS |
| T4 | Nilai di luar rentang | Citra,110 | Data ditolak | Data ditolak karena nilai diluar rentang | PASS |
| T5 | Input bukan angka | Budi,abc | Data ditolak | Data ditolak karena nilai bukan angka | PASS |
| T6 | Nama kosong | ,80 | Data ditolak | Data ditolak karena nama kosong | PASS |
| T7 | Format data salah | Andi | Data ditolak | Data ditolak karena format harus Nama,Nilai | PASS |