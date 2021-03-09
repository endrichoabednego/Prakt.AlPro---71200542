#Nama : Endricho Abednego 
#Kampus : Universitas Kristen Duta Wacana
#NIM : 71200542
"""
sumber soal : https://student.blog.dinus.ac.id/fanuelphalosa/2019/12/21/contoh-soal-perulangan-pada-python/

Sinta adalah orang yang boros, untuk membantu mengatasi masalah boros tersebut
sinta menginginkan sebuah program yang dapat mengingatkan dia ketika uang dia tersisa Rp.100.000,00.

input : 
uang  = uang bulanan 
batas = batas pengeluaran
pglrn = bentuk pengeluaran 
hrg = nominal / harga pengeluaran 

proses  : 
pengecekan apakah uang masih diatas batas pengeluaran

output : 
barang yang dibeli 
sisa uang 
"""

uang = int(input("Masukkan Uang bulanan : "))
batas = int(input("Masukkan batas pengeluaran : "))

while True : 
    if uang > batas : 
        pglrn = str(input("Pengeluaran : "))
        pglrn.lower()
        if pglrn == "tabung" : 
            hrg = int(input("Nominal yang ingin ditabung : "))
            uang = uang - hrg 
            print("Bagus!Anda menabung.")
            print("Uang sebesar Rp.",hrg,"berhasil ditabung")
            print("Sisa uang jajan anda adalah Rp. ",uang)
        else : 
            hrg = int(input("Berapa harga barang : "))
            uang = uang - hrg
            print(pglrn,"dengan harga Rp. ",hrg,"berhasil dibeli")
            print("Sisa uang jajan anda adalah Rp. ", uang)
    else : 
        print ("Uang anda telah mencapai batas pengeluaran, silahkan mulai dari sekarang berhemat")
        break 
        