from os import system
from datetime import datetime
import time

def view_menu():
	system("cls")
	menu = """
 ===> APLIKASI TIKET PESAWAT <===

[A] - BUAT TIKET
[B] - TAMPILKAN TIKET
[C] - CARI TIKET
[D] - PERBARUI TIKET
[E] - HAPUS TIKET
[Q] - KELUAR
	"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def create_id_penumpang():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_penumpang)+1
	id_penumpang = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
	return id_penumpang
 
def buat_tiket():
	system("cls")
	print("-MEMASUKKAN DAFTAR PENUMPANG BARU- ")
	nama = input("NAMA\t: ") 
	email = input("EMAIL\t: ") 
	tanggal_keberangkatan = input("TANGGAL TANGGAL_KEBERANGKATAN\t: ")
	maskapai = input("MASKAPAI\t: ")
	kode_booking = input("KODE BOOKING\t: ")
	kota_asal = input("KOTA ASAL\t: ")
	kota_tujuan = input("KOTA TUJUAN\t: ")
	seat = input("SEAT\t: ")
	terminal_gate = input("TERMINAL_GATE\t: ")
	kelas = input("KELAS\t: ")

	user_ans = input("TEKAN Y utuk menyimpan(Y/N) : ")
	
	if verify_ans(user_ans):
		id_penumpang = create_id_penumpang() 
		print("Menyimpan Data ...")
		time.sleep(1)
		
		data_penumpang[id_penumpang] = {
			"nama" : nama,
			"email" : email,
			"tanggal_keberangkatan" : tanggal_keberangkatan,
			"maskapai" : maskapai ,
			"kode_booking" : kode_booking,
			"kota_asal" : kota_asal,
			"kota_tujuan" : kota_tujuan,
			"seat" : seat,
			"terminal_gate" : terminal_gate,
			"kelas" : kelas,
		}
		print("Data Tersimpan")
	else:
		print("Data batal disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def tampilkan_tiket():
	system("cls")
	print("-SEMUA PENUMPANG-")
	if len(data_penumpang) == 0:
		print("<BELUM ADA DATA PENUMPANG YANG DISIMPAN>")
	else:
		for id_penumpang in data_penumpang:
			id_penumpang = id_penumpang
			nama = data_penumpang[id_penumpang]["nama"]
			email = data_penumpang[id_penumpang]["email"]
			tanggal_keberangkatan = data_penumpang[id_penumpang]["tanggal_keberangkatan"]
			maskapai = data_penumpang[id_penumpang]["maskapai"]
			kode_booking = data_penumpang[id_penumpang]["kode_booking"]
			kota_asal = data_penumpang[id_penumpang]["kota_asal"]
			kota_tujuan = data_penumpang[id_penumpang]["kota_tujuan"]
			seat = data_penumpang[id_penumpang]["seat"]
			terminal_gate = data_penumpang[id_penumpang]["terminal_gate"]
			kelas = data_penumpang[id_penumpang]["kelas"]
			print(f"""
ID_PENUMPANG : {id_penumpang}
NAMA : {nama}
EMAIL : {email}
TANGGAL_KEBERANGKATAN : {tanggal_keberangkatan}
MASKAPAI : {maskapai}
KODE_BOOKING : {kode_booking}		
KOTA_ASAL : {kota_asal}
KOTA_TUJUAN : {kota_tujuan}
SEAT : {seat}
TERMINAL_GATE : {terminal_gate}
KELAS : {kelas}
   				 """)
	input("Tekan ENTER Untuk Kembali Ke Menu Awal ")

def searching_by_name(penumpang):
	for id_penumpang in data_penumpang:
		if data_penumpang[id_penumpang]["nama"] == penumpang:
			print(f"""
		-DATA DITEMUKAN-
