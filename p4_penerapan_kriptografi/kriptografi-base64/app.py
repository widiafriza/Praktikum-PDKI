import base64

# =========================
# FUNGSI CAESAR CIPHER
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


# =========================
# ENKRIPSI GAMBAR
# =========================

with open("gambar/test.jpg", "rb") as image_file:
    binary_data = image_file.read()

# encode base64
encoded_data = base64.b64encode(binary_data)

# ubah menjadi string
encoded_string = encoded_data.decode('utf-8')

# enkripsi caesar
encrypted_text = caesar_encrypt(encoded_string, 3)

# simpan hasil enkripsi
with open("encrypted.txt", "w") as file:
    file.write(encrypted_text)

print("Enkripsi berhasil!")


# =========================
# DEKRIPSI GAMBAR
# =========================

# baca file terenkripsi
with open("encrypted.txt", "r") as file:
    encrypted_content = file.read()

# decrypt caesar
decrypted_text = caesar_decrypt(encrypted_content, 3)

# decode base64
decoded_data = base64.b64decode(decrypted_text)

# simpan hasil gambar
with open("hasil_decrypt.jpg", "wb") as image_file:
    image_file.write(decoded_data)

print("Dekripsi berhasil!")