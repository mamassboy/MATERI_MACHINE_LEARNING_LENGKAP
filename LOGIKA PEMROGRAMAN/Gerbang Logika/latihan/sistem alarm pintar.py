
sistem_aktif = False
pintu_terbuka = False
jendela_pecah = False


aktifkan_sistem = input("Ketik 'ya' untuk mengaktifkan sistem: ").lower()
buka_pintu = input("Ketik 'buka' untuk membuka pintu: ").lower()
kaca_pecah = input("Ketik 'Lempar' untuk kaca pecah: ").lower()

if aktifkan_sistem == "ya":
    sistem_aktif = True
if buka_pintu == "buka":
    pintu_terbuka =True
if kaca_pecah == "lempar":
    jendela_pecah = True


if pintu_terbuka and sistem_aktif:
    print("ALARM ON")

elif jendela_pecah :
    print("ALARM ON")
else:
    print("AMAN AJA CS")


