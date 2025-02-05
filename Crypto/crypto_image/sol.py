from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(filename, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Decrypt the file
encrypted_file = 'encrypted_image.jpeg'
decrypted_file = 'decrypted_image.jpeg'

key = '0123456789abcdef'  # Same key as used for encryption

decrypted_data = decrypt_file(encrypted_file, key)

with open(decrypted_file, 'wb') as f:
    f.write(decrypted_data)

print("Image decrypted successfully.")
