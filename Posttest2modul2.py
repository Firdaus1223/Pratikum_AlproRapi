#Masukkan varabel yang akan di panggil nanti
pilihan = "0"
Mahasiswa = {
  "Nama Mahasiswa": "",
  "Nim Mahasiswa": "",
  "Umur Mahasiswa": 0,
  "Jenis Kelamin Mahasiswa P/L": "",
  "IPK Mahasiswa": 0,
}
#Bikin pilihan menu yang keluar nanti
def pilihanku():
  print("""
=====DATA MAHASISWA=====
\nPilih menu di bawah ini :
1. tampilan data
2. hapus dan ubah data
3. Keluar
  """)
  pilihan = input("Pilih menu : ")
  return pilihan

#Masukkan while atau looping yang fungsinya agar 
# program dapat mengulang terus menerus hingga kita 
# perintahkan untuk berhenti
while pilihan != "3":
  pilihan = pilihanku()
  if pilihan == "1":
    print(f"""
DATA MAHASISWA
Nama Mahasiswa : {Mahasiswa["Nama Mahasiswa"]}
NIM Mahasiswa : {Mahasiswa["Nim Mahasiswa"]}
Umur Mahasiswa : {Mahasiswa["Umur Mahasiswa"]}
Jenis Kelamin Mahasiswa : {Mahasiswa["Jenis Kelamin Mahasiswa P/L"]}
IPK Mahasiswa : {float(Mahasiswa["IPK Mahasiswa"])}
  """)

  elif pilihan == "2":

    Mahasiswa["Nama Mahasiswa"] = input("Masukkan Nama : ")
    Mahasiswa["Nim Mahasiswa"] = input("Masukkan NIM : ")
    Mahasiswa["Umur Mahasiswa"] = input("Masukkan Umur : ")
    Mahasiswa["Jenis Kelamin Mahasiswa P/L"] = input("Masukkan Jenis Kelamin P/L : ")
    Mahasiswa["IPK Mahasiswa"] = input("Masukkan IPK : ")

    print("Selamat!!! Data anda sudah tersimpan")

print("\nTerima kasih! dan silahkan datang kembali")