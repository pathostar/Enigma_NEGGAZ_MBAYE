# enigma/key_utils.py

import json
import random
from .config import ALPHABET, ROTORS, REFLECTORS


def generate_random_plugboard(max_pairs: int = 8) -> str:
    """
    Génère un plugboard aléatoire sous forme de paires (ex: 'AF TV KO').
    max_pairs = nombre max de paires.
    """
    letters = list(ALPHABET)
    random.shuffle(letters)

    num_pairs = random.randint(0, max_pairs)
    pairs = []

    for i in range(num_pairs):
        c1 = letters[2 * i]
        c2 = letters[2 * i + 1]
        pairs.append(c1 + c2)

    return " ".join(pairs)


def generate_random_key() -> dict:
    """
    Génère une clé Enigma complète de manière aléatoire :
      - 3 rotors parmi ceux définis dans ROTORS
      - 3 positions initiales A-Z
      - 3 ring settings entre 1 et 26
      - 1 réflecteur
      - 0 à N paires de plugboard
    """
    rotor_names = random.sample(list(ROTORS.keys()), 3)
    rotor_positions = [random.choice(ALPHABET) for _ in range(3)]
    ring_settings = [random.randint(1, 26) for _ in range(3)]
    reflector_name = random.choice(list(REFLECTORS.keys()))
    plugboard_pairs = generate_random_plugboard(max_pairs=8)

    return {
        "rotors": rotor_names,
        "positions": rotor_positions,
        "rings": ring_settings,
        "reflector": reflector_name,
        "plugboard": plugboard_pairs,
    }


def save_key_to_file(key_dict: dict, filepath: str = "cle_enigma.json"):
    """
    Sauvegarde la clé dans un fichier JSON.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(key_dict, f, indent=4)


def load_key_from_file(filepath: str = "cle_enigma.json") -> dict:
    """
    Charge une clé depuis un fichier JSON et la retourne sous forme de dict.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
