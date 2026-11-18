mahasiswa = ["Budi", "Sari", "Dedi"]

mahasiswa.append("Rina")    
mahasiswa[1] = "Siti"      
mahasiswa.remove("Dedi")     

print("Daftar mahasiswa:", mahasiswa)
print("Mahasiswa pertama:", mahasiswa[0])

for i in range(len(mahasiswa)):
    print(i + 1, mahasiswa[i])