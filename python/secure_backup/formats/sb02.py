import json

MAGIC = b"SB02"
VERSION = 1

def build_metadata(filename):
    metadata = {
        "filename": filename
    }

    return json.dumps(metadata).encode("utf-8")

def parse_metadata(metadata_bytes):
    return json.loads(metadata_bytes.decode("utf-8"))

def write_sb02(
    output_path,
    metadata,
    salt,
    nonce,
    tag,
    ciphertext
):
    metadata_len = len(metadata).to_bytes(2, "big")

    with open(output_path, "wb") as f:
        f.write(MAGIC)
        f.write(VERSION.to_bytes(1, "big"))
        f.write(metadata_len)
        f.write(metadata)

        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)
        
def read_sb02(input_path):
    with open(input_path, "rb") as f:
        magic = f.read(4)

        if magic != MAGIC:
            raise ValueError("Invalid SB02 file")

        version = int.from_bytes(f.read(1), "big")

        if version != VERSION:
            raise ValueError("Unsupported SB02 version")

        metadata_len = int.from_bytes(f.read(2), "big")

        metadata_bytes = f.read(metadata_len)

        metadata = parse_metadata(metadata_bytes)

        salt = f.read(16)
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()

    return {
        "metadata": metadata,
        "salt": salt,
        "nonce": nonce,
        "tag": tag,
        "ciphertext": ciphertext,
    }