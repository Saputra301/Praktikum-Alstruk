nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("--- Praktikum 3 (Bagian Awal) ---")
print(f"Apakah nilai memenuhi syarat (>= 75)? {syarat_nilai}")
print(f"Apakah kehadiran memenuhi syarat (>= 80)? {syarat_kehadiran}")

lulus_and = syarat_nilai and syarat_kehadiran
print(f"Kelulusan dengan operator 'and': {lulus_and}")

nilai_baru = 70
syarat_nilai_baru = nilai_baru >= 75
lulus_and_baru = syarat_nilai_baru and syarat_kehadiran
print(f"\n[Ubah Nilai = 70] Kelulusan dengan operator 'and': {lulus_and_baru}")

lulus_or = syarat_nilai_baru or syarat_kehadiran
print(f"[Ubah Nilai = 70] Kelulusan dengan operator 'or': {lulus_or}")

#Nilai menjadi 70
nilai = 70
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("--- Praktikum 3 (Bagian Awal) ---")
print(f"Apakah nilai memenuhi syarat (>= 75)? {syarat_nilai}")
print(f"Apakah kehadiran memenuhi syarat (>= 80)? {syarat_kehadiran}")

lulus_and = syarat_nilai and syarat_kehadiran
print(f"Kelulusan dengan operator 'and': {lulus_and}")

nilai_baru = 70
syarat_nilai_baru = nilai_baru >= 75
lulus_and_baru = syarat_nilai_baru and syarat_kehadiran
print(f"\n[Ubah Nilai = 70] Kelulusan dengan operator 'and': {lulus_and_baru}")

lulus_or = syarat_nilai_baru or syarat_kehadiran
print(f"[Ubah Nilai = 70] Kelulusan dengan operator 'or': {lulus_or}")