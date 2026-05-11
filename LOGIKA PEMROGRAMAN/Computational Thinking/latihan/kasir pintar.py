
nama_pelanggan = input("Masukkan nama pelanggan: ")
status_input = input("Apakah pelanggan adalah member? (y/n): ").lower()
status_member = False
if status_input == "y":
    status_member = True


def menu():    
    while True:
        print("Sistem Kasir Pintar")
        print("1. Input Barang")
        print("2. Hitung Total Belanja")
        print("3. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3 = input_barang()
        elif pilihan == 2:
            total_belanja = hitung_total_belanja(jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3)
            diskon = hitung_diskon(total_belanja, status_member)
            total_pembayaran = total_belanja - diskon
            print(f"Total belanja: {total_belanja}")
            print(f"Diskon: {diskon}")
            print(f"Total pembayaran: {total_pembayaran}")
        elif pilihan == 3:
            break
        else:
            print("Pilihan tidak ada")
def input_barang():
    harga_barang1 = 70000
    harga_barang2 = 150000
    harga_barang3 = 23000

    print("NAMA BARANG|	HARGA BARANG")
    print("BARANG 1 |", harga_barang1)
    print("BARANG 2 |", harga_barang2)
    print("BARANG 3 |", harga_barang3)

    
    jumlah_barang1= int(input("Masukkan jumlah barang 1: "))
    jumlah_barang2 = int(input("Masukkan jumlah barang 2: "))
    jumlah_barang3 = int(input("Masukkan jumlah barang 3: "))
    
    return jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3

def hitung_total_belanja(jumlah_barang1, jumlah_barang2, jumlah_barang3, harga_barang1, harga_barang2, harga_barang3):
    total_belanja = (jumlah_barang1 * harga_barang1) + (jumlah_barang2 * harga_barang2) + (jumlah_barang3 * harga_barang3)
    return total_belanja

def pelanggan (nama, status_member):
    if status_member == True:
        print(f"{nama} adalah member, dapat diskon khusus!")
    else:        
        print(f"{nama} bukan member, tidak dapat diskon khusus.")


def hitung_diskon(total_belanja, status_member):
    if status_member == True and total_belanja > 300000:
        return total_belanja * 0.1
    else:
        return 0
       

    
pelanggan(nama_pelanggan, status_member)
menu()