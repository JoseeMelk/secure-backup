# Cryptographic Architecture

---

## Encryption

Secure Backup uses:

- AES-256-GCM

This provides:

- confidentiality
- integrity
- authentication

---

## Key Derivation

Passwords are converted into encryption keys using:

- PBKDF2-HMAC-SHA256

Parameters:

| Parameter | Value |
|---|---|
| Iterations | 200000 |
| Salt Size | 16 bytes |
| Key Length | 32 bytes |

---

## Security Requirements

- Salt must be random per file
- Nonce must never repeat for same key
- Authentication tags must always be verified

---

## Integrity Model

AES-GCM authentication detects:

- corrupted files
- modified ciphertext
- invalid passwords

Partial plaintext must never be trusted before authentication succeeds.