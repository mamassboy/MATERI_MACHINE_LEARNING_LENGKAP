'''
Dalam PYTHON kita bisa menggunakan operator aritmatika untuk melakukan perhitungan matematika. Operator aritmatika yang umum digunakan dalam Python meliputi:
1. Penjumlahan (+): digunakan untuk menjumlahkan dua angka.
2. Pengurangan (-): digunakan untuk mengurangi satu angka dari angka lainnya.
3. Perkalian (*): digunakan untuk mengalikan dua angka.
4. Pembagian (/): digunakan untuk membagi satu angka dengan angka lainnya.
5. Modulus (%): digunakan untuk mendapatkan sisa dari pembagian dua angka.
6. Pangkat (**): digunakan untuk menghitung pangkat dari suatu angka.
Berikut adalah contoh penggunaan operator aritmatika dalam Python:'''

print("     KAlKULATOR SEDERHANA")
print("="*30)

inputan1 = float(input("Masukkan angka pertama: "))
inputan2 = float(input("Masukkan angka kedua: "))

# variable bukan cuma bisa nyimpan data string, integer, float, boolean, tapi juga bisa nyimpan hasil perhitungan dari operator aritmatika. contoh:

penjumlah = inputan1 + inputan2
pengurangan = inputan1 - inputan2
perkalian = inputan1 * inputan2

print(f"Hasil penjumlahan: {penjumlah:.2f}") # :.2f digunakan untuk menampilkan hasil perhitungan dengan 2 angka di belakang koma
print(f"Hasil pengurangan: {pengurangan:.2f}")
print(f"Hasil perkalian: {perkalian:.2f}")

'''
     KAlKULATOR SEDERHANA
==============================
Masukkan angka pertama: 10.8
Masukkan angka kedua: 22.1
Hasil penjumlahan: 32.90
Hasil pengurangan: -11.30
Hasil perkalian: 238.68

'''