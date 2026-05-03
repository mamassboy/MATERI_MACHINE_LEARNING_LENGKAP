# problem: mencetak anka ganjil dan angka genap
# inputan: angka
# proses: jika habis dibagi 2 = genap jika tidak ganjil
# output: jenis angka

angka = int(input('MASUKKAN ANGKA YANG INGIN DI PERIKSA: ')) #input

if angka % 2 == 0: #proses
    print("ANGKA GENAP") #output
else:
    print("ANGKA GANJIL") #output