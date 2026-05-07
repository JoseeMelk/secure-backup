from secure_backup.parser import detect_format


def test_detect_sb01(tmp_path):
    file = tmp_path / "sample.enc"

    file.write_bytes(b"SB01test")

    assert detect_format(file) == "SB01"


def test_detect_sb02(tmp_path):
    file = tmp_path / "sample.enc"

    file.write_bytes(b"SB02test")

    assert detect_format(file) == "SB02"