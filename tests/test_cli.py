import subprocess
import sys
from pathlib import Path


def test_cli_encrypt_decrypt(tmp_path):
    input_file = tmp_path / "input.txt"
    enc_file = tmp_path / "file.enc"
    output_file = tmp_path / "output.txt"

    input_file.write_text("contenido secreto")

    password = "1234"

    # ENCRYPT
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "secure_backup.cli",
            "encrypt",
            str(input_file),
            "-o",
            str(enc_file),
        ],
        input=f"{password}\n{password}\n",
        text=True,
        capture_output=True,
    )

    assert proc.returncode == 0
    assert enc_file.exists()

    # DECRYPT
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "secure_backup.cli",
            "decrypt",
            str(enc_file),
            "-o",
            str(output_file),
        ],
        input=f"{password}\n",
        text=True,
        capture_output=True,
    )

    assert proc.returncode == 0
    assert output_file.read_text() == "contenido secreto"