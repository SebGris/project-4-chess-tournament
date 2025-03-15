import json
import os
import uuid
from typing import List


class BaseRepository:
    FILE_PATH = ""

    def __init__(self):
        if not os.path.exists(self.get_file_path()):
            with open(self.get_file_path(), "w") as file:
                json.dump([], file)

    def get_file_path(self, folder="data/tournaments"):
        data_folder = os.path.join(os.getcwd(), folder)
        os.makedirs(data_folder, exist_ok=True)
        return os.path.join(data_folder, self.FILE_PATH)


class FileService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Fichier non trouvé")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON")

    def write_to_file(self, data):
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise ValueError("Erreur d'écriture du fichier")


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self, player_repository: "PlayerRepository"):
        super().__init__()
        self.file_service = FileService(self.get_file_path())
        self.player_repository = player_repository

    def get_all_tournaments(self) -> List["Tournament"]:
        tournaments_dict = self.file_service.read_from_file()
        players = self.player_repository.get_all_players()
        players_dict = {player.id: player for player in players}
        return [Tournament.from_dict(tournament, players_dict) for tournament in tournaments_dict]

    def find_tournament_by_id(self, tournament_id):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def save_tournaments(self, tournaments: List["Tournament"]):
        tournaments_dict = [tournament.to_dict() for tournament in tournaments]
        self.file_service.write_to_file(tournaments_dict)


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_all_players(self) -> List["Player"]:
        players_dict = self.file_service.read_from_file()
        return [Player(**player) for player in players_dict]

    def find_player_by_id(self, player_id):
        players = self.get_all_players()
        for player in players:
            if player.id == player_id:
                return player
        return None

    def save_players(self, players: List["Player"]):
        players_dict = [player.to_dict() for player in players]
        self.file_service.write_to_file(players_dict)


class Player:
    def __init__(self, first_name, last_name, classement, player_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.classement = classement
        self.id = player_id or uuid.uuid4()

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "classement": self.classement,
            "id": str(self.id)
        }

    @classmethod
    def from_dict(dict_):
        return Player(
            dict_["first_name"],
            dict_["last_name"],
            dict_["classement"],
            dict_.get("id")
        )


