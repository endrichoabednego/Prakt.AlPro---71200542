#Nama : Endricho Abednego 
#NIM : 71200542
#Kuliah : Universitas Kristen Duta Wacana 

"""Soal : Buatlah suatu program untuk menghitung total harga makanan pada sebuah restoran

input : 
pesan = makanan yang ingin dipesan 
brp = jumlahnya ada berapa
menu = daftar menu 
total = total harga akhir

proses : 
menghitung total harga yang perlu dibayarkan 

output : 
total harga yang perlu dibayarkan
"""

menu = {"ayam goreng" : 12000, "bakso" : 8000 , "mie ayam" : 6000 , "ikan bakar" : 15000 , "nasi goreng" : 10000}

print("Daftar menu restoran 'nikmat' : ")
for i in menu : 
    print(i,"dengan harga Rp.",menu[i])
total = 0

while True : 
    pesan = str(input("Mau pesan apa?\n"))
    pesan = pesan.lower()
    if pesan == "ayam goreng" : 
        brp = int(input("Mau pesan %s berapa porsi\n"%(pesan)))
        a = menu["ayam goreng"]
        total += a * brp
    elif pesan == "bakso" :
        brp = int(input("Mau pesan %s berapa porsi\n"%(pesan)))
        a = menu["bakso"]
        total += a * brp
    elif pesan == "mie ayam" : 
        brp = int(input("Mau pesan %s berapa porsi\n"%(pesan)))
        a = menu["mie ayam"]
        total += a * brp
    elif pesan == "ikan bakar" : 
        brp = int(input("Mau pesan %s berapa porsi\n"%(pesan)))
        a = menu["ikan bakar"]
        total += a * brp
    elif pesan == "nasi goreng" :
        brp = int(input("Mau pesan %s berapa porsi\n"%(pesan)))
        a = menu["nasi goreng"]
        total += a * brp
    elif pesan == "cukup" : 
        vcr = str(input("Apakah anda memiliki voucher?\n"))
        vcr = vcr.lower()
        if vcr == "ya" : 
            print("Anda berhak mendapat potongan harga sebesar Rp. 5.000,00")
            total = total - 5000
            pjk = total + (total * 0.1)
            print("Total harga makanan anda adalah Rp.",total,"\nditambah pajak 10% menjadi Rp. ",pjk)
            break
        elif vcr == "tidak" :
            pjk = total + (total * 0.1)
            print("Total harga makanan anda adalah Rp.",total,"\nditambah pajak 10% menjadi Rp. ",pjk)
            break
    else : 
        print("Menu tidak tersedia")