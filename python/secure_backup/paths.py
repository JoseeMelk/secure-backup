from pathlib import Path


def default_encrypt_output(input_path):
    path = Path(input_path)

    return path.with_suffix(".enc")


def default_decrypt_output(input_path):
    path = Path(input_path)

    return path.with_suffix(".dec")


def resolve_encrypt_output(
    input_path,
    output_path=None,
    custom_name=None
):
    if output_path is not None:
        return Path(output_path)

    input_path = Path(input_path)

    if custom_name is not None:
        return input_path.with_name(f"{custom_name}.enc")

    return default_encrypt_output(input_path)


def resolve_decrypt_output(
    input_path,
    output_path=None,
    custom_name=None,
    metadata_filename=None,
):
    if output_path is not None:
        return Path(output_path)

    input_path = Path(input_path)

    if custom_name is not None:
        return input_path.with_name(custom_name)

    if metadata_filename is not None:
        return input_path.with_name(metadata_filename)

    return default_decrypt_output(input_path)