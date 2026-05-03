tombol1 = False
tombol2 = False

aktifkan_tombol1 = input("Ketik 'Ya' untuk mengaktifkan mesin: ").lower()
aktifkan_tombol2 = input("Ketik 'Ya' untuk mengaktifkan mesin: ").lower()

if aktifkan_tombol2 == "ya":
    tombol2= True

if aktifkan_tombol1 == "ya":
    tombol1 = True

# mesin_aktif = tombol1  != tombol2

if tombol1  != tombol2:
    print("MESIN MENYALA")

else: 
    print("MESIN MATI")