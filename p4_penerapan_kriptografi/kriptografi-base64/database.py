import sqlite3

# koneksi database
conn = sqlite3.connect("database.db")

# cursor
cursor = conn.cursor()

# buat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS riwayat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_file TEXT,
    waktu TEXT,
    status TEXT
)
""")

conn.commit()

print("Database berhasil dibuat!")