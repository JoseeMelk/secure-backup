# SB03 Draft Specification

Status: Draft

---

## Goals

SB03 is designed to support:

- streaming encryption
- low-memory processing
- large-file support

---

## Proposed Layout

| Field | Size |
|---|---|
| MAGIC (`SB03`) | 4 bytes |
| Version | 1 byte |
| Metadata Length | 2 bytes |
| Metadata | Variable |
| Salt | 16 bytes |
| Nonce | 12 bytes |
| Ciphertext | Variable |
| Authentication Tag | 16 bytes |

---

## Key Difference

Unlike SB01/SB02:

- authentication tag is stored at the END of file
- enables streaming encryption pipelines

---

## Current Status

Draft only.

Not yet stable.