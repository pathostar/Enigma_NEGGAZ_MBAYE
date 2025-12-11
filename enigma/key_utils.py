import os
import json
import random
from .config import ALPHABET, ROTORS, REFLECTORS


# ==============================
#   GÉNÉRATION DE LA CLÉ
# ==============================

def generate_random_plugboard(max_pairs: int = 8) -> str:
    """
    Génère un plugboard aléatoire sous forme de paires (ex: 'AF TV KO').
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
    Génère une clé Enigma complète de manière aléatoire.
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


# ==============================
#   SAUVEGARDE POUR CHIFFREMENT
# ==============================

def save_key_to_file(key_dict: dict, filename: str = "cle_enigma.json"):
    """
    Sauvegarde une clé Enigma dans le dossier Key/.
    """
    key_dir = "Key"  # le dossier existe déjà chez toi
    os.makedirs(key_dir, exist_ok=True)  # ne casse rien si déjà présent

    filepath = os.path.join(key_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(key_dict, f, indent=4)

    print(f"\nClé enregistrée dans : {filepath}")


# ==============================
#   CHARGEMENT POUR DÉCHIFFREMENT
# ==============================

def load_key_from_file(filename: str = "cle_enigma.json") -> dict:
    """
    Charge une clé depuis le dossier Key/.
    L'utilisateur ne donne que le nom du fichier.
    """
    key_dir = "Key"
    filepath = os.path.join(key_dir, filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Le fichier '{filepath}' est introuvable dans Key/.")

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