class Tournament:
    def __init__(self, nom, date, lieu, tournament_id=None):
        self.nom = nom
        self.date = date
        self.lieu = lieu
        self.players = []
        self.rounds = []
        self.id = tournament_id or str(uuid.uuid4())

    def add_player(self, player: Player):
        self.players.append(player)

    def add_players(self, players: List[Player]):
        self.players.extend(players)

    @classmethod
    def from_dict(dict_, players_dict):
        tournament = Tournament(dict_["nom"], dict_["date"], dict_["lieu"], dict_.get("id"))
        tournament.add_players([players_dict[player_id] for player_id in dict_.get("player_ids", [])])
        tournament.rounds = [
            Round.from_dict(round, players_dict) for round in dict_.get("rounds", [])
        ]
        return tournament

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "date": self.date,
            "lieu": self.lieu,
            "player_ids": [player.id for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

    def ajouter_round(self, round: "Round"):  # Correction du type
        self.rounds.append(round)


class Round:
    def __init__(self, joueur1, joueur2, resultat=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat

    @classmethod
    def from_dict(cls, dict_, players_dict):
        joueur1 = players_dict[dict_["joueur1"]]
        joueur2 = players_dict[dict_["joueur2"]]
        return cls(joueur1, joueur2, dict_.get("resultat"))

    def to_dict(self):
        return {
            "joueur1": self.joueur1.id,
            "joueur2": self.joueur2.id,
            "resultat": self.resultat,
        }


class TournamentManager:
    def __init__(
        self,
        tournament_repository: TournamentRepository
    ):
        self.tournament_repository = tournament_repository
        self.tournois = self.tournament_repository.get_all_tournaments()
        self.tournoi_actif = None

    def add_tournament(self, tournoi):
        self.tournois.append(tournoi)
        self.tournament_repository.save_tournaments(self.tournois)

    def select_tournament(self, nom):
        for tournoi in self.tournois:
            if tournoi.nom == nom:
                self.tournoi_actif = tournoi
                print(f"Tournoi actif : {tournoi.nom}")
                return
        print("Tournoi non trouvé.")

    def get_active_tournament(self):
        return self.tournoi_actif

    def lister_tournois(self):
        return [tournoi.nom for tournoi in self.tournois]


class TournamentView:
    def afficher_tournoi(self, tournoi):
        print(f"Tournoi: {tournoi.nom}, Date: {tournoi.date}, Lieu: {tournoi.lieu}")
        for round in tournoi.rounds:
            print(
                f"Partie entre {round.joueur1.first_name} {round.joueur1.last_name} et {round.joueur2.first_name} {round.joueur2.last_name}, Résultat: {round.resultat}"
            )


class TournamentController:
    def __init__(self, manager: TournamentManager, view: TournamentView):
        self.tournament_manager = manager
        self.tournament_view = view

    def create_tournament(self, nom, date, lieu, tournament_id):
        tournament = Tournament(nom, date, lieu, tournament_id)
        self.tournament_manager.add_tournament(tournament)
        print(f"Tournoi '{nom}' créé avec succès.")

    def selectionner_tournoi(self, nom):
        self.tournament_manager.select_tournament(nom)

    def ajouter_round(self, joueur1, joueur2, resultat=None):
        tournoi_actif = self.tournament_manager.get_active_tournament()
        if tournoi_actif:
            round = Round(joueur1, joueur2, resultat)
            tournoi_actif.ajouter_round(round)
            self.tournament_manager.tournament_repository.save_tournaments(self.tournament_manager.tournois)
            print("Partie ajoutée avec succès.")
        else:
            print("Aucun tournoi actif sélectionné.")

    def mettre_a_jour_resultat(self, index_round, resultat):
        tournoi_actif = self.tournament_manager.get_active_tournament()
        if tournoi_actif and 0 <= index_round < len(tournoi_actif.rounds):
            tournoi_actif.rounds[index_round].resultat = resultat
            self.tournament_manager.tournament_repository.save_tournaments(self.tournament_manager.tournois)
            print("Résultat mis à jour avec succès.")
        else:
            print("Index de round invalide ou aucun tournoi actif.")

    def afficher_tournoi(self):
        tournoi_actif = self.tournament_manager.get_active_tournament()
        if tournoi_actif:
            self.tournament_view.afficher_tournoi(tournoi_actif)
        else:
            print("Aucun tournoi actif sélectionné.")

    def afficher_rounds_sans_resultat(self):
        tournoi_actif = self.tournament_manager.get_active_tournament()
        if tournoi_actif:
            rounds_sans_resultat = [
                round for round in tournoi_actif.rounds if round.resultat is None
            ]
            if rounds_sans_resultat:
                print("Parties sans résultat :")
                for round in rounds_sans_resultat:
                    print(f"Partie entre {round.joueur1.first_name} {round.joueur1.last_name} et {round.joueur2.first_name} {round.joueur2.last_name}")
            else:
                print("Toutes les rounds ont un résultat.")
        else:
            print("Aucun tournoi actif sélectionné.")

    def display_available_tournaments(self):
        tournois = self.tournament_manager.lister_tournois()
        if tournois:
            print("Tournois disponibles :")
            for nom in tournois:
                print(f"- {nom}")
        else:
            print("Aucun tournoi disponible.")


class Application:
    def __init__(self):
        player_repository = PlayerRepository()
        tournament_repository = TournamentRepository(player_repository)
        self.tournament_manager = TournamentManager(tournament_repository)
        self.tournament_view = TournamentView()
        self.tournament_controller = TournamentController(
            self.tournament_manager, self.tournament_view
        )

    def afficher_menu(self):
        tournoi_actif = self.tournament_manager.get_active_tournament()
        if tournoi_actif:
            print("\nActions disponibles (Tournoi actif) :")
            print("1. Ajouter une round")
            print("2. Mettre à jour le résultat d'une round")
            print("3. Afficher les détails du tournoi")
            print("4. Afficher les rounds sans résultat")
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

            if not self.tournament_manager.get_active_tournament():
                if choix == "1":
                    nom = input("Nom du tournoi : ")
                    date = input("Date du tournoi : ")
                    lieu = input("Lieu du tournoi : ")
                    tournament_id = input("ID du tournoi : ")
                    self.tournament_controller.create_tournament(nom, date, lieu, tournament_id)

                elif choix == "2":
                    self.tournament_controller.display_available_tournaments()
                    nom = input("Nom du tournoi à sélectionner : ")
                    self.tournament_controller.selectionner_tournoi(nom)

                elif choix == "3":
                    self.tournament_controller.display_available_tournaments()

                elif choix == "4":
                    print("Fin du programme.")
                    break

                else:
                    print("Choix invalide. Veuillez réessayer.")

            else:
                if choix == "1":
                    nom1 = input("Nom du joueur 1 : ")
                    prenom1 = input("Prénom du joueur 1 : ")
                    nom2 = input("Nom du joueur 2 : ")
                    prenom2 = input("Prénom du joueur 2 : ")
                    classement1 = int(input("Classement du joueur 1 : "))
                    classement2 = int(input("Classement du joueur 2 : "))
                    joueur1 = Player(prenom1, nom1, classement1)
                    joueur2 = Player(prenom2, nom2, classement2)
                    self.tournament_controller.ajouter_round(joueur1, joueur2)

                elif choix == "2":
                    index = int(input("Index de la round à mettre à jour : "))
                    resultat = input("Nouveau résultat : ")
                    self.tournament_controller.mettre_a_jour_resultat(index, resultat)

                elif choix == "3":
                    self.tournament_controller.afficher_tournoi()

                elif choix == "4":
                    self.tournament_controller.afficher_rounds_sans_resultat()

                elif choix == "5":
                    self.tournament_controller.display_available_tournaments()
                    nom = input("Nom du tournoi à sélectionner : ")
                    self.tournament_controller.selectionner_tournoi(nom)

                elif choix == "6":
                    print("Fin du programme.")
                    break

                else:
                    print("Choix invalide. Veuillez réessayer.")


# Exécution de l'application
app = Application()
app.executer()
