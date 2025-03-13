import json
import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime


# Modèles
class Player:
    def __init__(self, last_name, first_name, birth_date, id_chess):
        self.id = uuid.uuid4()
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = f"{self.first_name} {self.last_name}"
        self.birth_date = birth_date
        self.id_chess = id_chess

    def formatted_birth_date(self):
        """Returns the birth date in dd/mm/yyyy format."""
        if self.birth_date:
            try:
                birth_date = datetime.strptime(self.birth_date, "%Y-%m-%dT%H:%M:%S")
                return birth_date.strftime("%d/%m/%Y")
            except ValueError:
                return self.birth_date
        return None

    def to_dict(self):
        return {
            "id": str(self.id),
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "id_chess": self.id_chess,
        }

    @staticmethod
    def from_dict(player_dict):
        player = Player(
            player_dict["last_name"],
            player_dict["first_name"],
            player_dict["birth_date"],
            player_dict["id_chess"],
        )
        player.id = uuid.UUID(player_dict["id"])
        return player


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date=None,
        end_date=None,
        description=None,
        players_list=None,
        rounds_list=None,
        number_of_rounds=4,
    ):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = players_list if players_list is not None else []
        self.rounds = rounds_list if rounds_list is not None else []
        self.number_of_rounds = number_of_rounds
        self.current_round = 0

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def to_dict(self):
        """Convert Tournament object to dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "player_ids": [str(player.id) for player in self.players],
            "description": self.description,
            "rounds": [round.to_dict() for round in self.rounds],
            "number_of_rounds": self.number_of_rounds,
        }

    @staticmethod
    def from_dict(tournament_dict):
        """Create a Tournament object from a dictionary."""
        return Tournament(
            name=tournament_dict["name"],
            location=tournament_dict["location"],
            start_date=tournament_dict.get("start_date"),
            end_date=tournament_dict.get("end_date"),
            number_of_rounds=tournament_dict.get("number_of_rounds", 4),
            description=tournament_dict.get("description"),
            players=tournament_dict.get("players", []),
            rounds=tournament_dict.get("rounds", []),
        )


class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(
        self, player1: Player, player2: Player, player1_score=0, player2_score=0
    ):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def set_score(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def is_finished(self):
        """Returns True if player score 1 is not negative, False otherwise."""
        return self.player1_score >= 0

    def to_dict(self):
        return {
            "player1": {
                "id": str(self.player1.id),
                "last_name": self.player1.last_name,
                "first_name": self.player1.first_name,
            },
            "player1_score": self.player1_score,
            "player2": {
                "id": str(self.player2.id),
                "last_name": self.player2.last_name,
                "first_name": self.player2.first_name,
            },
            "player2_score": self.player2_score,
        }

    def get_player_names(self):
        """Returns a tuple of the full names of player1 and player2."""
        return self.player1.full_name, self.player2.full_name

    def get_player_names_and_scores(self):
        """Returns a tuple of the full names of player1, player2 and score."""
        names = self.get_player_names()
        scores = self.player1_score, self.player2_score
        return names + scores

    def get_player1(self):
        return self.player1.id, self.player1_score

    def get_player2(self):
        return self.player2.id, self.player2_score

    def __repr__(self):
        return (
            f"Match(player1={self.player1}, player2={self.player2}, "
            f"player1_score={self.player1_score}, "
            f"player2_score={self.player2_score})"
        )

    def __str__(self):
        """Returns a text representation of the match."""
        return (
            f"{' vs '.join(self.get_player_names())} "
            f" Scores: {self.player1_score} - {self.player2_score}"
        )


class Round:
    """Represents a round in a chess tournament."""

    def __init__(self, name, matches=None, start_datetime=None, end_datetime=None):
        self.name = name
        self.matches = (
            self.convert_dict_to_matches(matches) if matches is not None else []
        )
        self.start_datetime = (
            datetime.fromisoformat(start_datetime) if start_datetime else datetime.now()
        )
        self.end_datetime = (
            datetime.fromisoformat(end_datetime) if end_datetime else None
        )

    def convert_dict_to_matches(self, matches):
        return [
            Match(
                Player(match["player1"]["last_name"], match["player1"]["first_name"]),
                Player(match["player2"]["last_name"], match["player2"]["first_name"]),
                match["player1_score"],
                match["player2_score"],
            )
            for match in matches
        ]

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def end_round(self):
        """Marks the lap as completed and records the end time."""
        self.end_datetime = datetime.now()

    def is_finished(self):
        """Returns True if the round is completed, False otherwise."""
        return self.end_datetime is not None

    def get_pairs_players(self):
        """Returns the pairs of players (full name)."""
        return (
            self.name,
            [
                (
                    match.get_player_names_and_scores()
                    if match.is_finished()
                    else match.get_player_names()
                )
                for match in self.matches
            ],
        )

    def to_dict(self):
        """Convert Round object to dictionary."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat() if self.end_datetime else None
            ),
        }

    def __repr__(self):
        return f"Round(matches={self.matches})"

    def __str__(self):
        """Returns a string representation of the round."""
        matches_str = "\n".join(str(match) for match in self.matches)
        return (
            f"Round: {self.name}\n"
            f"Start: {self.start_datetime}\n"
            f"End: {self.end_datetime}\n"
            f"Matches:\n{matches_str}"
        )


