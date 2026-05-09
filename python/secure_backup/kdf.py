import os
from hashlib import pbkdf2_hmac

ITERATIONS = 200_000
KEY_LENGTH = 32

def generate_salt() -> bytes:
    return os.urandom(16)

def derive_key(password: str, salt: bytes) -> bytes:
    return pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        ITERATIONS,
        dklen=KEY_LENGTH
    )
    