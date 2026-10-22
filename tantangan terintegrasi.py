# Program Rekap Nilai dengan pengujian minimal dua kombinasi nilai berbeda

nama = "DWI SAPUTRA"
tugas = 80
ujian = 85

rerata = (tugas + ujian) / 2
status = rerata>= 75

print("=== REKAP NILAI: KOMBINASI 1 ===")
print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Tugas    : {tugas}")
print(f"Nilai Ujian    : {ujian}")
print(f"Rata-rata      : {rerata}")
print(f"Status Kelulusan (Minimal 75): {status}\n")

tugas = 65
ujian = 70

rerata = (tugas + ujian) / 2
status = rerata >= 75

print("=== REKAP NILAI: KOMBINASI 2 ===")
print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Tugas    : {tugas}")
print(f"Nilai Ujian    : {ujian}")
print(f"Rata-rata      : {rerata}")
print(f"Status Kelulusan (Minimal 75): {status}")