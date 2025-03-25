# Application de gestion de tournois d'échecs

## Description
Ce projet est une application de gestion de tournois d'échecs. Elle permet de créer, gérer et suivre des tournois, les joueurs et leurs résultats. L'application utilise le format JSON pour les fichiers de données, stockés dans le répertoire `data\tournaments`.

### Fonctionnalités principales :
- Création de joueurs.
- Création et gestion de tournois.
- Suivi des résultats des matchs.
- Génération de rapports HTML.

## Utilisation du programme

### 1. Comment exécuter le script Python sous Windows ?

1. Dans l'__Explorateur de fichiers__, ouvrez votre dossier Windows "__Documents__".
2. Dans la barre d'adresse de la fenêtre __Explorateur de fichiers__, tapez `cmd` à la place de l'adresse `C:\Users\votre_nom\Documents`, puis validez par "__Entrée__".
3. Tapez la commande suivante dans l'__invite de commandes__ :

```bash
python "Scripts Python\Virtual Environment\project-4-chess-tournament-main\project-chess-tournament\chess_tournament.py"
```

### 2. Menu au premier lancement de l'application

Aide rapide sur les éléments des menus :
- Le choix "__Saisir des joueurs__" permet d'ajouter des joueurs sans les rattacher à un tournoi.
- Le choix "__Nouveau tournoi__" permet de créer un tournoi.
- Le menu "__Rapport__" affiche chaque rapport dans un nouvel onglet de votre navigateur web.

_Exemple du menu lorsque le fichier JSON des tournois est vide :_

![Capture d'écran du menu au lancement sans tournoi](<docs/Use/2025-03-23 21_46_37-C__Windows_System32_cmd.exe - python  _Scripts Python_Virtual Environment_projec.png>)

_Exemple du menu lorsque des tournois existent déjà :_

![Capture d'écran du menu au lancement avec tournoi](<docs/Use/2025-03-23 21_56_37-C__Windows_System32_cmd.exe - python  _Scripts Python_Virtual Environment_projec.png>)

### 3. Comment sélectionner un tournoi ?

Le choix "__Sélectionner un tournoi__" permet de sélectionner le tournoi sur lequel des saisies seront effectuées.

![Capture d'écran du menu pour sélectionner un tournoi](<docs/Use/2025-03-23 22_06_34-C__Windows_System32_cmd.exe - python  _Scripts Python_Virtual Environment_projec.png>)

_Exemple du menu après la sélection d'un tournoi :_

![Capture d'écran du menu après avoir sélectionné un tournoi](<docs/Use/2025-03-23 22_10_45-C__Windows_System32_cmd.exe - python  _Scripts Python_Virtual Environment_projec.png>)

## Générer un nouveau fichier flake8-html

Pour générer un nouveau fichier flake8-html dans le dossier `flake8-html-report`, utilisez l'outil `flake8-html`. Voici les étapes à suivre :

1. **Installer flake8-html** : Le package `flake8-html` devrait déjà être installé, car il est inclus dans le fichier `requirements.txt`.

2. **Créer un dossier pour le rapport** : Si le dossier `flake8-html-report` n'existe pas, créez-le dans votre projet.

3. **Exécuter flake8 avec flake8-html** : Utilisez la commande suivante pour générer un rapport HTML :
   ```bash
   flake8 --format=html --htmldir=flake8-html-report
   ```

Cela générera un fichier HTML dans le dossier `flake8-html-report`. Vous pouvez ensuite ouvrir ce fichier dans un navigateur pour consulter le rapport.

## Installation de l'application

### Installation avec l'environnement virtuel

#### Étape 1 : Comment créer l'environnement virtuel ?
1. Dans l'__Explorateur de fichiers__, ouvrez votre dossier Windows "__Documents__".
2. Dans la barre d'adresse de la fenêtre __Explorateur de fichiers__, tapez `cmd` à la place de l'adresse `C:\Users\votre_nom\Documents`, puis validez par "__Entrée__".
3. Tapez la commande suivante dans l'__invite de commandes__ :

```bash
python -m venv "Scripts Python\Virtual Environment"
```

#### Étape 2 : Comment activer l'environnement virtuel ?
1. Tapez la commande suivante dans l'__invite de commandes__ :

```bash
"Scripts Python\Virtual Environment\Scripts\activate.bat"
```

#### Étape 3 : Cloner le dépôt depuis GitHub

1. Cliquez sur le bouton vert nommé "__Code__".
2. Dans le menu déroulant, cliquez sur "__Download ZIP__".
3. Extrayez le fichier `project-4-chess-tournament-main.zip` qui vient d'être téléchargé dans le dossier `Virtual Environment`.

#### Étape 4 : Installer les paquets Python

1. Tapez la commande suivante dans l'__invite de commandes__ :

```bash
pip install -r "Scripts Python\Virtual Environment\project-4-chess-tournament-main\requirements.txt"
```
