#Nama : Endricho Abednego
#Kampus : Universitas Kristen Duta Wacana

""" Sumber soal : https://mastahbisnis.com/biaya-tenaga-kerja-btk/
Budi bekerja pada perusahaan A dengan upah Rp.200.000 per hari dan jika lembur akan mendapatkan tambahan 20% dari upah per hari. 
Gaji setiap karyawan akan dipotong sebesar 5% per bulan untuk biaya asuransi. Jika dalam satu bulan budi bekerja 
24 hari dan diantara itu 10 hari dia lembur, berapa gajii yang dia dapatkan?

input :  
gjHari = gaji per hari 
hari = berapa hari dia bekerja
gjLmbr = berapa tambahan gaji setelah dia lembur
lembur = berapa hari dia lembur
tambahan = berapa banyak tambahan yang akan diberi 
ptg = potongan asuransi 

proses : 
gjBul = gjHari * hari 
gjLmbr = lembur * (tambahan * gjHari)
gjAkhir = (gjBul + gjLmbr) - ((gjBul + gjLmbr) * ptg) 

output : 
gaji akhir budi """

#input 
gjHari = int(input("Masukkan gaji per hari = "))
hari = int(input("Berapa hari budi bekerja = "))
lembur = int(input("Berapa hari budi lembur = "))
tambahan = float(input("Besarnya tambahan jika lembur = "))
ptg = float(input("Masukan potongan gaji dari asuransi = "))

#proses 
gjBul = gjHari * hari 
gjLmbr = lembur * (tambahan * gjHari)
gjAkhir =  (gjBul + gjLmbr) - ((gjBul + gjLmbr )* ptg)

#output 

print("Gaji yang budi dapatkan adalah Rp. ", gjAkhir)



 




