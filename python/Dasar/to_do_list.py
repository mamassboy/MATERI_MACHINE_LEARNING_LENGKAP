# List tugas
daftar_tugas = []

for i in range(3):
    tugas = input(f"Masukkan tugas ke-{i+1}: ")
    daftar_tugas.append(tugas)
    
    
print("\nDaftar Tugas:")
for i, tugas in enumerate(daftar_tugas, start=1):
    print(f"{i}. {tugas}")

# Menyelesaikan tugas:
while True:
    indeks_tugas = int(input("\nMasukkan nomor tugas yang telah diselesaikan (0 untuk keluar): "))
    if indeks_tugas == 0:
        break
    elif indeks_tugas > 0 and indeks_tugas <= len(daftar_tugas):
        daftar_tugas.pop(indeks_tugas -1)
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")     
    else:
        print("Nomor tugas tidak valid. Silakan coba lagi.")
        
        
