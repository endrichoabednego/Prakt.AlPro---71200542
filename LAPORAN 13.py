#Nama : Endricho Abednego
#NIM : 71200542
# Kampus : Universitas Kristen Duta Wacana

"""
Soal :  Buatlah sebuah menu untuk memanipulasi karakter / kata dengan 3 pilihan yaitu 
membalikan kata, mencetak kata per huruf, membuat pola setengah segitiga terbalik (Harus menggunakan fungsi rekursif)

input : 
pil = pilihan menu
kata = memasukkan kata 
indeks = menentukan mau mulai dari indeks keberapa
baris = mau membuat pola berapa baris
karakter = mamu membuat pola menggunakan karakter apa

proses : 
membalikan kata
memisahkan huruf dari sebuah kata kemudian mencetaknya perhuruf
mencetak karakter sehingga membentuk suatu pola

output :
kata yang terbalik
susunan huruf dari sebuah kata
pola setengah segitiga terbalik


"""

def balikkata(kata) :
    if len(kata) == 0 : 
        return kata
    else : 
        return balikkata(kata[1:])+kata[0]
    
def cetakhuruf(kata,indeks) :
    if indeks == len(kata) - 1 :
        print(kata[indeks])
        return("Huruf habis")
    else : 
        print(kata[indeks])
        return cetakhuruf(kata,indeks+1)

def pola(baris,karakter) :
    if baris < 0 : 
        return ("pola selesai")
    else : 
        simbol = []
        for i in range (0,baris) :
            simbol += karakter    
        print(baris," ".join(simbol))
        return pola(baris-1,karakter)

while True : 
    print("""Selamat datang di menu manipulasi karakter/kata
1. Membalikan kata
2. Mencetak kata per huruf
3. Membuat pola setengah segitiga terbalik
4. Exit""")

    pil = int(input("Mau pilih menu keberapa : "))
    if pil == 1 : 
        kata = str(input("Masukan kata yang ingin dibalik : "))
        print("kata setelah dibalik : " ,balikkata(kata))
    elif pil == 2 : 
        kata = str(input("Kata yang ingin dicetak : "))
        indeks = int(input("Ingin mulai dari indeks keberapa : "))
        print(cetakhuruf(kata,indeks))
    elif pil == 3 : 
        baris = int(input("Mau membuat pola berapa baris : "))
        karakter = str(input("Ingin membuat pola menggunakan karakter apa : "))
        print(pola(baris,karakter))
    elif pil == 4 : 
        print("anda berhasil keluar")
        break
    else : 
        print("invalid")