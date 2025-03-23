# Application tournois d'échecs

## Description
Ce projet est une application de gestion de tournois d'échecs. Elle permet de créer, gérer et suivre des tournois, les joueurs et leurs résultats.

Caractéristiques du programme :
- Création des joueurs.
- Création et gestion des tournois.
- Suivi des résultats des matchs.
- Génération de rapports HTML.

# Utilisation du programme

## Comment exécuter le script Python sous Windows ?

1. Dans l'__Explorateur de fichiers__, ouvrir votre dossier Windows "__Documents__"
2. Dans la barre d'adresse de la fenêtre __Explorateur de fichiers__ tapez `cmd` à la place de l'adresse `C:\Users\votre_nom\Documents` puis validez par "__Entrée__"
3. Tapez la texte ci-dessous dans l'__invite de commandes__.

```bash
  python "Scripts Python\Virtual Environment\project-4-chess-tournament-main\project-chess-tournament\chess_tournament.py"
```
Menu de l'application au lancement.

![Screenshot menu au lancement ](<docs/Use/2025-03-23 21_20_49-C__Windows_System32_cmd.exe - python  _Scripts Python_Virtual Environment_projec.png>)



# Générer un nouveau fichier flake8-html

Pour générer un nouveau fichier flake8-html dans le dossier "flake8-html-report", il faut utiliser l'outil `flake8-html`. Voici les étapes à suivre :

1. **Installer flake8-html** : Le package `flake8-html` devrait déjà être installé, car il est inclus dans le fichier requirements.txt.

2. **Créer un dossier pour le rapport** : Si le dossier "flake8-html-report" n'existe pas, créez-le dans votre projet.

3. **Exécuter flake8 avec flake8-html** : Utilisez la commande suivante pour générer un rapport HTML :
   ```bash
   flake8 --format=html --htmldir=flake8-html-report
   ```

Cela générera un fichier HTML dans le dossier "flake8-html-report". Vous pouvez ensuite ouvrir ce fichier dans un navigateur pour consulter le rapport.


# Installation de l'application
## Installation avec l'environnement virtuel
### 1e étape : Comment créer l'environnement virtuel ?
1. Dans l'__Explorateur de fichiers__, ouvrir votre dossier Windows "__Documents__"
2. Dans la barre d'adresse de la fenêtre __Explorateur de fichiers__ tapez `cmd` à la place de l'adresse `C:\Users\votre_nom\Documents` puis validez par "__Entrée__"
3. Tapez le texte ci-dessous dans l'__invite de commandes__.

```bash
  python -m venv "Scripts Python\Virtual Environment"
```
### 2e étape : Comment activer l'environnement virtuel ?
1. Tapez le texte ci-dessous dans l'__invite de commandes__.

```bash
  "Scripts Python\Virtual Environment\Scripts\activate.bat"
```
### 3e étape : Cloner le repository à partir de GitHub

1. Cliquez sur le bouton en vert nommé "__Code__"
2. Dans le menu déroulant, cliquez sur "__Download ZIP__"
4. Extraire le fichier "__project-4-chess-tournament-main.zip__" qui vient d'être téléchargé dans le dossier "__Virtual Environment__"

### 4e étape : Installer les paquets Python

1. Tapez le texte ci-dessous dans l'__invite de commandes__.

```bash
  pip install -r "Scripts Python\Virtual Environment\project-4-chess-tournament-main\requirements.txt"
```