Id_penumpang \t:{id_penumpang}
Nama \t:{data_penumpang[id_penumpang]["nama"]}
Email \t:{data_penumpang[id_penumpang]["email"]}
Tanggal_keberangkatan \t:{data_penumpang[id_penumpang]["tanggal_keberangkatan"]}
Maskapai \t:{data_penumpang[id_penumpang]["maskapai"]}
Kode_booking \t:{data_penumpang[id_penumpang]["kode_booking"]}
Kota_asal \t:{data_penumpang[id_penumpang]["kota_asal"]}
Kota_tujuan \t:{data_penumpang[id_penumpang]["kota_tujuan"]}
Seat \t:{data_penumpang[id_penumpang]["seat"]}
Terminal_gate \t:{data_penumpang[id_penumpang]["terminal_gate"]}
Kelas \t:{data_penumpang[id_penumpang]["kelas"]}
			""")
			return id_penumpang
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def cari_tiket():
	system("cls")
	print("-CARI TIKET-\n")
	nama = input("Nama Penumpang Yang ingin Dicari : ")
	result = searching_by_name(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def update_nama(penumpang):
	print(f"Nama Lama \t:{penumpang}")
	new_nama = input("Nama Baru\t: ")
	respon = input("Apa Yakin ingin mengganti data (Y/N) : ")
	if verify_ans(respon):
		id_penumpang = searching_by_name(penumpang)
		data_penumpang[id_penumpang] = new_nama
		#del data_penumpang[penumpang]
		print("Data Telah di-update")
	else:
		print("Data batal diperbarui")

def update_email(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama Lama \t:{penumpang}")
	print(f"Nama \t:{penumpang}")
	print(f"email Lama \t:{data_penumpang[id_penumpang]['email']}")
	new_email = input("Email baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['email'] = new_email
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_tanggal_keberangkatan(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"tanggal_keberangkatan Lama \t:{data_penumpang[id_penumpang]['tanggal_keberangkatan']}")
	new_tanggal_keberangkatan = input("Tanggal_keberangkatan baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['tanggal_keberangkatan'] = new_tanggal_keberangkatan
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_maskapai(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"maskapai Lama \t:{data_penumpang[id_penumpang]['maskapai']}")
	new_maskapai = input("Maskapai baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['maskapai'] = new_maskapai
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_kode_booking(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"kode_booking Lama \t:{data_penumpang[id_penumpang]['kode_booking']}")
	new_kode_booking = input("Kode_booking baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['kode_booking'] = new_kode_booking
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_kota_asal(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"kota_asal Lama \t:{data_penumpang[id_penumpang]['kota_asal']}")
	new_kota_asal = input("Kota_asal baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['kota_asal'] = new_kota_asal
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_kota_tujuan(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"kota_tujuan Lama \t:{data_penumpang[id_penumpang]['kota_tujuan']}")
	new_kota_tujuan = input("kota_tujuan baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['kota_tujuan'] = new_kota_tujuan
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_seat(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"seat Lama \t:{data_penumpang[id_penumpang]['seat']}")
	new_seat = input("seat baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['seat'] = new_seat
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_terminal_gate(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"terminal_gate Lama \t:{data_penumpang[id_penumpang]['terminal_gate']}")
	new_terminal_gate = input("terminal_gate baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['terminal_gate'] = new_terminal_gate
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_kelas(penumpang):
	id_penumpang = searching_by_name(penumpang)
	print(f"Nama \t:{penumpang}")
	print(f"kelas Lama \t:{data_penumpang[id_penumpang]['kelas']}")
	new_kelas = input("Kelas baru\t: ")
	respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
	if verify_ans(respon):
		data_penumpang[id_penumpang]['kelas'] = new_kelas
		print("Data telah di-update")
	else:
		print("Data batal diperbarui")

def update_tiket():
	system("cls")
	for id_penumpang in data_penumpang:
			nama = data_penumpang[id_penumpang]["nama"]
			email = data_penumpang[id_penumpang]["email"]
			tanggal_keberangkatan = data_penumpang[id_penumpang]["tanggal_keberangkatan"]
			maskapai = data_penumpang[id_penumpang]["maskapai"]
			kode_booking = data_penumpang[id_penumpang]["kode_booking"]
			kota_asal = data_penumpang[id_penumpang]["kota_asal"]
			kota_tujuan = data_penumpang[id_penumpang]["kota_tujuan"]
			seat = data_penumpang[id_penumpang]["seat"]
			terminal_gate = data_penumpang[id_penumpang]["terminal_gate"]
			kelas = data_penumpang[id_penumpang]["kelas"]
			
	nama = input("Nama Penumpang yang ingin diperbarui : ")
	result = searching_by_name(nama)
	if result:
		print("Data Penumpang yang ingin diperbarui : ")
		time.sleep(1)
		print("[1]. Nama , [2]. Email , [3]. Tanggal_keberangkatan , [4]. Maskapai , [5]. Kode_booking , [6]. Kota_asal , [7]. Kota_tujuan , [8]. Seat , [9]. Terminal_gate , [10]. Kelas")
		time.sleep(1)
		respon = input("Pilihan : ")
		if respon == "1":
			update_nama(nama)
		elif respon == "2":
			update_email(nama)
		elif respon == "3":
			update_tanggal_keberangkatan(nama)
		elif respon == "4":
			update_maskapai(nama)
		elif respon == "5":
			update_kode_booking(nama)
		elif respon == "6":
			update_kota_asal(nama)
		elif respon == "7":
			update_kota_tujuan(nama)
		elif respon == "8":
			update_seat(nama)
		elif respon == "9":
			update_terminal_gate(nama)
		elif respon == "10":
			update_kelas(nama)
	input("Tekan ENTER untuk kembali ke menu utama")

def hapus_tiket():
	system("cls")
	nama = input("Masukkan Nama Penumpang yang akan Dihapus : ")
	id_penumpang = searching_by_name(nama)
	if id_penumpang:
		respon = input(f"Yakin ingin menghapus {nama} (Y/N): ")
		if verify_ans(respon):
			del data_penumpang[id_penumpang]
			time.sleep(1)
			print("DATA telah dihapus.")

		else:
			print("DATA batal dihapus")
		input("Tekan ENTER utuk kembali ke menu utama")

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		buat_tiket()
	elif char == "B":
		tampilkan_tiket()
	elif char == "C":
		cari_tiket()
	elif char == "D":
		update_tiket()
	elif char == "E":
		hapus_tiket()
				
data_penumpang = {
	"20200210-C001" : {
		"nama" : "Kevin",
		"email" : "kevin500@gmail.com",
		"tanggal_keberangkatan" : "10 Februari 2021",
		"maskapai" : "BATIK AIR",
		"kode_booking" : "BA27S",
		"kota_asal" : "Palembang",
		"kota_tujuan" : "Jakarta",
		"seat" : "12B",
		"terminal_gate" : "1C",
		"kelas" : "Economy"
	},
	"20200125-C002" : {
		"nama" : "Joko",
		"email" : "joko123@gmail.com",
		"tanggal_keberangkatan" : "25 Januari 2021",
		"maskapai" : "GARUDA INDONESIA",
		"kode_booking" : "GA027F",
		"kota_asal" : "Bandung",
		"kota_tujuan" : "Medan",
		"seat" : "25A",
		"terminal_gate" : "2D",
		"kelas" : "Business"
	},
	"20200125-C003" : {
		"nama" : "Budi",
		"email" : "Budi100@gmail.com",
		"tanggal_keberangkatan" : "20 Mei 2021",
		"maskapai" : "CITILINK INDONESIA",
		"kode_booking" : "CT18B",
		"kota_asal" : "Surabaya",
		"kota_tujuan" : "Bali",
		"seat" : "15F",
		"terminal_gate" : "3A",
		"kelas" : "Business"
	}
}	
stop = False

while not stop:
	view_menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)



	


