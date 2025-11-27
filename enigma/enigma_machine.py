# enigma/enigma_machine.py

from .config import ROTORS, REFLECTORS
from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard
from .utils import clean_text

class EnigmaMachine:
    def __init__(self, rotor_names, rotor_positions, ring_settings, reflector_name, plugboard_pairs):
        """
        rotor_names     : liste de 3 noms de rotors, ex ["II","V","III"]
        rotor_positions : liste de 3 lettres, ex ["B","C","R"]
        ring_settings   : liste de 3 entiers, ex [12,2,20]
        reflector_name  : "B" ou "C"
        plugboard_pairs : string, ex "AF TV KO BL RW"
        """

        # Convention : rotors = [left, middle, right]
        self.rotors = []
        for i, name in enumerate(rotor_names):
            cfg = ROTORS[name]
            self.rotors.append(
                Rotor(
                    wiring=cfg["wiring"],
                    notch=cfg["notch"],
                    position=rotor_positions[i],
                    ring_setting=ring_settings[i],
                )
            )

        # Réflecteur
        self.reflector = Reflector(REFLECTORS[reflector_name])

        # Plugboard
        self.plugboard = Plugboard(plugboard_pairs)

    def step_rotors(self):
        """
        Stepping avec notch pour 3 rotors.

        Convention : self.rotors = [left, middle, right]

        Logique :
          - le rotor de droite tourne à chaque lettre
          - si le rotor de droite est SUR SON NOTCH AVANT de tourner -> le milieu tourne aussi
          - si le rotor du milieu est SUR SON NOTCH AVANT de tourner -> le gauche tourne aussi
        """

        left, middle, right = self.rotors

        # On vérifie les notches AVANT de tourner
        rotate_middle = right.is_at_notch()
        rotate_left = middle.is_at_notch()

        # Le rotor de droite tourne toujours
        right.step()

        # Le milieu tourne si le droit était sur son notch
        if rotate_middle:
            middle.step()

        # Le gauche tourne si le milieu était sur son notch
        if rotate_left:
            left.step()

    def encrypt_letter(self, c: str) -> str:
        """
        Chiffre UNE lettre (A-Z) avec la configuration actuelle de la machine.
        """
        if not c.isalpha():
            return c

        c = c.upper()

        # 1) Stepping des rotors
        self.step_rotors()

        # 2) Plugboard entrée
        c = self.plugboard.forward(c)

        # 3) Rotors aller (droite -> gauche)
        left, middle, right = self.rotors
        for rotor in (right, middle, left):
            c = rotor.encode_forward(c)

        # 4) Réflecteur
        c = self.reflector.reflect(c)

        # 5) Rotors retour (gauche -> droite)
        for rotor in (left, middle, right):
            c = rotor.encode_backward(c)

        # 6) Plugboard sortie
        c = self.plugboard.forward(c)

        return c

    def encrypt_message(self, text: str) -> str:
        """
        Chiffre un message complet (string) :
        - nettoie le texte (A-Z uniquement)
        - applique encrypt_letter sur chaque caractère
        """
        text = clean_text(text)
        result = []
        for c in text:
            result.append(self.encrypt_letter(c))
        return "".join(result)
