from .domains import domain_map

def is_valid_mime(mime: str) -> bool:
    mime = mime.lower()
    mime = mime.split(";", 1)[0].strip()
    if "/" not in mime:
        return False
    first, last = mime.split("/", 1)
    return last in domain_map.get(first, set())