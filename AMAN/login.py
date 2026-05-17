# pada projek ini saya akan membuat sebuah Sistem AI Anti-Fraud & Keamanan Brankas Digital

username_terdaftar = input("Daftarkan username Anda: ")
password_terdaftar = input("Daftarkan password Anda: ")

Simpan_pass = {username_terdaftar: password_terdaftar}
saldo = 1000000  # Contoh saldo awal
riwayat_transaksi = []  # List untuk menyimpan riwayat transaksi

status_server_utama = True
status_server_cadangan = False

def server():
    global status_server_utama, status_server_cadangan
    if status_server_utama != status_server_cadangan:
        print("Server aktif, menjalankan sistem dengan lancar.")
        main()
    elif status_server_utama == False:
        print("Server utama mengalami gangguan, beralih ke server cadangan.")
        status_server_cadangan = True
    elif (status_server_utama == status_server_cadangan):
        print("Kedua server mengalami gangguan, sistem tidak dapat berjalan.")
    else:
        print("Status server tidak valid.")
    
def login():
    
    for _ in range(3):  # Memberikan kesempatan login sebanyak 3 kali
        input_username = input("Masukkan username: ")
        input_password = input("Masukkan password: ")

        if input_username in Simpan_pass and Simpan_pass[input_username] == input_password:
            print("Login berhasil!")
            return True
        else:
            print("Login gagal! Username atau password salah.")
            
    print("Anda telah mencoba login sebanyak 3 kali. Program akan keluar.")
    return False
        
def cek_keamanan():
    if username_terdaftar in Simpan_pass and password_terdaftar == Simpan_pass[username_terdaftar]:
        print("Keamanan brankas digital terjamin.")


def menu():
    while True:
        print("Selamat datang di Sistem AI Anti-Fraud & Keamanan Brankas Digital!")
        print("1. Cek Keamanan Brankas")
        print("2. Proses Transaksi")
        print("3. Cek Saldo")
        print("4. Cek Riwayat Transaksi")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "1":
            cek_keamanan()
            
        elif pilihan == "2":
            proses_transaksi()            
        elif pilihan == "3":
            print(f"Saldo Anda: {saldo}")
        
        elif pilihan == "4":
            print("Riwayat Transaksi Anda:")
            for transaksi in riwayat_transaksi:
                print(transaksi)
                
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem kami. Sampai jumpa!")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
            
def tarik_tunai():
    global saldo
    jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
    if jumlah_tarik > saldo:
        print("Saldo tidak cukup untuk melakukan penarikan.")
    else:
        saldo -= jumlah_tarik
    print(f"Anda telah menarik {jumlah_tarik} dari brankas digital.")
    print ("Berikut adalah riwayat transaksi Anda:")
    riwayat_transaksi.append(-jumlah_tarik)

def setor_tunai():
    global saldo
    jumlah_setor = int(input("Masukkan jumlah yang ingin disetor: "))
    saldo += jumlah_setor
    riwayat_transaksi.append(jumlah_setor)       
                   
def proses_transaksi():
    print("Menu transaksi:")
    print("1. Tarik tunai")
    print("2. Setor tunai")
    pilihan_transaksi = input("Pilih jenis transaksi: ")
    if pilihan_transaksi == "1":
        tarik_tunai()
    elif pilihan_transaksi == "2":
        setor_tunai()
    else:
        print("Pilihan transaksi tidak valid.")
    print("Transaksi selesai.")
    
 
 

            
def main():
    
    if login() == True:
        menu()
    else:
        print("Gagal login. Program akan keluar.")


server()
    