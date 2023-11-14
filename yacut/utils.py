import random
import re
import string

from settings import SHORT_ID_LENGTH


def get_unique_short_id() -> str:
    """Формирует уникальный ID для короткой ссылки."""
    length = SHORT_ID_LENGTH
    characters: str = string.ascii_letters + string.digits
    short_id: str = "".join(random.choice(characters) for _ in range(length))
    return short_id


def is_valid_custom_id(custom_id):
    pattern = re.compile("^[a-zA-Z0-9]+$")
    return bool(pattern.match(custom_id)) and len(custom_id) <= 16
