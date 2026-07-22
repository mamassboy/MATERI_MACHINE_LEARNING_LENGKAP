# untuk memasukkan data ke variable(kotak) kita dapat menggunakan fungsi input() yang disediakan oleh Python. Fungsi ini akan menunggu pengguna untuk memasukkan data melalui keyboard, dan data yang dimasukkan akan dikembalikan sebagai string. maka dari itu jika kita ingin menggunakan data yang dimasukkan sebagai angka (misalnya untuk perhitungan), kita perlu mengonversinya ke tipe data yang sesuai, seperti int atau float. Misalnya, jika kita ingin mengonversi umur menjadi integer, kita dapat melakukannya seperti ini:

# meminta pengguna memasukkan nama
nama = input("Masukkan nama Anda: ")
# data yang di ketikkan oleh pengguna akan disimpan dalam variable (kotak) nama

# meminta pengguna memasukkan umur
# dikarnakan inputan selalu dikembalikan sebagai string, maka kita perlu mengonversinya ke tipe data integer menggunakan fungsi int()
umur = int(input("Masukkan umur Anda: "))
# data yang di ketikkan oleh pengguna akan disimpan dalam variable (kotak) umur

# memintakan pengguna memasukkan gaji
# dikarnakan inputan selalu dikembalikan sebagai string, maka kita perlu mengonversinya ke tipe data float menggunakan fungsi float()
gaji = float(input("Masukkan gaji Anda: "))
# data yang di ketikkan oleh pengguna akan disimpan dalam variable (kotak) gaji

# menampilkan data yang dimasukkan oleh pengguna
print("Nama Anda adalah:", nama)
print("Umur Anda adalah:", umur)
print("Gaji Anda adalah:", gaji)

# hasil konversi tipe data(bentuk data) dari inputan pengguna:
print("Tipe data nama:", type(nama))
print("Tipe data umur:", type(umur))
print("Tipe data gaji:", type(gaji))

'''
Masukkan nama Anda: Dimas
Masukkan umur Anda: 21
Masukkan gaji Anda: 50000000 
Nama Anda adalah: Dimas
Umur Anda adalah: 21
Gaji Anda adalah: 50000000.0
Tipe data nama: <class 'str'>
Tipe data umur: <class 'int'>
Tipe data gaji: <class 'float'>
'''
