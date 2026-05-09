# CLI Documentation

---

## Encrypt a file

```bash
python -m secure_backup.cli encrypt photo.png
```
#### Default output:

```bash
photo.enc
```

### Encrypt with custom encrypted filename

```bash
python -m secure_backup.cli encrypt photo.png --name backup-secret
```

#### output:

```bash
backup-secret.enc
```

### Encrypt to custom directory

```bash
python -m secure_backup.cli encrypt photo.png -o /tmp/
```

You will be prompted for a password.

---

## Decrypt file

```bash
python -m secure_backup.cli decrypt photo.enc
```
SB02 automatically restores original filename.

### Decrypt with custom output name

```bash
python -m secure_backup.cli decrypt photo.enc --name recovered.png
```

### Decrypt to custom directory

```bash
python -m secure_backup.cli decrypt photo.enc -o /tmp/
```

## Output Resolution Priority

Priority order:
```bash
-o > --name > metadata/default
```
---