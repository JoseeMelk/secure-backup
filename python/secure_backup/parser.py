from secure_backup.formats.sb01 import MAGIC as SB01_MAGIC
from secure_backup.formats.sb02 import MAGIC as SB02_MAGIC


def detect_format(input_path):
    with open(input_path, "rb") as f:
        magic = f.read(4)

    if magic == SB01_MAGIC:
        return "SB01"

    if magic == SB02_MAGIC:
        return "SB02"

    raise ValueError("Unknown file format")