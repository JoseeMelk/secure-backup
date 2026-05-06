import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

NONCE_SIZE = 12

def generate_nonce() -> bytes:
    return os.urandom(NONCE_SIZE)

def encrypt_bytes(key: bytes, plaintext: bytes, nonce: bytes):
    aesgcm = AESGCM(key)
    encrypted = aesgcm.encrypt(nonce, plaintext, None)

    ciphertext = encrypted[:-16]
    tag = encrypted[-16:]
    return ciphertext, tag

def decrypt_bytes(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes):
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext + tag, None)