# Dépôts de données
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

    def file_exists(self):
        return os.path.exists(self.file_path)

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


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_all_players(self):
        players_dict = self.file_service.read_from_file()
        return [Player.from_dict(player) for player in players_dict]

    def find_player_by_id(self, player_id):
        players = self.get_all_players()
        for player in players:
            if player.id == player_id:
                return player
        return None

    def create_player(self, player):
        players = self.get_all_players()
        players.append(player)
        self.file_service.write_to_file([player.to_dict() for player in players])
        return player

    def update_player(self, player_id, updated_data):
        players = self.get_all_players()
        for player in players:
            if str(player.id) == player_id:
                player.last_name = updated_data["last_name"]
                player.first_name = updated_data["first_name"]
                player.birth_date = updated_data["birth_date"]
                player.id_chess = updated_data["id_chess"]
                self.file_service.write_to_file(
                    [player.to_dict() for player in players]
                )
                return player
        return None


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_all_tournaments(self):
        tournaments_dict = self.file_service.read_from_file()
        return [Tournament.from_dict(tournament) for tournament in tournaments_dict]

    def find_tournament_by_id(self, tournament_id):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def create_tournament(self, tournament):
        tournaments = self.get_all_tournaments()
        tournaments.append(tournament)
        self.file_service.write_to_file(
            [tournament.to_dict() for tournament in tournaments]
        )
        return tournament

    def update_tournament(self, tournament_id, updated_data):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if str(tournament.id) == tournament_id:
                tournament.name = updated_data["name"]
                tournament.location = updated_data["location"]
                tournament.start_date = updated_data["start_date"]
                tournament.end_date = updated_data["end_date"]
                tournament.number_of_rounds = updated_data["number_of_rounds"]
                tournament.description = updated_data["description"]
                self.file_service.write_to_file(
                    [tournament.to_dict() for tournament in tournaments]
                )
                return tournament
        return None


# Vues
class PlayerView:
    def display_player(self, player):
        print(f"Player ID: {player.id}, Name: {player.last_name}")

    def display_players(self, players):
        for player in players:
            self.display_player(player)

    def display_player_created(self, player):
        print(f"Player created: ID: {player.id}, Name: {player.last_name}")

    def display_player_updated(self, player):
        print(f"Player updated: ID: {player.id}, Name: {player.last_name}")


class TournamentView:
    def display_tournament(self, tournament):
        print(
            f"Tournament ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.location}"
        )

    def display_tournaments(self, tournaments):
        for tournament in tournaments:
            self.display_tournament(tournament)

    def display_tournament_created(self, tournament):
        print(
            f"Tournament created: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.location}"
        )

    def display_tournament_updated(self, tournament):
        print(
            f"Tournament updated: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.location}"
        )


# Contrôleurs
class PlayerController:
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view

    def get_all_players(self):
        players = self.repository.get_all_players()
        self.view.display_players(players)

    def get_player_by_id(self, player_id):
        player = self.repository.find_player_by_id(player_id)
        if player:
            self.view.display_player(player)
        else:
            print("Player not found.")

    def create_player(self, last_name, first_name, birth_date, id_chess):
        player = Player(last_name, first_name, birth_date, id_chess)
        self.repository.create_player(player)
        self.view.display_player_created(player)

    def update_player(self, player_id, last_name, first_name, birth_date, id_chess):
        player = self.repository.update_player(
            player_id,
            {
                "last_name": last_name,
                "first_name": first_name,
                "birth_date": birth_date,
                "id_chess": id_chess,
            },
        )
        if player:
            self.view.display_player_updated(player)
        else:
            print("Player not found.")


class TournamentController:
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view

    def get_all_tournaments(self):
        tournaments = self.repository.get_all_tournaments()
        self.view.display_tournaments(tournaments)

    def get_tournament_by_id(self, tournament_id):
        tournament = self.repository.find_tournament_by_id(tournament_id)
        if tournament:
            self.view.display_tournament(tournament)
        else:
            print("Tournament not found.")

    def create_tournament(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_rounds,
        description=None,
        player_ids=None,
        rounds_list=None,
    ):
        players_list = (
            [self.all_players[player_id] for player_id in player_ids]
            if player_ids
            else []
        )
        rounds_list = [Round(**round) for round in rounds_list] if rounds_list else []
        tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            number_of_rounds,
            description,
            players_list,
            rounds_list,
        )
        self.active_tournament = tournament
        self.tournaments.append(tournament)
        created_tournament = self.repository.create_tournament(tournament)
        self.view.display_tournament_created(created_tournament)

    def update_tournament(self, tournament_id, name, date):
        tournament = self.repository.update_tournament(
            tournament_id, {"name": name, "date": date}
        )
        if tournament:
            self.view.display_tournament_updated(tournament)
        else:
            print("Tournament not found.")


