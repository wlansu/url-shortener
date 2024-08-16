import string
import secrets


def generate_short_code(length: int = 6) -> str:
    """With a length of 6 we could generate around 50 million shortened urls.

    26 lowercase letters + 26 uppercase letters + 10 digits = 62 characters
    62^6 = 56,800,235,584

    We could also check in the database if the short_code already exists, but that seems premature at the moment.
    """
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))
