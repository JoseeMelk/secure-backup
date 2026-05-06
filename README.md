# 🔐 Secure Backup

CLI tool for local file encryption and decryption using password-based cryptography.

---

## Overview

**Secure Backup** is a command-line application that allows you to securely encrypt and decrypt files using a password.

It is designed to generate self-contained encrypted files (`.enc`) that can be safely stored, shared, or backed up without exposing their contents.

> Encryption happens **locally** — your data is never sent anywhere.

---

## ⚙️ Features

* Password-based encryption
* Self-contained encrypted file format (`SB01`)
* Authenticated encryption (AES-256-GCM)
* Portable `.enc` files
* Designed for cross-language compatibility (Python → C++)
* Future-ready for cloud integrations

---

## How It Works

1. You provide a file and a password
2. A secure key is derived from the password (PBKDF2)
3. The file is encrypted using AES-256-GCM
4. A `.enc` file is generated containing:

   * metadata (salt, nonce, tag)
   * encrypted data

To decrypt, the same password is required.

---

## Installation

### 1. Clone the repository

```bash
git clone [link]
cd secure-backup
```

---

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Encrypt a file

```bash
python -m secure_backup.cli encrypt archivo.mp4 -o archivo.enc
```

You will be prompted for a password.

---

### Decrypt a file

```bash
python -m secure_backup.cli decrypt archivo.enc -o salida.mp4
```

---

## File Format (SB01)

Encrypted files follow a structured binary format:

| Offset | Size | Description    |
| ------ | ---- | -------------- |
| 0      | 4    | Magic (`SB01`) |
| 4      | 16   | Salt           |
| 20     | 12   | Nonce          |
| 32     | 16   | Auth Tag       |
| 48     | ...  | Ciphertext     |

---

## Project Structure

```bash
secure-backup/
├── docs/              # specifications
├── python/            # Python prototype
│   └── secure_backup/
├── cpp/               # future C++ implementation
├── test_vectors/      # interoperability tests
└── README.md
```

---

## Roadmap

### Current

* File encryption/decryption (CLI)
* Password-based key derivation
* Stable file format (SB01)

### Next

* Streaming encryption (large files)
* Improved CLI UX

### Future

* C++ high-performance implementation
* Secure file viewer (no disk exposure)
* Virtual encrypted filesystem (FUSE)
* Optional cloud integration (e.g., Google Drive)

---

## Security Notes

* Password is **never stored**
* Each file uses a unique salt and nonce
* Authentication ensures file integrity
* If decryption fails → file is tampered or password is incorrect

> If you lose your password, your data **cannot be recovered**

---

## Design Philosophy

* Keep cryptography **simple and correct**
* Separate core logic from interfaces (CLI / GUI)
* Ensure compatibility across implementations
* Avoid exposing sensitive data at all times

---

## Contributing

Contributions are welcome. Please:

* Follow the existing structure
* Keep changes aligned with `docs/spec.md`
* Add tests when modifying core logic

---

## License

MIT License

---

## Author

Built as a secure backup and encryption system with a focus on correctness, portability, and future scalability.
