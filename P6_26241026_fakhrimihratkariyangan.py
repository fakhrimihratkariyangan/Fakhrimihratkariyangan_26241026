a =int(input("Digit A: "))
b =int(input("Digit B: "))

#Membuat dua kondisi Boolean berdasarkan nilai digit >= 5
Kondisi1 = a >= 5
Kondisi2 = b >= 5

#Menampilkan hasil evaluasi Boolean dari kondisi1 dan kondisi2
print("Kondisi 1:", Kondisi1)
print("Kondisi 2:", Kondisi2)

#Menampilkan hasil operasi logika NOT, AND, OR, dan ^(XOR)
print("NOT:", not Kondisi1)
print("AND:", Kondisi1 and Kondisi2)
print("OR:", Kondisi1 or Kondisi2)
print("XOR:", Kondisi1 ^ Kondisi2)

# Penjelasan mengapa OR dan XOR berbeda saat kedua kondisi bernilai True:
# Operator OR (inclusive OR) bernilai True jika minimal salah satu kondisi True (termasuk saat keduanya True),
# Sedangkan XOR (Exclusive OR) hanya bernilai True jika kedua kondisi berbeda nilai,
# Sehingga hasilnya False ketika kedua kondisi sama-sama bernilai True