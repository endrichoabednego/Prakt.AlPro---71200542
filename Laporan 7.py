#Nama : Endricho Abednego 
#Kampus : Universitas Kristen Duta Wacana 
#NIM : 71200542

""" soal : 
Buatlah suatu program strings yang memiliki fungsi untuk mengganti suatu kata atau huruf dengan kata yang diinputkan oleh user"

input : 
kalimat : kalimat awal 
ubah = kata / huruf yang ingin diganti pada kalimat 
ubah1 = kata / huruf baru 

proses : 
penggantian kata yang sudah dipilih oleh user dengan kata baru yang telah dipilih oleh user 

output : 
kalimat baru dengan kata yang telah diganti 
"""

while True : 
    kal = str(input("Masukkan kalimat : "))
    ubah = str(input("Masukkan kata / huruf yang ingin diubah : "))
    if ubah in kal : 
        ubah1 = str(input("Masukkan kata / huruf baru : "))
        a = kal.replace(ubah,ubah1)
        print("kalimat baru anda adalah : ",a)
        pil = str(input("Apakah anda ingin mengulangi lagi? \n"))
        pil.lower()
        if pil == "ya" : 
            continue
        if pil =="tidak" : 
            break 
    else : 
        print("Kata / huruf tidak ada dalam kalimat")
        continue    
    