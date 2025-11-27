# enigma/rotor.py

from .utils import char_to_index, index_to_char

class Rotor:
    def __init__(self, wiring: str, notch: str, position: str = "A", ring_setting: int = 1):
        """
        wiring       : string de 26 lettres représentant le câblage du rotor
        notch        : lettre de notch (Q, E, V, ...)
        position     : position actuelle du rotor (A-Z)
        ring_setting : réglage d'anneau (1-26)
        """
        self.wiring = wiring
        self.notch = notch.upper()
        self.position = position.upper()
        self.ring_setting = ring_setting

        # mapping direct : index -> index
        self.forward_map = [char_to_index(c) for c in self.wiring]

        # mapping inverse : index -> index
        self.backward_map = [0] * 26
        for i, v in enumerate(self.forward_map):
            self.backward_map[v] = i

    def is_at_notch(self) -> bool:
        """
        Indique si le rotor est actuellement sur sa position de notch.
        """
        return self.position == self.notch

    def encode_forward(self, c: str) -> str:
        """
        Passage de la lettre dans le rotor dans le sens aller (droite -> gauche).
        """
        idx = char_to_index(c)

        # Offset position + ring
        offset = (idx + char_to_index(self.position) - (self.ring_setting - 1)) % 26

        # Câblage forward
        mapped = self.forward_map[offset]

        # Retour au repère global
        out_idx = (mapped - char_to_index(self.position) + (self.ring_setting - 1)) % 26

        return index_to_char(out_idx)

    def encode_backward(self, c: str) -> str:
        """
        Passage de la lettre dans le rotor dans le sens retour (gauche -> droite).
        """
        idx = char_to_index(c)

        offset = (idx + char_to_index(self.position) - (self.ring_setting - 1)) % 26

        mapped = self.backward_map[offset]

        out_idx = (mapped - char_to_index(self.position) + (self.ring_setting - 1)) % 26

        return index_to_char(out_idx)

    def step(self):
        """
        Fait tourner le rotor d'un cran (A->B->C ... Z->A).
        """
        pos_idx = (char_to_index(self.position) + 1) % 26
        self.position = index_to_char(pos_idx)
