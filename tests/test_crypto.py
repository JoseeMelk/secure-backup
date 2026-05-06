import pytest

from secure_backup.kdf import generate_salt, derive_key
from secure_backup.crypto import generate_nonce, encrypt_bytes, decrypt_bytes


def test_encrypt_decrypt_roundtrip():
    password = "test123"
    data = b"hola mundo"

    salt = generate_salt()
    key = derive_key(password, salt)
    nonce = generate_nonce()

    ciphertext, tag = encrypt_bytes(key, data, nonce)
    decrypted = decrypt_bytes(key, nonce, ciphertext, tag)

    assert decrypted == data


def test_wrong_password_fails():
    password = "correct"
    wrong_password = "wrong"
    data = b"secret"

    salt = generate_salt()
    key = derive_key(password, salt)
    wrong_key = derive_key(wrong_password, salt)
    nonce = generate_nonce()

    ciphertext, tag = encrypt_bytes(key, data, nonce)

    with pytest.raises(Exception):
        decrypt_bytes(wrong_key, nonce, ciphertext, tag)
        
def test_vector_decrypt():
    from secure_backup.kdf import derive_key
    from secure_backup.crypto import decrypt_bytes

    with open("test_vectors/sample.enc", "rb") as f:
        data = f.read()

    salt = data[4:20]
    nonce = data[20:32]
    tag = data[32:48]
    ciphertext = data[48:]

    key = derive_key("test-password", salt)
    plaintext = decrypt_bytes(key, nonce, ciphertext, tag)

    assert plaintext == b"SecureBackupTest"