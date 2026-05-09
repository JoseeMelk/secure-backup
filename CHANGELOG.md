# Changelog

All notable changes to this project will be documented in this file.

---

## [0.2.0] - 2026-05-08

### Added

- SB02 encrypted file format
- Embedded filename metadata
- Automatic filename restoration
- Multi-format parser system
- Path resolution utilities
- Metadata serialization support
- SB02 unit tests

### Changed

- CLI output behavior redesigned
- Project documentation reorganized
- SB02 is now default encryption format

### Deprecated

- SB01 marked as legacy format

---

## [0.1.0] - 2026-05-06

### Added

- Initial SB01 encrypted file format
- AES-256-GCM encryption
- PBKDF2-HMAC-SHA256 key derivation
- Encrypt/decrypt CLI prototype
- Pytest test suite
- Deterministic test vectors