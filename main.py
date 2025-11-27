# main.py

from enigma.enigma_machine import EnigmaMachine
from enigma.key_utils import (
    generate_random_key,
    save_key_to_file,
    load_key_from_file,
)


if __name__ == "__main__":
    mode = input("[E]ncrypter ou [D]écrypter ? ").strip().upper()

    # ======================= MODE CHIFFREMENT =======================
    if mode == "E":
        print("\n=== CHIFFREMENT AVEC CLÉ ALÉATOIRE ===")

        # 1) Génération aléatoire de la clé
        key_dict = generate_random_key()

        rotor_names = key_dict["rotors"]
        rotor_positions = key_dict["positions"]
        ring_settings = key_dict["rings"]
        reflector_name = key_dict["reflector"]
        plugboard_pairs = key_dict["plugboard"]

        print("\nClé générée :")
        print("  ROTORS     :", rotor_names)
        print("  POSITIONS  :", rotor_positions)
        print("  RINGS      :", ring_settings)
        print("  REFLECTOR  :", reflector_name)
        print("  PLUGBOARD  :", plugboard_pairs if plugboard_pairs else "AUCUN")

        # 2) Message à chiffrer
        message = input("\nEntrez le message à chiffrer : ").strip()

        # 3) Création de la machine avec cette clé
        machine = EnigmaMachine(
            rotor_names=rotor_names,
            rotor_positions=rotor_positions,
            ring_settings=ring_settings,
            reflector_name=reflector_name,
            plugboard_pairs=plugboard_pairs,
        )

        # 4) Chiffrement
        cipher = machine.encrypt_message(message)

        print("\n=== TEXTE CHIFFRÉ ===")
        print(cipher)

        # 5) Sauvegarde de la clé dans un fichier
        save_choice = input("\nSauvegarder la clé dans un fichier ? (O/N) : ").strip().upper()
        if save_choice == "O":
            filename = input("Nom du fichier (ex: cle_enigma.json) : ").strip()
            if not filename:
                filename = "cle_enigma.json"
            save_key_to_file(key_dict, filename)
            print(f"Clé sauvegardée dans le fichier : {filename}")

    # ======================= MODE DÉCHIFFREMENT =======================
    elif mode == "D":
        print("\n=== DÉCHIFFREMENT AVEC FICHIER DE CLÉ ===")

        # 1) Charger la clé depuis un fichier
        filename = input("Nom du fichier de clé (ex: cle_enigma.json) : ").strip()
        if not filename:
            filename = "cle_enigma.json"

        try:
            key_dict = load_key_from_file(filename)
        except FileNotFoundError:
            print(f"Erreur : fichier '{filename}' introuvable.")
            exit(1)

        rotor_names = key_dict["rotors"]
        rotor_positions = key_dict["positions"]
        ring_settings = key_dict["rings"]
        reflector_name = key_dict["reflector"]
        plugboard_pairs = key_dict["plugboard"]

        print("\nClé chargée :")
        print("  ROTORS     :", rotor_names)
        print("  POSITIONS  :", rotor_positions)
        print("  RINGS      :", ring_settings)
        print("  REFLECTOR  :", reflector_name)
        print("  PLUGBOARD  :", plugboard_pairs if plugboard_pairs else "AUCUN")

        # 2) Entrer le texte chiffré
        cipher = input("\nTexte chiffré à déchiffrer : ").strip()

        # 3) Construire la machine avec la même clé
        machine = EnigmaMachine(
            rotor_names=rotor_names,
            rotor_positions=rotor_positions,
            ring_settings=ring_settings,
            reflector_name=reflector_name,
            plugboard_pairs=plugboard_pairs,
        )

        # 4) Déchiffrement (on "rechiffre")
        plain = machine.encrypt_message(cipher)

        print("\n=== TEXTE DÉCHIFFRÉ ===")
        print(plain)

    else:
        print("Choix invalide.")
