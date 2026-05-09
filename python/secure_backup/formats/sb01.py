MAGIC = b"SB01"


def write_sb01(output_path, salt, nonce, tag, ciphertext):
    with open(output_path, "wb") as f:
        f.write(MAGIC)
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)


def read_sb01(input_path):
    with open(input_path, "rb") as f:
        magic = f.read(4)

        if len(magic) != 4:
            raise ValueError("Empty or invalid file")
        
        if magic != MAGIC:
            raise ValueError("Invalid SB01 file")

        salt = f.read(16)
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()

    return {
        "salt": salt,
        "nonce": nonce,
        "tag": tag,
        "ciphertext": ciphertext,
    }