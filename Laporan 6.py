#Nama : Endricho Abednego
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana
"""
soal : Bina sering lupa mengenai tugas tugasnya, buatlah sebuah program sebagai reminder bina tentang tugas yang dia punya!
input : 
tgs = apakah ada tugas?
tgs2 = tugas apa
dead = deadline 
krj = apakah dia mau mengerjakan?
alsn = alasan tidak mau mengerjakan 

proses :
akan melakukan perulangan selama masih ada tugas (variabel "tgs = ya")

output : 

akan keluar loop jika tgs berisi tidak 


"""
while True : 
    tgs = str(input("Apakah ada tugas? \n"))
    if tgs == "ya" : 
        tgs2 = str(input("Tugas apa? \n"))
        dead = int(input("Deadline : "))
        print("Anda memiliki tugas",tgs2,"dengan deadline selama",dead,"hari")
        for i in range (dead+1) : 
            krj = str(input("Apakah anda ingin mengerjakan sekarang? \n"))
            if krj == "ya" : 
                print("Bagus! anda rajin ")
                break
            elif krj == "tidak" : 
                alsn = str(input("Kenapa tidak mau mengerjakan : "))
                print("Setelah",alsn,"segera kerjakan!")
                dead -= 1 
                if dead != 0 :
                    print("Deadline anda tersisa",dead,"hari ")
                elif dead == 0 : 
                    print("Deadline anda tersisa",dead,"hari ")
                    print("Anda sudah terlambat mengumpulkan tugas")
                    break
    elif tgs == "tidak" : 
        print("Anda hari ini bisa santai dulu bosss...")
        break
    else : 
        print("Invalid")
        break
    
        

    