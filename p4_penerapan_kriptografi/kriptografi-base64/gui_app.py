import base64
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
from datetime import datetime
import os

# =========================
# CAESAR CIPHER
# =========================

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        result += chr((ord(char) + shift) % 256)

    return result


def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        result += chr((ord(char) - shift) % 256)

    return result


selected_file = ""

# =========================
# PILIH GAMBAR
# =========================

def pilih_gambar():
    global selected_file

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if file_path:
        selected_file = file_path
        label_file.config(text=os.path.basename(file_path))


# =========================
# ENKRIPSI
# =========================

def encrypt_image():

    global selected_file

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Pilih gambar terlebih dahulu!"
        )
        return

    try:

        # baca gambar
        with open(selected_file, "rb") as image_file:
            binary_data = image_file.read()

        # encode base64
        encoded_data = base64.b64encode(binary_data)

        # ubah ke string
        encoded_string = encoded_data.decode('utf-8')

        # encrypt caesar
        encrypted_text = caesar_encrypt(encoded_string, 3)

        # simpan txt
        with open("encrypted.txt", "w") as file:
            file.write(encrypted_text)

        # =========================
        # SIMPAN DATABASE
        # =========================

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO riwayat (nama_file, waktu, status)
        VALUES (?, ?, ?)
        """, (
            os.path.basename(selected_file),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Encrypted"
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sukses",
            "Enkripsi berhasil!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# =========================
# DEKRIPSI
# =========================

def decrypt_image():

    try:

        # baca encrypted txt
        with open("encrypted.txt", "r") as file:
            encrypted_content = file.read()

        # decrypt caesar
        decrypted_text = caesar_decrypt(encrypted_content, 3)

        # decode base64
        decoded_data = base64.b64decode(decrypted_text)

        # simpan gambar
        with open("hasil_decrypt.jpg", "wb") as image_file:
            image_file.write(decoded_data)

        messagebox.showinfo(
            "Sukses",
            "Dekripsi berhasil!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# =========================
# LIHAT RIWAYAT
# =========================

def lihat_riwayat():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM riwayat")

    data = cursor.fetchall()

    conn.close()

    hasil = ""

    for row in data:

        hasil += f"""
ID      : {row[0]}
File    : {row[1]}
Waktu   : {row[2]}
Status  : {row[3]}

"""

    if hasil == "":
        hasil = "Belum ada data."

    messagebox.showinfo(
        "Riwayat Encrypt",
        hasil
    )


# =========================
# GUI
# =========================

root = tk.Tk()
root.title("Enkripsi Gambar Base64")
root.geometry("500x400")
root.resizable(False, False)

judul = tk.Label(
    root,
    text="ENKRIPSI GAMBAR BASE64",
    font=("Arial", 16, "bold")
)

judul.pack(pady=20)

btn_pilih = tk.Button(
    root,
    text="Pilih Gambar",
    command=pilih_gambar,
    width=25
)

btn_pilih.pack(pady=10)

label_file = tk.Label(
    root,
    text="Belum ada gambar",
    font=("Arial", 10)
)

label_file.pack()

btn_encrypt = tk.Button(
    root,
    text="Encrypt",
    command=encrypt_image,
    width=25,
    bg="lightblue"
)

btn_encrypt.pack(pady=10)

btn_decrypt = tk.Button(
    root,
    text="Decrypt",
    command=decrypt_image,
    width=25,
    bg="lightgreen"
)

btn_decrypt.pack(pady=10)

btn_history = tk.Button(
    root,
    text="Lihat Riwayat",
    command=lihat_riwayat,
    width=25,
    bg="orange"
)

btn_history.pack(pady=10)

btn_exit = tk.Button(
    root,
    text="Keluar",
    command=root.quit,
    width=25,
    bg="red"
)

btn_exit.pack(pady=10)

root.mainloop()