# python-pendu 🪢

Un jeu du pendu en français avec une interface graphique **tkinter**.

## Fonctionnalités

- Interface graphique avec clavier alphabétique cliquable
- Dessin ASCII du pendu évoluant à chaque mauvaise réponse (7 tentatives)
- Mots tirés aléatoirement depuis un dictionnaire CSV (`dico.csv`)
- Mots filtrés : entre 3 et 10 lettres, sans tiret, sans accents
- Disponible en version exécutable Windows (`.exe`)

## Prérequis

- Python 3.x
- [pandas](https://pandas.pydata.org/) — pour la sélection du mot
- tkinter — inclus dans la bibliothèque standard Python

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/devfrp/python-pendu.git
cd python-pendu

# Installer les dépendances
pip install pandas
```

## Lancement

```bash
python pendu.py
```

## Version Windows (.exe)

Un exécutable Windows est disponible dans les [releases](https://github.com/devfrp/python-pendu/releases/tag/french). Il n'est pas nécessaire d'installer Python ou pandas pour l'utiliser.

## Compiler l'exécutable soi-même

Le projet utilise [PyInstaller](https://pyinstaller.org/) :

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "dico.csv;." pendu.py
```

L'exécutable se trouvera dans le dossier `dist/`.

## Structure du projet

| Fichier | Description |
|---|---|
| `pendu.py` | Application principale (interface tkinter + logique du jeu) |
| `choix_mot.py` | Sélection et normalisation d'un mot aléatoire |
| `dico.csv` | Dictionnaire de mots français |

## Règles du jeu

Le joueur doit deviner un mot lettre par lettre. Il dispose de **7 tentatives** avant que le pendu ne soit complet. À chaque mauvaise lettre, un élément du dessin ASCII s'affiche. Le mot est révélé en cas de défaite.
