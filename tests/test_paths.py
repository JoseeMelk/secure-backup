from secure_backup.paths import (
    resolve_encrypt_output,
    resolve_decrypt_output,
)


def test_encrypt_default():
    result = resolve_encrypt_output("photo.png")

    assert result.name == "photo.enc"


def test_encrypt_custom_name():
    result = resolve_encrypt_output(
        "photo.png",
        custom_name="secret"
    )

    assert result.name == "secret.enc"


def test_encrypt_output_override():
    result = resolve_encrypt_output(
        "photo.png",
        output_path="/tmp/custom.enc"
    )

    assert str(result) == "/tmp/custom.enc"


def test_decrypt_default():
    result = resolve_decrypt_output("photo.enc")

    assert result.name == "photo.dec"


def test_decrypt_custom_name():
    result = resolve_decrypt_output(
        "photo.enc",
        custom_name="restored.png"
    )

    assert result.name == "restored.png"


def test_decrypt_metadata_name():
    result = resolve_decrypt_output(
        "photo.enc",
        metadata_filename="photo.png"
    )

    assert result.name == "photo.png"


def test_decrypt_output_override():
    result = resolve_decrypt_output(
        "photo.enc",
        output_path="/tmp/output.png"
    )

    assert str(result) == "/tmp/output.png"