from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Ensure the key length is 16 bytes (AES-128)
def ensure_key_length(key):
    return key.ljust(16, '0')  # Pad the key to 16 bytes

def encrypt_file(filename, key):
    key = ensure_key_length(key)  # Ensure key length is correct
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    with open(filename, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # Padding to make the size a multiple of block size
    return ciphertext

# Encrypt the image
input_file = 'image.jpeg'  # The image with the flag embedded
encrypted_file = 'encrypted_image.jpeg'

key = '0123456789abcdef'  # 16-byte key (valid for AES-128)

encrypted_data = encrypt_file(input_file, key)

with open(encrypted_file, 'wb') as f:
    f.write(encrypted_data)

print("Image encrypted successfully.")