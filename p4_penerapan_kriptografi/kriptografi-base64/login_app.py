import tkinter as tk
from tkinter import messagebox

# =========================
# DATA LOGIN
# =========================

USERNAME = "admin"
PASSWORD = "12345"

# =========================
# FUNGSI LOGIN
# =========================

def login():

    username = entry_username.get()
    password = entry_password.get()

    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login", "Login berhasil!")

        root.destroy()

        import gui_app

    else:
        messagebox.showerror("Login", "Username atau password salah!")

# =========================
# GUI LOGIN
# =========================

root = tk.Tk()
root.title("Login Sistem")
root.geometry("350x250")

judul = tk.Label(
    root,
    text="LOGIN SISTEM",
    font=("Arial", 16, "bold")
)

judul.pack(pady=20)

label_username = tk.Label(root, text="Username")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(
    root,
    text="Login",
    command=login,
    width=15
)

btn_login.pack(pady=20)

root.mainloop()