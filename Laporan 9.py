#Nama : Endricho Abednego
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana 
"""Soal : Buatlah suatu sistem untuk membantu pemilihan ketua kelas di Kelas A!
input : 
pil = berapa jumlah pemilih 
pil2 = nama yang akan dipilih 
nmBanyak = nama paling banyak yang terpilih (ketua kelas yang terpilih)
jml = berapa suara yang dia dapat

proses : 
menentukan suara terbanyak yang dimasukkan oleh user 

output : 
suara terbanyak atau ketua kelas yang terpilih 
 """

print("""Selamat datang di pemilihan ketua kelas A
 Nama kandidat calon ketua kelas : 
 1. Niko
 2. Stevan
 3. Bardi 
 4. Cecil """)
pil = int(input("Ada berapa pemilih : "))
a = []
b = []

for i in range (pil) : 
    pil2 = str(input("Pemilih ke - %s mau memilih siapa?\n" %(i+1) ))
    pil2 = pil2.lower()
    if pil2 == "niko" or pil2 == "stevan" or pil2 == "bardi" or pil2 == "cecil" : 
        a.append(pil2)
    else : 
        print("Tidak ada kandidat dengan nama",pil2)    
for i in a : 
    if i not in b : 
        b.append(i)
print(a)
print("ada",len(b),"kandidat yang terpilih")

nmBanyak = 0 
jml = 0 
for i in a : 
    if a.count(i) > jml : 
        jml = a.count(i)
        nmBanyak = i 
for i in range (len(b)) : 
    x = a[i]
    y = a.count(x) 
    for i in range (y-1) : 
        a.remove(x)
    print(x,"terpilih sebanyak",y,"suara")
print("Suara terbanyak : ",nmBanyak,"\nJumlah suara : ",jml)
print("Saudara/i",nmBanyak,"terpilih sebagai ketua kelas A")


        
