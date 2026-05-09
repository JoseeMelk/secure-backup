from secure_backup.kdf import derive_key
from secure_backup.crypto import encrypt_bytes

MAGIC = b"SB01"

password = "test-password"
plaintext = b"SecureBackupTest"

salt = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
nonce = bytes.fromhex("101112131415161718191a1b")

key = derive_key(password, salt)

ciphertext, tag = encrypt_bytes(key, plaintext, nonce)

with open("test_vectors/sample.enc", "wb") as f:
    f.write(MAGIC)
    f.write(salt)
    f.write(nonce)
    f.write(tag)
    f.write(ciphertext)

print("Vector generado")