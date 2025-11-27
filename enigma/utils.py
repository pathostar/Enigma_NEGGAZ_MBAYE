# enigma/utils.py

from .config import ALPHABET

def char_to_index(c: str) -> int:
    """
    Convertit une lettre (A-Z) en index (0-25).
    """
    c = c.upper()
    return ALPHABET.index(c)

def index_to_char(i: int) -> str:
    """
    Convertit un index (0-25) en lettre (A-Z).
    On fait un modulo 26 pour rester dans l'alphabet.
    """
    return ALPHABET[i % 26]

def clean_text(text: str) -> str:
    """
    Met le texte en majuscules et enlève tout ce qui n'est pas A-Z.
    """
    text = text.upper()
    return "".join(c for c in text if c in ALPHABET)
