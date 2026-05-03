# problem: mencetak anka ganjil dan angka genap
# inputan: angka
# proses: jika habis dibagi 2 = genap jika tidak ganjil
# output: jenis angka

angka = int(input('MASUKKAN ANGKA YANG INGIN DI PERIKSA: '))

if angka % 2 == 0:
    print("ANGKA GENAP")
else:
    print("ANGKA GANJIL")