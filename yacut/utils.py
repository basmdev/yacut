import random
import re
import string

from . import app


def get_unique_short_id() -> str:
    """Формирует уникальный ID для короткой ссылки."""
    length = app.config['SHORT_ID_LENGTH']
    characters: str = string.ascii_letters + string.digits
    short_id: str = "".join(random.choice(characters) for _ in range(length))
    return short_id


def is_valid_custom_id(custom_id) -> bool:
    """Проверяет валидность короткого идентификатора ссылки."""
    pattern: str = re.compile("^[a-zA-Z0-9]+$")
    return bool(pattern.match(custom_id)) and len(custom_id) <= 16
