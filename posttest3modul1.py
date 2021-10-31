import datetime

print()
print("Selamat Datang di Nasi Goreng Cap Enak checkout")
pembeli = input("Masukkan Nama Pembeli : ")
print("Nama Pembeli : ",pembeli)
hari = input("Hari	:")


def main():
	print("\n=============== Promo Super Gila! ==============")
	print("PEMBELIAN 3 MINUMAN DISKON SEBESAR 10%")
	print("PEMBELIAN 2 MAKANAN DISKON SEBESAR 5%")
	print("PEMBELIAN MENGGUNAKAN E-money DISKON SEBESAR 5%")
	print("DISKON SEBESAR 5% SAAT WEEKEND")
	print("DISKON SEBESAR 10% SAAT WEEKDAYS")
	print()
	print("Menu yang Tersedia :")
	print("1. Nasi Goreng = Rp.15.000")
	print("2. Mie Goreng = Rp.10.000")
	print("3. Mie Mawut = Rp.13.000")
	print("4. Es Teh = Rp.5.000")
	print("5. Teh Hangat = Rp.6.000")
	print("6. Es Jeruk = Rp.5.000")
	print("================================================")


menus = [
  {"id": '1', "nama": "Nasi Goreng", "harga": 15000, "tipe": "food"},
  {"id": '2', "nama": "Mie Goreng", "harga": 10000, "tipe": "food"},
  {"id": '3', "nama": "Mie Mawut", "harga": 13000, "tipe": "drink"},
  {"id": '4', "nama": "Es Teh", "harga": 5000, "tipe": "drink"},
  {"id": '5', "nama": "Teh Hangat", "harga": 6000, "tipe": "drink"},
  {"id": '6', "nama": "Es Jeruk", "harga": 5000, "tipe": "drink"},
]

#mata uang yang dipakai adalah rupiah
def format_rupiah(val):
  return f"Rp. {round(val)}"

Nasi_Goreng = 15000
Mie_Goreng = 10000
Mie_Mawut = 13000
Es_Teh = 5000
Teh_Hangat = 6000
Es_Jeruk = 5000

main()

#total_Nasi_Goreng =int(input("Nasi Goreng mau pesan berapa? : "))
#print(total_Nasi_Goreng,"Unit Nasi Goreng.")

#total_Mie_Goreng =int(input("Mie Goreng mau pesan berapa? : "))
#print(total_Mie_Goreng,"Unit Mie Goreng.")

#total_Mie_Mawut =int(input("Mie_Mawut mau pesan berapa? : "))
#print(total_Mie_Mawut,"Unit Mie Mawut.")

#total_Es_Teh =int(input("Es Teh mau pesan berapa? : "))
#print(total_Es_Teh,"Unit Es Teh.")

#total_Teh_Hangat =int(input("Teh Hangat mau pesan berapa? : "))
#print(total_Teh_Hangat,"Unit Teh Hangat.")

#total_Es_Jeruk =int(input("Es Jeruk mau pesan berapa? : "))
#print(total_Es_Jeruk,"Unit Es_Jeruk.")

#harga_Nasi_Goreng = Nasi_Goreng * total_Nasi_Goreng
#harga_Mie_Goreng = Mie_Goreng * total_Mie_Goreng
#harga_Mie_Mawut = Mie_Mawut * total_Mie_Mawut
#harga_Es_Teh = Es_Teh * total_Es_Teh
#harga_Teh_Hangat = Teh_Hangat * total_Teh_Hangat
#harga_Es_Jeruk = Es_Jeruk * total_Es_Jeruk
#total = harga_Nasi_Goreng + harga_Mie_Goreng + harga_Mie_Mawut + harga_Mie_Mawut + harga_Es_Teh + harga_Teh_Hangat + harga_Es_Jeruk
#total_food = harga_Nasi_Goreng + harga_Mie_Mawut + harga_Mie_Goreng
#total_drink = harga_Es_Teh + harga_Teh_Hangat + harga_Es_Jeruk


beli = True
kantong_belanja = []
while beli:
  barang = input('Selamat Datang di Nasi Goreng Cap Enak! Apakah Ingin memesan Sesuatu? ')

  # pemilihan barang yang ingin dibeli
  item = next((sub for sub in menus if sub['id'] == barang), None)

  if item == None:
    print('Maaf, tapi menu sedang tidak ada')
  else:
    total = input(f"{item['nama']}, Baik? Kalau Boleh Tau Mau Berapa Banyak? ")
    item['total'] = int(total)
    item['payment'] = item['total'] * item['harga']
    kantong_belanja.append(item)
    print(f"{item['nama']} {item['total']} pesanan anda sudah kami catat sudah kami catat! ditunggu ya pesanannya akan datang ^_^")
  beli = input('Apa anda ingin memesan lagi? (y/n) ') == 'y'


# total keranjang belanjaan
#Fungsi len() digunakan untuk mengetahui panjang (jumlah item atau anggota) dari objek seperti sequence 
# (string, list, tuple, range) dan collection (dictionary, set, dan frozenset).
if len(kantong_belanja) == 0:
  print("Maaf, Tapi anda tidak memesan apa-apa.")
else:
  # GET TOTAL FOOD AND DRINKS
  total_food = 0
  total_drinks = 0
  for cart in kantong_belanja:
    if cart['tipe'] == 'food':
      total_food += cart['total']
    else:
      total_drinks += cart['total']
  
  # keranjang belanjaan
  print(40*"=", "DAFTAR BELANJAAN", 40*"=")
  for cart in kantong_belanja:
    harga = format_rupiah(cart['harga'])
    print(f"[{cart['id']}] {cart['nama']} x {cart['total']} = {format_rupiah(cart['payment'])}")
  # pembayaran
  print("\n========================================================================================================")
  
  payment_method = input("Apa anda ingin membayar dengan E-money? Kami sedang ada diskon lo dengan pembayaran menggunakan E-money (y/n) ")
  payment_discount = 5 if payment_method == "y" else 0

  # diskon hari 
  day_discount = 10 if datetime.datetime.today().weekday() < 5 else 5

  # pembelian makanan dan minuman yang diskon
  food_discount = 10 if total_food >= 3 else 0
  drink_discount = 5 if total_drinks >= 2 else 0
  total_discount = payment_discount + day_discount + food_discount + drink_discount
  total_payment = sum(cart['payment'] for cart in kantong_belanja)
  cut_discount = total_payment * total_discount / 100
  final_payment = total_payment - cut_discount


  print(f"Total pembelian anda adalah: {format_rupiah(total_payment)}")
  print(f"Anda mendapatkan diskon {total_discount}% senilai {format_rupiah(cut_discount)}")
  print(f"Total pembayaran anda adalah: {format_rupiah(final_payment)}")

  print(f"Selamat Tinggal! Silahkan Datang Kembali")