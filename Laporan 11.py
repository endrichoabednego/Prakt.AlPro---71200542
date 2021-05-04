#Nama : Endricho Abednego
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana

""" Soal : Buatlah suatu program untuk menentukan pasangan orang tua dan anak yang benar
input :
anak = ()
ortu = ()

proses : 
sorting huruf awal setiap data pada kedua tuple

output : 
pasangan orangtua dan anak yang benar
"""

def pasangan (anak,ortu) :
    a = []
    b = []
    c = []

    for i in ortu : 
        gender, nama = i.split(" ")
        c.append(gender)    
        a.append(nama)
        a.sort()
    for j in anak :
        kategori, naMe = j.split(" ")    
        b.append(naMe)
        b.sort()
    a = tuple(a)
    b = tuple(b)
    for i in range (len(a)) :
        print(b[i],"adalah anak dari",c[i],a[i])
    print(type(a),type(b))


anak = ("An. Budi","An. Cika","An. Safira","An. Karto","An. Dian")
ortu = ("Bp. Bardi","Ibu. Cica","Bp. Doni","Ibu. Kirana","Bp. Sartono")
pasangan(anak,ortu)