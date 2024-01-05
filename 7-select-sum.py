import sqlite3

#buat koneksi database(db)
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM (jumlah_sekarang) FROM FAUNA")
#ambil data gaji jadikan baris baru dimulai dari indeks 0
total_fauna = kursor.fetchone()[0] 

print(f"Total seluruh jumlah fauna sekarang adalah : {total_fauna} ")

koneksi.close()
