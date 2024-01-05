import sqlite3

#buat koneksi database(db)
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
#mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA")
#Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

print("Data Fauna Indonesia")
print("="*115)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama Fauna", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("-"*115)
#Tampilkan data seusia format tabvel dg perulangan
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()