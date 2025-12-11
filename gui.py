import tkinter as tk
from tkinter import filedialog, messagebox
from enigma.enigma_machine import EnigmaMachine
from enigma.key_utils import generate_random_key, save_key_to_file, load_key_from_file


class EnigmaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Enigma")
        self.root.geometry("600x500")
        self.key = None  # clé chargée ou générée

        # Zone Message
        tk.Label(root, text="Message :", font=("Arial", 12)).pack(pady=5)
        self.input_text = tk.Text(root, height=5, width=60)
        self.input_text.pack()

        # Boutons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Chiffrer", width=12, command=self.encrypt_message).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Déchiffrer", width=12, command=self.decrypt_message).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Charger Clé", width=12, command=self.load_key).grid(row=0, column=2, padx=10)

        # Résultat
        tk.Label(root, text="Résultat :", font=("Arial", 12)).pack(pady=5)
        self.output_text = tk.Text(root, height=5, width=60)
        self.output_text.pack()

    # ----------------------
    # Chiffrement
    # ----------------------
    def encrypt_message(self):
        message = self.input_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Erreur", "Aucun message à chiffrer.")
            return

        # Génération clé aléatoire
        self.key = generate_random_key()

        machine = EnigmaMachine(
            rotor_names=self.key["rotors"],
            rotor_positions=self.key["positions"],
            ring_settings=self.key["rings"],
            reflector_name=self.key["reflector"],
            plugboard_pairs=self.key["plugboard"],
        )

        cipher = machine.encrypt_message(message)

        # ----------------------------------------
        # SAUVEGARDE AVEC NOM CHOISI PAR L’UTILISATEUR
        # ----------------------------------------
        filename = filedialog.asksaveasfilename(
            initialdir="Key",
            title="Enregistrer la clé sous...",
            defaultextension=".json",
            filetypes=[("Fichier JSON", "*.json")]
        )

        if not filename:
            messagebox.showwarning("Attention", "Aucune clé enregistrée. Déchiffrement impossible.")
            return

        # récupérer juste le nom (ex: ma_cle.json)
        filename_only = filename.split("/")[-1]

        # sauvegarde dans Key/
        save_key_to_file(self.key, filename_only)

        # afficher le message chiffré
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, cipher)

        messagebox.showinfo("Clé sauvegardée", f"Clé enregistrée dans Key/{filename_only}")

    # ----------------------
    # Déchiffrement
    # ----------------------
    def decrypt_message(self):
        cipher = self.input_text.get("1.0", tk.END).strip()
        if not cipher:
            messagebox.showerror("Erreur", "Aucun texte chiffré à déchiffrer.")
            return

        if self.key is None:
            messagebox.showerror("Erreur", "Aucune clé chargée. Clique sur 'Charger Clé'.")
            return

        machine = EnigmaMachine(
            rotor_names=self.key["rotors"],
            rotor_positions=self.key["positions"],
            ring_settings=self.key["rings"],
            reflector_name=self.key["reflector"],
            plugboard_pairs=self.key["plugboard"],
        )

        plain = machine.encrypt_message(cipher)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, plain)

    # ----------------------
    # Charger la clé
    # ----------------------
    def load_key(self):
        file_path = filedialog.askopenfilename(
            initialdir="Key",
            title="Choisir une clé",
            filetypes=[("Fichiers JSON", "*.json")]
        )

        if not file_path:
            return

        filename = file_path.split("/")[-1]
        try:
            self.key = load_key_from_file(filename)
            messagebox.showinfo("OK", f"Clé '{filename}' chargée.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))


# Lancer l'interface
if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()
