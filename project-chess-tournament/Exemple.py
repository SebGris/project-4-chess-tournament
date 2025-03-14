import json
from typing import List


class BaseRepository:
    def get_file_path(self):
        raise NotImplementedError("Subclasses should implement this method.")


class FileService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_to_file(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_file_path(self):
        return self.FILE_PATH

    def get_all_tournaments(self) -> List["Tournament"]:
        tournaments_dict = self.file_service.read_from_file()
        return [Tournament.from_dict(tournament) for tournament in tournaments_dict]

    def find_tournament_by_id(self, tournament_id):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def save_tournaments(self, tournaments: List["Tournament"]):
        tournaments_dict = [tournament.to_dict() for tournament in tournaments]
        self.file_service.write_to_file(tournaments_dict)


class Tournament:
    def __init__(self, id, nom, date, lieu):
        self.id = id
        self.nom = nom
        self.date = date
        self.lieu = lieu
        self.parties = []

    @classmethod
    def from_dict(cls, dict_):
        tournament = cls(dict_["id"], dict_["nom"], dict_["date"], dict_["lieu"])
        tournament.parties = [
            Partie.from_dict(partie) for partie in dict_.get("parties", [])
        ]
        return tournament

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "date": self.date,
            "lieu": self.lieu,
            "parties": [partie.to_dict() for partie in self.parties],
        }

    def ajouter_partie(self, partie):
        self.parties.append(partie)


class Partie:
    def __init__(self, joueur1, joueur2, resultat=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat

    @classmethod
    def from_dict(cls, dict_):
        joueur1 = Joueur(**dict_["joueur1"])
        joueur2 = Joueur(**dict_["joueur2"])
        return cls(joueur1, joueur2, dict_.get("resultat"))

    def to_dict(self):
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "resultat": self.resultat,
        }


class Joueur:
    def __init__(self, nom, classement):
        self.nom = nom
        self.classement = classement

    def to_dict(self):
        return {"nom": self.nom, "classement": self.classement}


class Modele:
    def __init__(self, repository):
        self.repository = repository
        self.tournois = self.repository.get_all_tournaments()
        self.tournoi_actif = None

    def ajouter_tournoi(self, tournoi):
        self.tournois.append(tournoi)
        self.repository.save_tournaments(self.tournois)

    def selectionner_tournoi(self, nom):
        for tournoi in self.tournois:
            if tournoi.nom == nom:
                self.tournoi_actif = tournoi
                print(f"Tournoi actif : {tournoi.nom}")
                return
        print("Tournoi non trouvé.")

    def obtenir_tournoi_actif(self):
        return self.tournoi_actif

    def lister_tournois(self):
        return [tournoi.nom for tournoi in self.tournois]


class VueTournoi:
    def afficher_tournoi(self, tournoi):
        print(f"Tournoi: {tournoi.nom}, Date: {tournoi.date}, Lieu: {tournoi.lieu}")
        for partie in tournoi.parties:
            print(
                f"Partie entre {partie.joueur1.nom} et {partie.joueur2.nom}, Résultat: {partie.resultat}"
            )


