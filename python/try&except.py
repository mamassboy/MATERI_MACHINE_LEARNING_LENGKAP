saldo_nasabah = [1000000]  # Saldo awal nasabah

# fubngsi ini untuuk melakukan penarikan tunai dari brankas digital
def tarik_tunai():
    global saldo_nasabah
    jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
    try:
        if jumlah_tarik > saldo_nasabah[0]:
            print("Saldo tidak cukup untuk melakukan penarikan.")
        else:
            saldo_nasabah[0] -= jumlah_tarik
        print(f"Anda telah menarik {jumlah_tarik} dari brankas digital.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
        
        
# fungsi ini untuk melakukan penyetoran tunai ke brankas digital
def setor_tunai():
    global saldo_nasabah
    try:
        jumlah_setor = int(input("Masukkan jumlah yang ingin disetor: "))
        saldo_nasabah[0] += jumlah_setor
        print(f"Anda telah menyetor {jumlah_setor} ke brankas digital.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
   
   
# fungsi ini untuk mengecek saldo nasabah   
def cek_saldo():
    global saldo_nasabah
    print(f"Saldo Anda: {saldo_nasabah[0]}")
    
# fungsi utama untuk menjalankan program transaksi
def transaksi():
  
    print("===== Menu Transaksi =====")
    print("1. Tarik tunai")
    print("2. Setor tunai")
    print("3. Cek Saldo")
    print("0. Keluar")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        tarik_tunai()
    elif pilihan == "2":
        setor_tunai()
    elif pilihan == "3":
        cek_saldo()
    elif pilihan == "0":
        print("Terima kasih telah menggunakan sistem kami. Sampai jumpa!")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

while True:
    transaksi()     
