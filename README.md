## Auteure

Projet  **Master 2 MIAGE – Cybersécurité**  
Développé par **Ndeye Pathe MBAYE et Lynda NEGGAZ**.

# Machine Enigma — Implémentation Python (Projet MIAGE Cybersécurité)

Ce projet propose une implémentation complète et fonctionnelle de la **Machine Enigma**, utilisée durant la Seconde Guerre mondiale.  
Il inclut  des rotors, du réflecteur, du plugboard ainsi qu’une interface graphique avec  Tkinter.

---

# Fonctionnalités principales

### Chiffrement
- Génération automatique d’une clé Enigma complète  
- Sauvegarde de la clé dans un fichier `.json` choisi par l'utilisateur  
- Chiffrement symétrique : **le même mécanisme sert au chiffrement et au déchiffrement**

### Déchiffrement
- Chargement d'une clé existante depuis le dossier `Key/`  
- Déchiffrement automatique du texte chiffré **si la même clé est utilisée**

###  Composants 
- 3 rotors sélectionnés parmi (I, II, III, IV, V)
- Positions initiales (A–Z)
- Ring settings (1–26)
- Réflecteurs : B ou C
- Plugboard (Steckerbrett) avec jusqu'à 8 paires aléatoires
- Rotation automatique des rotors (stepping)

---

## Fonctionnement de la machine

### 1. Chiffrement
- L'utilisateur saisit un message
- Le programme génère automatiquement une clé Enigma :
  - rotors
  - positions
  - ring settings
  - plugboard aléatoire
  - réflecteur
- L’utilisateur choisit un nom pour le fichier de clé
- Le texte chiffré s'affiche

### 2. Déchiffrement
- L’utilisateur charge la clé `.json` utilisée lors du chiffrement
- Le message chiffré est saisi
- Le programme renvoie **le message original**

## Interface graphique (Tkinter)

Le projet inclut une interface simple permettant de tester la Machine Enigma sans utiliser le terminal.




## Structure du projet
Projet_Enigma/
│
├── main.py                  # Mode console (chiffrement/déchiffrement)
├── gui.py                   # Interface graphique Tkinter
├── requirements.txt
│
├── enigma/
│    ├── config.py           # Rotors, réflecteurs, alphabet
│    ├── rotor.py            # Implémentation des rotors
│    ├── reflector.py        # Réflecteur
│    ├── plugboard.py        # Plugboard (Steckerbrett)
│    ├── enigma_machine.py   # Logique complète d’Enigma
│    ├── key_utils.py        # Génération, sauvegarde et chargement des clés
│    └── utils.py            # Fonctions utilitaires
│
└── Key/
     └── (fichiers .json générés)

