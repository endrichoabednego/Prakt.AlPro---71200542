#NAMA : Endricho Abednego
#NIM : 71200542
#Kampus : Universitas Kristen Duta Wacana
"""Soal : Buatlah sebuah menu untuk regristrasi atau login sederhana!

input : 
menu : dia sudah regristrasi atau belum 
username : username yang ingin didaftar
password : password yang ingin didaftar
passWord : konfirmasi password 
userName1 : username yang sudah didaftar
passWord1 : password yang sudah didaftar 

proses : 
pengecekan sudah mendaftar atau belum sebelumnya 
pengecekan password dengan passWord apakah sama
pengecekan data yang sudah tersimpan di files cocok dengan data yang di input

output : 
berhasil login atau tidak 
"""
print("""Selamat datang di Kerengram 
Apakah anda sudah pernah memiliki akun sebelumny?
Jika sudah ketik "sudah" dibawah
Jika belum ketik "belum" dibawah""")

try : 
    menu = str(input("Ketik disini : "))
except : 
    print("Invalid input!")
else : 
    if menu == "belum" : 
        print("silahkan buat akun terlebih dahulu ! ")
        username = str(input("Buatlah Username : "))
        password = str(input("Buatlah password : "))
        passWord = str(input("Pastikan password : "))
        if password == passWord : 
            handle = open("data.txt","w")
            handle.write("Username : "+username+"\n")
            handle.write("Password : "+password+"\n")
            print("Anda sudah berhasil registrasi")
        else : 
            print("Password tidak cocok! Silahkan coba lagi")
    elif menu == "sudah" : 
        print("Silahkan login")
        handle = open("data.txt","r")
        userName1 = str(input("Masukkan username : "))
        for line in handle : 
            if line.find (userName1) != -1 : 
                print("Username Benar!")
                passWord1 = str(input("Masukkan Password : "))
                for line in handle : 
                    if line.find(passWord1) != -1 : 
                        print("Password Benar!\n","Anda berhasil login!")
                    else : 
                        print("Password salah ! Silahkan coba lagi ")
            else : 
                print("Username Salah! Silahkan coba lagi ")
                break
    else : 
        print("Invalid input")