class ControleurTournoi:
    def __init__(self, modele, vue):
        self.modele = modele
        self.vue = vue

    def creer_tournoi(self, nom, date, lieu, id):
        tournoi = Tournament(id, nom, date, lieu)
        self.modele.ajouter_tournoi(tournoi)
        print(f"Tournoi '{nom}' créé avec succès.")

    def selectionner_tournoi(self, nom):
        self.modele.selectionner_tournoi(nom)

    def ajouter_partie(self, joueur1, joueur2, resultat=None):
        tournoi_actif = self.modele.obtenir_tournoi_actif()
        if tournoi_actif:
            partie = Partie(joueur1, joueur2, resultat)
            tournoi_actif.ajouter_partie(partie)
            self.modele.repository.save_tournaments(self.modele.tournois)
            print("Partie ajoutée avec succès.")
        else:
            print("Aucun tournoi actif sélectionné.")

    def mettre_a_jour_resultat(self, index_partie, resultat):
        tournoi_actif = self.modele.obtenir_tournoi_actif()
        if tournoi_actif and 0 <= index_partie < len(tournoi_actif.parties):
            tournoi_actif.parties[index_partie].resultat = resultat
            self.modele.repository.save_tournaments(self.modele.tournois)
            print("Résultat mis à jour avec succès.")
        else:
            print("Index de partie invalide ou aucun tournoi actif.")

    def afficher_tournoi(self):
        tournoi_actif = self.modele.obtenir_tournoi_actif()
        if tournoi_actif:
            self.vue.afficher_tournoi(tournoi_actif)
        else:
            print("Aucun tournoi actif sélectionné.")

    def afficher_parties_sans_resultat(self):
        tournoi_actif = self.modele.obtenir_tournoi_actif()
        if tournoi_actif:
            parties_sans_resultat = [
                partie for partie in tournoi_actif.parties if partie.resultat is None
            ]
            if parties_sans_resultat:
                print("Parties sans résultat :")
                for partie in parties_sans_resultat:
                    print(f"Partie entre {partie.joueur1.nom} et {partie.joueur2.nom}")
            else:
                print("Toutes les parties ont un résultat.")
        else:
            print("Aucun tournoi actif sélectionné.")

    def lister_tournois(self):
        tournois = self.modele.lister_tournois()
        if tournois:
            print("Tournois disponibles :")
            for nom in tournois:
                print(f"- {nom}")
        else:
            print("Aucun tournoi disponible.")


class Application:
    def __init__(self):
        repository = TournamentRepository()
        self.modele = Modele(repository)
        self.vue = VueTournoi()
        self.controleur = ControleurTournoi(self.modele, self.vue)

    def afficher_menu(self):
        tournoi_actif = self.modele.obtenir_tournoi_actif()
        if tournoi_actif:
            print("\nActions disponibles (Tournoi actif) :")
            print("1. Ajouter une partie")
            print("2. Mettre à jour le résultat d'une partie")
            print("3. Afficher les détails du tournoi")
            print("4. Afficher les parties sans résultat")
            print("5. Sélectionner un autre tournoi")
            print("6. Quitter")
        else:
            print("\nActions disponibles (Aucun tournoi actif) :")
            print("1. Créer un nouveau tournoi")
            print("2. Sélectionner un tournoi")
            print("3. Lister les tournois")
            print("4. Quitter")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une action : ")

            if not self.modele.obtenir_tournoi_actif():
                if choix == "1":
                    nom = input("Nom du tournoi : ")
                    date = input("Date du tournoi : ")
                    lieu = input("Lieu du tournoi : ")
                    id = input("ID du tournoi : ")
                    self.controleur.creer_tournoi(nom, date, lieu, id)

                elif choix == "2":
                    self.controleur.lister_tournois()
                    nom = input("Nom du tournoi à sélectionner : ")
                    self.controleur.selectionner_tournoi(nom)

                elif choix == "3":
                    self.controleur.lister_tournois()

                elif choix == "4":
                    print("Fin du programme.")
                    break

                else:
                    print("Choix invalide. Veuillez réessayer.")

            else:
                if choix == "1":
                    nom1 = input("Nom du joueur 1 : ")
                    nom2 = input("Nom du joueur 2 : ")
                    classement1 = int(input("Classement du joueur 1 : "))
                    classement2 = int(input("Classement du joueur 2 : "))
                    joueur1 = Joueur(nom1, classement1)
                    joueur2 = Joueur(nom2, classement2)
                    self.controleur.ajouter_partie(joueur1, joueur2)

                elif choix == "2":
                    index = int(input("Index de la partie à mettre à jour : "))
                    resultat = input("Nouveau résultat : ")
                    self.controleur.mettre_a_jour_resultat(index, resultat)

                elif choix == "3":
                    self.controleur.afficher_tournoi()

                elif choix == "4":
                    self.controleur.afficher_parties_sans_resultat()

                elif choix == "5":
                    self.controleur.lister_tournois()
                    nom = input("Nom du tournoi à sélectionner : ")
                    self.controleur.selectionner_tournoi(nom)

                elif choix == "6":
                    print("Fin du programme.")
                    break

                else:
                    print("Choix invalide. Veuillez réessayer.")


# Exécution de l'application
app = Application()
app.executer()
