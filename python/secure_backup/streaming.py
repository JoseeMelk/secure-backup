CHUNK_SIZE = 1024 * 1024  # 1MB

def read_chunks(file_obj):
    while True:
        chunk = file_obj.read(CHUNK_SIZE)
        if not chunk:
            break
        yield chunk