# mengambil nama pelanggan, nama barang, jumlah barang dan harga barang dari input pengguna, kemudian menghitung total harga dan menampilkan struk belanja.

# nama pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ").upper() # .upper() agar nama pelanggan ditampilkan dengan huruf kapital semua

# nama barang 
nama_barang = input ("Masukkan nama barang: ").upper() # .upper() agar nama barang ditampilkan dengan huruf kapital semua

stock_barang = {"BAJU": 100000, "CELANA": 150000, "SEPATU": 500000} # dictionary untuk menyimpan stock barang, dengan nama barang sebagai key dan jumlah stock sebagai value
# penerapan type casting
# jumlah barang
# tipe data jumlah barang integer karna jumlah barang tidak bisa berupa desimal
try:
    jumlah_barang = int(input("Masukkan jumlah barang: "))
except ValueError:
    print("Jumlah barang harus berupa angka.")
    exit()

# harga barang
# tipe data harga float karna harga barang bisa berupa desimal
if nama_barang in stock_barang:
    harga_barang = stock_barang.get(nama_barang)
else:
    print("Barang tidak ditemukan dalam stock.")
    exit()

# menghitung total harga
total_harga = jumlah_barang * harga_barang

def diskon(total_harga):
    if total_harga > 100000:
        print("Selamat! Anda mendapatkan diskon 10%")
        diskon = 0.1
        nilai_diskon = total_harga * diskon # diskon 10% dari total harga
        harga_setelah_diskon = total_harga - nilai_diskon # harga akhir setelah diskon
        return nilai_diskon, harga_setelah_diskon
    else:
        return 0, total_harga

nilai_diskon, harga_setelah_diskon = diskon(total_harga)

print("=" * 30)
print("Struk Belanja")
print("=" * 30)
print(f"Nama Pelanggan: {nama_pelanggan}")
print(f"Nama Barang: {nama_barang}")
print(f"Jumlah Barang: {jumlah_barang}")
print(f"Harga Barang: Rp {harga_barang:.2f}")
if total_harga > 100000:
    print (f"Total Harga diskon: Rp {nilai_diskon:.2f}")
    print(f"Total Harga setelah diskon: Rp {harga_setelah_diskon:.2f}") #.2f agar harga barang dan total harga ditampilkan dengan 2 angka di belakang koma
else:
    print(f"Total Harga: Rp {total_harga:.2f}")
print("=" * 30)