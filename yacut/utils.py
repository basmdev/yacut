import random
import re
import string


def get_unique_short_id():
    length = 6
    characters = string.ascii_letters + string.digits
    short_id = "".join(random.choice(characters) for _ in range(length))

    return short_id


def is_valid_custom_id(custom_id):
    pattern = re.compile("^[a-zA-Z0-9]+$")
    return bool(pattern.match(custom_id)) and len(custom_id) <= 16
