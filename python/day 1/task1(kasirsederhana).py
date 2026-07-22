def kasirsederhana() :
    nama = input("masukkan nama anda: ")
    totalBelanja = int(input("masukkan total belanja anda: "))
    memBership = input ("Apakah anda memiliki Kartu Membership (y/n): ").lower
    return nama, totalBelanja, memBership

nama, totalBelanja, memBership = kasirsederhana()

if totalBelanja > 100000 :
    diskon = 0.1
    totalBayar = totalBelanja - (totalBelanja * diskon)
    print(f"Selamat {nama} Anda mendapatkan diskon 10% karena anda melakukan pembelian lebih dari Rp 100.000")
    print(f"Total Pembayaran Anda: Rp {totalBayar}")
        if memBership == ("y"):
        

else :
    print (f"Sayang sekali {nama} anda tidak mendapatkan diskon 10% karna belanja anda masih di bawah 100000")
    print (f"Total Pembayaran Anda: Rp {totalBelanja}")






    
