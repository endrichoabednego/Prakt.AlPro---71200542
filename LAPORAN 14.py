#Nama : Endricho Abednego 
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana 

"""Soal : Buatlah suatu program untuk pendaftaran nomor telepon dengan syarat dan ketentuan yang sudah ditentukan (harus 12 digit & 3 digit pertama sesuai kode daerah)

input : 
nomor : nomor telpon 
tinggal : tempat tinggal 

proses : 
1. proses pengecekan apakah nomor sudah 12 digit (jika lebih yang dibaca akan 12 digit pertama)
2. proses pengecekan apakah 3 digit pertama sudah sesuai dengan kode daerah atau belum
output : 
keberhasilan pembuatan nomor (ya/tidak)
nomor 
"""
import re
import typing

def nomortelepon (nomor,tinggal) :
    pola = ("\d{12}")
    cocok = re.findall(pola,nomor)
    yk = re.search("^082",nomor)
    bdg = re.search("^083",nomor)
    jkt = re.search("^084",nomor)
    mlg = re.search("^085",nomor)
    sby = re.search("^086",nomor)
    while True : 
        
    
        if cocok :
            tinggal = tinggal.lower()
            if tinggal == "yogyakarta" :
                if yk : 
                    print("Nomor anda berhasil didaftarkan\nIni nomor anda : ",nomor)
                    break
                else : 
                    print("Nomor tidak sesuai ketentuan")
                    break
            elif tinggal == "bandung" :
                if bdg : 
                    print("Nomor anda berhasil didaftarkan\nIni nomor anda : ",nomor)
                    break
                else : 
                    print("Nomor tidak sesuai ketentuan")
                    break
            elif tinggal == "jakarta" :
                if jkt : 
                    print("Nomor anda berhasil didaftarkan\nIni nomor anda : ",nomor)
                    break
                else : 
                    print("Nomor tidak sesuai ketentuan")
                    break
            elif tinggal == "malang" :
                if mlg : 
                    print("Nomor anda berhasil didaftarkan\nIni nomor anda : ",nomor)
                    break
                else : 
                    print("Nomor tidak sesuai ketentuan")
                    break
            elif tinggal == "surabaya" :
                if sby : 
                    print("Nomor anda berhasil didaftarkan\nIni nomor anda : ",nomor)
                    break
                else : 
                    print("Nomor tidak sesuai ketentuan")
                    break
            else : 
                print("Daerah tersebut belum tersedia/invalid")
                break
        else : 
            print("Nomor tidak sesuai ketentuan")
            break


print("""Selamat datang di pembuatan nomor baru 
Syarat dan ketentuan sebagai berikut : 
1. Harus sebanyak 12 digit (jika lebih yang akan dibaca hanya 12 digit pertama
2. 3 digit pertama harus sesuai dengan kode daerah
Kode daerah : 
Yogyakarta = 082
Bandung = 083
Jakarta = 084
Malang = 085
Surabaya = 086""")
tinggal = input("Tinggal dimana : ")
nomor = input("Masukkan nomor : ")

nomortelepon(nomor,tinggal)

