# untuk memasukkan data dari pengguna, kita dapat menggunakan fungsi input() yang disediakan oleh Python. Fungsi ini akan menunggu pengguna untuk memasukkan data melalui keyboard, dan data yang dimasukkan akan dikembalikan sebagai string. Berikut adalah contoh penggunaan fungsi input() untuk meminta pengguna memasukkan nama dan umur mereka:

# meminta pengguna memasukkan nama
nama = input("Masukkan nama Anda: ")
# data yang di ketikkan oleh pengguna akan disimpan dalam variable (kotak) nama 

# meminta pengguna memasukkan umur
umur = input("Masukkan umur Anda: ")
# data yang di ketikkan oleh pengguna akan disimpan dalam variable (kotak) umur

# menampilkan data yang dimasukkan oleh pengguna
print("Nama Anda adalah:", nama)
print("Umur Anda adalah:", umur)

# inputan selalu dikembalikan sebagai string, jadi jika Anda ingin menggunakan data yang dimasukkan sebagai angka (misalnya untuk perhitungan), Anda perlu mengonversinya ke tipe data yang sesuai, seperti int atau float. Misalnya, jika Anda ingin mengonversi umur menjadi integer, Anda dapat melakukannya seperti ini:

print("Tipe data umur:", type(umur))

# Tipe data umur: <class 'str'>

'''
Masukkan nama Anda: Dimas 
Masukkan umur Anda: 21
Nama Anda adalah: Dimas
Umur Anda adalah: 21

'''
