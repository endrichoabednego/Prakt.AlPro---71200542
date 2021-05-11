#Nama : Endricho Abednego
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana 

""" Soal : Buatlah suatu sistem untuk peminjaman dan pengembalian buku sederhana pada perpustakaan 

input : 
listbuku = list buku apa saja yang dipinjam 
brpbuku = berapa jumlah buku yang mau dipinjam
nama = nama dari mahasiswa 
jumlah = jumlah buku yang dia pinjam  
pil = indikasi pemilihan menu
namBuku = judul buku yang ingin dia pinjam/kembalikan


proses : 
memasukan item kedalam list
mengeluarkan item pada list
menampilkan list dan jumlah buku

output : 
menampilkan list dan ada berapa buku yang dia pinjam


"""


listbuku = []
nama = str(input("Nama anda : "))
while True : 
    print("""Selamat datang di perpustakaan UKDW
1. Meminjam buku 
2. Mengembalikan buku
3. Menampilkan data buku yang dipinjam
4. Exit
""")
    pil = int(input("Halo %s apa yang ingin anda lakukan?\n"%(nama)))
    if pil == 1 : 
        brpbuku = int(input("Berapa buku yang ingin dipinjam : "))
        for i in range (brpbuku) :
            namBuku = str(input("Mau meminjam buku apa : "))
            listbuku.append(namBuku)
    elif pil == 2 : 
        namBuku = str(input("Buku apa yang ingin dikembalikan : "))
        listbuku.remove(namBuku)
    elif pil == 3 : 
        b = set(listbuku)
        print(nama,"telah meminjam buku sebagai berikut :\n",b)
        for i in b :
            brpbuku = listbuku.count(i)
            print(i,"ada",brpbuku)
    elif pil == 4 : 
        print("Terimakasih")
        break
    else : 
        print("Menu tidak tersedia!")