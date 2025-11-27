# enigma/config.py

# Alphabet utilisé par la machine
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Définition des rotors disponibles
# wiring : câblage interne du rotor (26 lettres)
# notch  : position d'encoche historique (on peut l'ignorer pour le stepping simple)
ROTORS = {
    "I": {
        "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "notch": "Q",
    },
    "II": {
        "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "notch": "E",
    },
    "III": {
        "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "notch": "V",
    },
    "IV": {
        "wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "notch": "J",
    },
    "V": {
        "wiring": "VZBRGITYUPSDNHLXAWMJQOFECK",
        "notch": "Z",
    },
}

# Réflecteurs disponibles
REFLECTORS = {
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
}
