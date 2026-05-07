from pathlib import Path

from secure_backup.formats.sb02 import (
    build_metadata,
    write_sb02,
    read_sb02
)


def test_write_sb02(tmp_path):
    output = tmp_path / "sample.enc"

    metadata = build_metadata("photo.png")

    salt = b"A" * 16
    nonce = b"B" * 12
    tag = b"C" * 16
    ciphertext = b"encrypted-data"

    write_sb02(
        output,
        metadata,
        salt,
        nonce,
        tag,
        ciphertext
    )

    assert output.exists()

    data = output.read_bytes()

    assert data.startswith(b"SB02")
    
def test_read_sb02(tmp_path):
    output = tmp_path / "sample.enc"

    metadata = build_metadata("photo.png")

    salt = b"A" * 16
    nonce = b"B" * 12
    tag = b"C" * 16
    ciphertext = b"encrypted-data"

    write_sb02(
        output,
        metadata,
        salt,
        nonce,
        tag,
        ciphertext
    )

    parsed = read_sb02(output)

    assert parsed["metadata"]["filename"] == "photo.png"
    assert parsed["salt"] == salt
    assert parsed["nonce"] == nonce
    assert parsed["tag"] == tag
    assert parsed["ciphertext"] == ciphertext