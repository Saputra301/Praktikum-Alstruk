mahasiswa = ("Budi", "12345", "Informatika")

print("Nama   :", mahasiswa[0])
print("NIM    :", mahasiswa[1])
print("Jurusan:", mahasiswa[2])

try:
    mahasiswa[0] = "Andi"
except TypeError:
    print("Data mahasiswa tidak bisa diubah (immutable)")