# Interface de commande
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Commandes concrètes
class CreatePlayerCommand(Command):
    def __init__(self, controller, last_name, first_name, birth_date, id_chess):
        self.controller = controller
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id_chess = id_chess

    def execute(self):
        self.controller.create_player(
            self.last_name, self.first_name, self.birth_date, self.id_chess
        )


class GetAllPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.get_all_players()


class UpdatePlayerCommand(Command):
    def __init__(
        self, controller, player_id, last_name, first_name, birth_date, id_chess
    ):
        self.controller = controller
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id_chess = id_chess

    def execute(self):
        self.controller.update_player(
            self.player_id,
            self.last_name,
            self.first_name,
            self.birth_date,
            self.id_chess,
        )


class GetPlayerByIdCommand(Command):
    def __init__(self, controller, player_id):
        self.controller = controller
        self.player_id = player_id

    def execute(self):
        self.controller.get_player_by_id(self.player_id)


class CreateTournamentCommand(Command):
    def __init__(self, controller, name, location):
        self.controller = controller
        self.name = name
        self.location = location

    def execute(self):
        self.controller.create_tournament(self.name, self.location, None, None, 4)


class GetAllTournamentsCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.get_all_tournaments()


class UpdateTournamentCommand(Command):
    def __init__(
        self,
        controller,
        tournament_id,
        name,
        location,
        start_date,
        end_date,
        description,
        number_of_rounds,
    ):
        self.controller = controller
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds

    def execute(self):
        self.controller.update_tournament(
            self.tournament_id,
            self.name,
            self.location,
            self.start_date,
            self.end_date,
            self.description,
            self.number_of_rounds,
        )


class GetTournamentByIdCommand(Command):
    def __init__(self, controller, tournament_id):
        self.controller = controller
        self.tournament_id = tournament_id

    def execute(self):
        self.controller.get_tournament_by_id(self.tournament_id)


# Vue du menu
class MenuView:
    def display_menu(self, tournament_loaded):
        print("\nMenu:")
        print("1. Create Player")
        print("2. Get All Players")
        print("3. Update Player")
        print("4. Get Player by ID")
        print("5. Delete Player")
        print("6. Create Tournament")
        print("7. Get All Tournaments")

        if tournament_loaded:
            print("8. Update Tournament")
            print("9. Get Tournament by ID")
            print("10. Delete Tournament")

        print("11. Quit")

    def get_user_choice(self):
        return input("Choose an option: ")

    def display_message(self, message):
        print(message)


# Contrôleur du menu
class MenuController:
    def __init__(self, view, player_controller, tournament_controller):
        self.view = view
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller
        self.tournament_loaded = False

    def execute_choice(self, choice):
        if choice == "1":
            last_name = input("Enter player last_name: ")
            first_name = input("Enter player first_name: ")
            birth_date = input("Enter player birth_date: ")
            id_chess = input("Enter player id_chess: ")
            command = CreatePlayerCommand(
                self.player_controller, last_name, first_name, birth_date, id_chess
            )
        elif choice == "2":
            command = GetAllPlayersCommand(self.player_controller)
        elif choice == "3":
            player_id = int(input("Enter player ID to update: "))
            command = UpdatePlayerCommand(
                self.player_controller,
                player_id,
                last_name,
                first_name,
                birth_date,
                id_chess,
            )
        elif choice == "4":
            player_id = int(input("Enter player ID: "))
            command = GetPlayerByIdCommand(self.player_controller, player_id)
        elif choice == "5":
            player_id = int(input("Enter player ID to delete: "))
        elif choice == "6":
            name = input("Enter tournament name: ")
            location = input("Enter tournament location: ")
            command = CreateTournamentCommand(
                self.tournament_controller, name, location
            )
            self.tournament_loaded = True  # Tournament is loaded after creation
        elif choice == "7":
            command = GetAllTournamentsCommand(self.tournament_controller)
            self.tournament_loaded = True  # Tournament is loaded after retrieval
        elif choice == "8" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID to update: "))
            name = input("Enter new name: ")
            location = input("Enter new location: ")
            command = UpdateTournamentCommand(
                self.tournament_controller, tournament_id, name, location
            )
        elif choice == "9" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID: "))
            command = GetTournamentByIdCommand(
                self.tournament_controller, tournament_id
            )
        elif choice == "10" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID to delete: "))
            self.tournament_loaded = False  # Tournament is unloaded after deletion
        elif choice == "11":
            self.view.display_message("Goodbye!")
            return None
        else:
            self.view.display_message("Invalid choice. Please try again.")
            return self.execute_choice(self.view.get_user_choice())

        return command


def main():
    # Initialisation des contrôleurs
    player_controller = PlayerController(PlayerRepository(), PlayerView())
    tournament_controller = TournamentController(
        TournamentRepository(), TournamentView()
    )

    # Initialisation du contrôleur de menu
    menu_view = MenuView()
    menu_controller = MenuController(
        menu_view, player_controller, tournament_controller
    )

    while True:
        menu_view.display_menu(menu_controller.tournament_loaded)
        choice = menu_view.get_user_choice()
        command = menu_controller.execute_choice(choice)

        if command is None:
            break

        command.execute()


if __name__ == "__main__":
    main()
