import argparse
import getpass
import os

from secure_backup.kdf import generate_salt, derive_key
from secure_backup.crypto import generate_nonce, encrypt_bytes, decrypt_bytes

MAGIC = b"SB01"


def encrypt_file(input_path, output_path):
    if not os.path.exists(input_path):
        print("Input file not found")
        return

    password = getpass.getpass("Password: ")
    confirm = getpass.getpass("Confirm: ")

    if password != confirm:
        print("Passwords do not match")
        return

    salt = generate_salt()
    key = derive_key(password, salt)
    nonce = generate_nonce()

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext, tag = encrypt_bytes(key, plaintext, nonce)

    with open(output_path, "wb") as f:
        f.write(MAGIC)
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f"Encrypted → {output_path}")


def decrypt_file(input_path, output_path):
    if not os.path.exists(input_path):
        print("Encrypted file not found")
        return

    password = getpass.getpass("Password: ")

    with open(input_path, "rb") as f:
        magic = f.read(4)

        if magic != MAGIC:
            print("Invalid file format")
            return

        salt = f.read(16)
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()

    key = derive_key(password, salt)

    try:
        plaintext = decrypt_bytes(key, nonce, ciphertext, tag)
    except Exception:
        print("Decryption failed (wrong password or corrupted file)")
        return

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted → {output_path}")


def main():
    parser = argparse.ArgumentParser(prog="secure-backup")
    subparsers = parser.add_subparsers(dest="command")

    enc = subparsers.add_parser("encrypt")
    enc.add_argument("input")
    enc.add_argument("-o", "--output", required=True)

    dec = subparsers.add_parser("decrypt")
    dec.add_argument("input")
    dec.add_argument("-o", "--output", required=True)

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_file(args.input, args.output)
    elif args.command == "decrypt":
        decrypt_file(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()