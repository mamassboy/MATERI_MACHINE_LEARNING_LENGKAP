# Menerapkan OOP DI Projek Brankas

# untuk menyimpan akun
import json 

class Brankas:
    def __init__(self):
        try:
            with open('data_brankas.json', 'r') as file:
                self.__databaseAkun = json.load(file)
        # Menangkap error jika file tidak ada ATAU file kosong/rusak
        except (FileNotFoundError, json.decoder.JSONDecodeError): 
            self.__databaseAkun = {}
            
    def daftar_akun(self, username, password):
        if username in self.__databaseAkun:
            print("Username sudah terdaftar.")
        else:
            self.__databaseAkun[username] = {'password': password, 'saldo': 0}
            with open('data_brankas.json', 'w') as file:
                json.dump(self.__databaseAkun, file)
            print("Akun berhasil didaftarkan.")
    def set_saldo(self, password, username, jumlah):
        if username in self.__databaseAkun and self.__databaseAkun[username]['password'] == password:
            self.__databaseAkun[username]['saldo'] += jumlah
            print(f"Saldo berhasil ditambahkan. Saldo saat ini: {self.__databaseAkun[username]['saldo']}")
        else:
            print("Password salah. Tidak dapat menambahkan saldo.")
            return

    def get_saldo(self, password, username):
        if username in self.__databaseAkun and self.__databaseAkun[username]['password'] == password:
            print(f"Saldo saat ini: {self.__databaseAkun[username]['saldo']}")
        else:
            print("Password salah. Tidak dapat menampilkan saldo.")
        return 
            
# Contoh penggunaan
brankas = Brankas()

while True:
    print("\nMenu:")
    print("1. Daftar Akun")
    print("2. Tambah Saldo")
    print("3. Tampilkan Saldo")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == '1':
        username = input("Masukkan username untuk brankas: ")
        password = input("Masukkan password untuk brankas: ")
        brankas.daftar_akun(username, password)
        
    elif pilihan == '2':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        jumlah = float(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
        brankas.set_saldo(password, username, jumlah)
        
    elif pilihan == '3':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        brankas.get_saldo(password, username)
        
    elif pilihan == '4':
        print("Terima kasih telah menggunakan Brankas!")
        break
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
