#Nama : Endricho Abednego
#NIM : 71200542 
#Kampus : Universitas Kristen Duta Wacana
"""
Sumber soal : https://dosenit.com/kuliah-it/pemrograman/contoh-program-python
Buatlah suatu program untuk menentukan angka berapa saja yang dapat habis dibagi 2, 3 , 2 dan 3 dengan rentang 1 sampai 20 

input : 
a = rentang awal
b = rentang akhir
c = angka pembagi 1
d = angka pembagi 2 

proses : 
Pencarian angka berapa saja yang habis dibagi angka pembagi 

output : 
Angka yang habis dibagi angka pembagi

"""
#fungsi
def bilangan(a,b,c,d) :
    total = []
    total2 = []
    total3 = [] 
    for i in range (a,b+1) : 
        if (i%c) == 0 : 
            total.append(i)
        if (i%d) == 0 : 
            total2.append(i)
        if (i%c) == 0 and (i%d) == 0 : 
            total3.append(i)
        else : 
            pass
    print("Angka",a,"sampai",b,"yang habis dibagi",c,",",d,",",c,"dan",d," adalah ", end= " ")
    return total,total2,total3


#input
a = int(input("Masukkan range awal : "))
b = int(input("Masukkan range akhir : "))
c = int(input("Masukkan angka pembagi 1 : "))
d = int(input("Masukkan angka pembagi 2 : "))
print(bilangan(a,b,c,d))




