import argparse
import getpass
import os

from pathlib import Path

from cryptography.exceptions import InvalidTag
from pathlib import Path
from secure_backup.kdf import generate_salt, derive_key
from secure_backup.crypto import (
    generate_nonce,
    encrypt_bytes,
    decrypt_bytes,
)

from secure_backup.parser import detect_format

from secure_backup.paths import (
    resolve_encrypt_output,
    resolve_decrypt_output,
)

from secure_backup.formats.sb01 import (
    write_sb01,
    read_sb01,
)

from secure_backup.formats.sb02 import (
    build_metadata,
    write_sb02,
    read_sb02,
)


def encrypt_file(
    input_path,
    output_path=None,
    custom_name=None,
):
    if not os.path.exists(input_path):
        print("Input file not found")
        return
    
    if Path(input_path).is_dir():
        print("Directory encryption is not supported yet")
        return

    output_path = resolve_encrypt_output(
        input_path,
        output_path,
        custom_name,
    )

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

    ciphertext, tag = encrypt_bytes(
        key,
        plaintext,
        nonce,
    )

    metadata = build_metadata(
        Path(input_path).name
    )

    write_sb02(
        output_path,
        metadata,
        salt,
        nonce,
        tag,
        ciphertext,
    )

    print(f"Encrypted → {output_path}")


def decrypt_file(
    input_path,
    output_path=None,
    custom_name=None,
):
    if not os.path.exists(input_path):
        print("Encrypted file not found")
        return
    
    if Path(input_path).is_dir():
        print("Input path cannot be a directory")
        return

    password = getpass.getpass("Password: ")

    try:
        format_type = detect_format(input_path)

        if format_type == "SB01":
            data = read_sb01(input_path)

        elif format_type == "SB02":
            data = read_sb02(input_path)

        else:
            print("Unsupported format")
            return

    except ValueError:
        print("Invalid file format")
        return

    salt = data["salt"]
    nonce = data["nonce"]
    tag = data["tag"]
    ciphertext = data["ciphertext"]

    metadata_filename = None

    if format_type == "SB02":
        metadata_filename = data["metadata"]["filename"]

    output_path = resolve_decrypt_output(
        input_path,
        output_path,
        custom_name,
        metadata_filename,
    )

    key = derive_key(password, salt)

    try:
        plaintext = decrypt_bytes(
            key,
            nonce,
            ciphertext,
            tag,
        )

    except InvalidTag:
        print("Decryption failed (wrong password or corrupted file)")
        return

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted → {output_path}")


def main():
    parser = argparse.ArgumentParser(
        prog="secure-backup"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    enc = subparsers.add_parser("encrypt")
    enc.add_argument("input")
    enc.add_argument("-o", "--output")
    enc.add_argument("--name")

    dec = subparsers.add_parser("decrypt")
    dec.add_argument("input")
    dec.add_argument("-o", "--output")
    dec.add_argument("--name")

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_file(
            args.input,
            args.output,
            args.name,
        )

    elif args.command == "decrypt":
        decrypt_file(
            args.input,
            args.output,
            args.name,
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()