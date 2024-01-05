import sqlite3

#buat koneksi database(db)
koneksi = sqlite3.connect('database_fauna.db')

#create table baru
koneksi.execute('''
            CREATE TABLE fauna(
             id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
             nama_fauna VARCHAR(50),
             jenis VARCHAR(50),
             asal VARCHAR(50),
             jumlah_sekarang INTEGER(10),
             tahun_ditemukan INTEGER(10)
            )
            ''')
koneksi.close()