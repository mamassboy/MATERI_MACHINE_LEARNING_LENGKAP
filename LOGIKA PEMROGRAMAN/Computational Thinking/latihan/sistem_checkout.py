def hitung_total_belanja(jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3):
    total_belanja = (jumlah_barang1 * harga_barang1) + (jumlah_barang2 * harga_barang2) + (jumlah_barang3 * harga_barang3)
    return total_belanja

def hitung_pajak(total_belanja):
    return total_belanja * 0.11


harga_barang1 = 70000
harga_barang2 = 150000
harga_barang3 = 23000

jumlah_barang1 = 0
jumlah_barang2 = 0
jumlah_barang3 = 0
while True:
    print("Sistem Checkout")
    print("1. Tambah Barang")
    print("2. Hitung Total Belanja")
    print("3. Keluar")
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:

        while True:
            print("NAMA BARANG|	HARGA BARANG")
            print("BARANG 1 |", harga_barang1)
            print("BARANG 2 |", harga_barang2)
            print("BARANG 3 |", harga_barang3)

            
            jumlah_barang1= int(input("Masukkan jumlah barang 1: "))
            jumlah_barang2 = int(input("Masukkan jumlah barang 2: "))
            jumlah_barang3 = int(input("Masukkan jumlah barang 3: "))
            pilihan2 = input("Apakah anda ingin menambahkan barang lain? (y/n)? ").lower()
            if pilihan2 == "y":
                continue
            else:
                break
                
    elif pilihan == 2:
        total_belanja = hitung_total_belanja(jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3)
        pajak = hitung_pajak(total_belanja)
        total_pembayaran = total_belanja + pajak
        
        print("Total belanja: ", total_belanja)
        print("Pajak: ", pajak)
        print("Total pembayaran: ", total_pembayaran)
    elif pilihan == 3:
        break
    else:
        print("Pilihan tidak ada")
