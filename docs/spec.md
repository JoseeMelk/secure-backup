# Secure Backup Specification
---

## Overview

Secure Backup defines a versioned encrypted file architecture for portable and authenticated file encryption.

The project separates:

- cryptographic logic
- file format definitions
- CLI behavior
- implementation details

This enables compatibility across multiple languages and implementations.

---

## Design Goals

- Self-contained encrypted files
- Authenticated encryption
- Stable binary protocols
- Cross-language interoperability
- Future streaming support
- Extensible metadata system

---

## Cryptographic Architecture

Secure Backup currently uses:

| Component | Algorithm |
|---|---|
| Encryption | AES-256-GCM |
| KDF | PBKDF2-HMAC-SHA256 |
| Key Size | 32 bytes |
| Salt | 16 bytes |
| Nonce | 12 bytes |
| Tag | 16 bytes |

---

## Supported Formats

| Format | Status |
|---|---|
| SB01 | Legacy |
| SB02 | Current |
| SB03 | Draft |

---

## Compatibility Rules

- New formats must use new MAGIC identifiers
- Older formats should remain decryptable when possible
- Parsers must reject unsupported versions
- Binary layouts must remain deterministic

---

## Security Model

Secure Backup guarantees:

- confidentiality
- integrity
- tamper detection

Secure Backup does NOT guarantee:

- password recovery
- plausible deniability
- metadata secrecy

---

## Future Extensions

Planned future features:

- streaming encryption
- chunked formats
- compression support
- secure viewers
- encrypted virtual filesystem

---

## Compliance

Implementations claiming compatibility MUST:

- correctly parse official formats
- use identical cryptographic parameters
- reject invalid authentication tags
- pass official test vectors