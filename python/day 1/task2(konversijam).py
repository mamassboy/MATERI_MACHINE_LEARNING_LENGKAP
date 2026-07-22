WaktuBerkerja = int(input("masukkan berapa hari kamu kerja : "))
totalJamkerja = WaktuBerkerja * 24
konversiJamkeMenit = totalJamkerja * 60
gajiPerJam = 100000
Total_Gaji = totalJamkerja * gajiPerJam
gajiPerMenit = Total_Gaji / konversiJamkeMenit
print(f"lama kamu berkerja adalah {WaktuBerkerja} Hari \n per jamnya kamu mendapat gaji {gajiPerJam} \n permenitnya kamu mendapat gaji {gajiPerMenit} \n maka kamu memperoleh gaji sebesar {Total_Gaji}")
