# Secure Backup

CLI tool for local file encryption and decryption using password-based cryptography.

---

## Overview

Secure Backup is a command-line application designed to securely encrypt and decrypt files locally using password-based encryption.

The project focuses on:

- correctness
- portability
- format stability
- future interoperability across implementations

Encrypted files are self-contained and can safely be stored, shared, or backed up.

> Encryption happens locally. Data is never uploaded or transmitted.

---

## Features

- Password-based encryption
- AES-256-GCM authenticated encryption
- PBKDF2-HMAC-SHA256 key derivation
- Portable `.enc` encrypted files
- Embedded metadata support (SB02)
- Automatic filename restoration
- Multi-format parser architecture
- Cross-language compatibility design
- Future-ready streaming architecture

---

## Supported Formats

| Format | Status | Features |
|--------|--------|----------|
| SB01 | Legacy | Basic encryption |
| SB02 | Current | Metadata support |
| SB03 | Planned | Streaming encryption |

---

## How It Works

1. User provides a file and password
2. A secure key is derived using PBKDF2
3. File is encrypted using AES-256-GCM
4. Metadata and cryptographic parameters are embedded
5. A portable `.enc` file is generated

Decryption requires the original password.

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

### 4. Install project

```bash
pip install -e ".[dev]"
```

---

## Usage

### Encrypt a file

```bash
python -m secure_backup.cli encrypt photo.png
```
##### Default output:

```bash
photo.enc
```

#### Encrypt with custom encrypted filename

```bash
python -m secure_backup.cli encrypt photo.png --name backup-secret
```

##### output:

```bash
backup-secret.enc
```

#### Encrypt to custom directory

```bash
python -m secure_backup.cli encrypt photo.png -o /tmp/
```

You will be prompted for a password.

---

### Decrypt file

```bash
python -m secure_backup.cli decrypt photo.enc
```
SB02 automatically restores original filename.

#### Decrypt with custom output name

```bash
python -m secure_backup.cli decrypt photo.enc --name recovered.png
```

#### Decrypt to custom directory

```bash
python -m secure_backup.cli decrypt photo.enc -o /tmp/
```

---

## Project Structure

```bash
   secure-backup/
   ├── docs/
   │   ├── cli.md
   │   ├── crypto.md
   │   ├── spec.md
   │   └── formats/
   │       ├── sb01.md
   │       ├── sb02.md
   │       └── sb03-draft.md
   │
   ├── python/
   │   └── secure_backup/
   │
   ├── tests/
   ├── test_vectors/
   ├── scripts/
   └── README.md
```

---

## Roadmap

### Current

* SB02 metadata format
* Multi-format parser
* CLI encryption/decryption
* Automatic filename restoration
* Deterministic test vectors

### Next

* Streaming encryption
* Large-file support
* Low-memory encryption pipeline

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
* Corrupted or tampered files are rejected
* If decryption fails → file is tampered or password is incorrect

> If you lose your password, your data **cannot be recovered**

---

## Design Philosophy

* Keep cryptography **simple and correct**
* Design stable binary formats
* Separate protocol from implementation
* Prioritize compatibility and maintainability

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

---
