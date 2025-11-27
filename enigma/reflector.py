# enigma/reflector.py

from .utils import char_to_index, index_to_char

class Reflector:
    def __init__(self, wiring: str):
        """
        wiring : string de 26 lettres représentant le câblage du réflecteur.
        Exemple : "YRUHQSLDPXNGOKMIEBFZCWVJAT" pour B.
        """
        # On convertit chaque lettre en index (0-25)
        self.map = [char_to_index(c) for c in wiring]

    def reflect(self, c: str) -> str:
        """
        Prend une lettre (A-Z) et renvoie la lettre correspondante
        après passage dans le réflecteur.
        """
        idx = char_to_index(c)
        mapped_idx = self.map[idx]
        return index_to_char(mapped_idx)
