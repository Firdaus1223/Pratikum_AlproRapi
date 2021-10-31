users = {}
users['firdaus'] = '000'
status = ""

def displayMenu():
    status = input("""
SELAMAT DATANG
=================
1. Login
2. Buat Akun baru
3. Keluar
  """)  


    if status == "1":
        olduser()
    elif status == "2":
        newuser()
    #elif status == "3":
        #displayMenu()

x = 1
def olduser():
    count = 0
    while count < 3 :
        login = input("Enter login name: ")
        passw = input("Enter password: ")
        if login in users and users[login] == passw: 
            print ("\nLogin successful!\n")
            break
        else:
            print('Gagal Login, Coba Lagi \nKet : Jika Sudah Mencoba 3 Kali Anda Kembali Ke Menu')
            count += 1
    else:
        print("Username Tidak Valid")
        print(40*"=")
        print()
# check if user exists and login matches password
x = 2
def newuser():
    createLogin = input("Create login name: ")

    if createLogin in users: # check if login name exists
        print ("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw # add login and password
        print("\nUser created!\n")  

loop = True
while loop :
    print(40*"=")
    print(15*"*", "Log in", 15*"*")
    print(40*"=")
    print("[1] login \n[2] Buat Akun Baru \n[0] Keluar")
    pilihan = int(input("Masukkan Pilihan = "))
    if pilihan == 1:
        olduser()
        print()
    elif pilihan == 2:
        newuser()
        print()
    elif pilihan == 0:
        print("Terima Kasih! Selamat Tinggal")
        loop = False
    else:
        print("Input Salah,Silahkan Masukkan input Dengan Benar")
        
