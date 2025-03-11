# models.py
import json
import os


class Player:
    def __init__(self, player_id, name, age):
        self.id = player_id
        self.name = name
        self.age = age

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}

    @staticmethod
    def from_dict(player_dict):
        return Player(player_dict["id"], player_dict["name"], player_dict["age"])


class Tournament:
    def __init__(self, tournament_id, name, date):
        self.id = tournament_id
        self.name = name
        self.date = date

    def to_dict(self):
        return {"id": self.id, "name": self.name, "date": self.date}

    @staticmethod
    def from_dict(tournament_dict):
        return Tournament(
            tournament_dict["id"], tournament_dict["name"], tournament_dict["date"]
        )


class PlayerModel:
    FILE_PATH = "players.json"

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                json.dump([], file)

    def get_all_players(self):
        with open(self.FILE_PATH, "r") as file:
            players_dict = json.load(file)
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
        with open(self.FILE_PATH, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)
        return player

    def update_player(self, player_id, updated_data):
        players = self.get_all_players()
        for player in players:
            if player.id == player_id:
                player.name = updated_data["name"]
                player.age = updated_data["age"]
                with open(self.FILE_PATH, "w") as file:
                    json.dump([player.to_dict() for player in players], file, indent=4)
                return player
        return None

    def delete_player(self, player_id):
        players = self.get_all_players()
        players = [player for player in players if player.id != player_id]
        with open(self.FILE_PATH, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)
        return True


class TournamentModel:
    FILE_PATH = "tournaments.json"

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                json.dump([], file)

    def get_all_tournaments(self):
        with open(self.FILE_PATH, "r") as file:
            tournaments_dict = json.load(file)
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
        with open(self.FILE_PATH, "w") as file:
            json.dump(
                [tournament.to_dict() for tournament in tournaments], file, indent=4
            )
        return tournament

    def update_tournament(self, tournament_id, updated_data):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                tournament.name = updated_data["name"]
                tournament.date = updated_data["date"]
                with open(self.FILE_PATH, "w") as file:
                    json.dump(
                        [tournament.to_dict() for tournament in tournaments],
                        file,
                        indent=4,
                    )
                return tournament
        return None

    def delete_tournament(self, tournament_id):
        tournaments = self.get_all_tournaments()
        tournaments = [
            tournament for tournament in tournaments if tournament.id != tournament_id
        ]
        with open(self.FILE_PATH, "w") as file:
            json.dump(
                [tournament.to_dict() for tournament in tournaments], file, indent=4
            )
        return True


# views.py
class PlayerView:
    def display_all_players(self, players):
        for player in players:
            print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}")

    def display_player(self, player):
        if player:
            print(f"ID: {player.id}, Name: {player.name}, Age: {player.age}")
        else:
            print("Player not found.")

    def display_player_created(self, player):
        print(
            f"Player created: ID: {player.id}, Name: {player.name}, Age: {player.age}"
        )

    def display_player_updated(self, player):
        if player:
            print(
                f"Player updated: ID: {player.id}, Name: {player.name}, Age: {player.age}"
            )
        else:
            print("Player not found.")

    def display_player_deleted(self, success):
        if success:
            print("Player deleted.")
        else:
            print("Player not found.")


class TournamentView:
    def display_all_tournaments(self, tournaments):
        for tournament in tournaments:
            print(
                f"ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}"
            )

    def display_tournament(self, tournament):
        if tournament:
            print(
                f"ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}"
            )
        else:
            print("Tournament not found.")

    def display_tournament_created(self, tournament):
        print(
            f"Tournament created: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}"
        )

    def display_tournament_updated(self, tournament):
        if tournament:
            print(
                f"Tournament updated: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}"
            )
        else:
            print("Tournament not found.")

    def display_tournament_deleted(self, success):
        if success:
            print("Tournament deleted.")
        else:
            print("Tournament not found.")


# controllers.py
class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_all_players(self):
        players = self.model.get_all_players()
        self.view.display_all_players(players)

    def get_player_by_id(self, player_id):
        player = self.model.find_player_by_id(player_id)
        self.view.display_player(player)

    def create_player(self, name, age):
        player_id = len(self.model.get_all_players()) + 1
        player = Player(player_id, name, age)
        created_player = self.model.create_player(player)
        self.view.display_player_created(created_player)

    def update_player(self, player_id, name, age):
        updated_data = {"name": name, "age": age}
        player = self.model.update_player(player_id, updated_data)
        self.view.display_player_updated(player)

    def delete_player(self, player_id):
        success = self.model.delete_player(player_id)
        self.view.display_player_deleted(success)


class TournamentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_all_tournaments(self):
        tournaments = self.model.get_all_tournaments()
        self.view.display_all_tournaments(tournaments)

    def get_tournament_by_id(self, tournament_id):
        tournament = self.model.find_tournament_by_id(tournament_id)
        self.view.display_tournament(tournament)

    def create_tournament(self, name, date):
        tournament_id = len(self.model.get_all_tournaments()) + 1
        tournament = Tournament(tournament_id, name, date)
        created_tournament = self.model.create_tournament(tournament)
        self.view.display_tournament_created(created_tournament)

    def update_tournament(self, tournament_id, name, date):
        updated_data = {"name": name, "date": date}
        tournament = self.model.update_tournament(tournament_id, updated_data)
        self.view.display_tournament_updated(tournament)

    def delete_tournament(self, tournament_id):
        success = self.model.delete_tournament(tournament_id)
        self.view.display_tournament_deleted(success)


# main.py
from models import PlayerModel, TournamentModel
from views import PlayerView, TournamentView
from controllers import PlayerController, TournamentController


def main():
    # Initialize models, views, and controllers
    player_model = PlayerModel()
    player_view = PlayerView()
    player_controller = PlayerController(player_model, player_view)

    tournament_model = TournamentModel()
    tournament_view = TournamentView()
    tournament_controller = TournamentController(tournament_model, tournament_view)

    # Test PlayerController
    print("Creating players...")
    player_controller.create_player("Alice", 25)
    player_controller.create_player("Bob", 30)

    print("\nDisplaying all players...")
    player_controller.get_all_players()

    print("\nUpdating player with ID 1...")
    player_controller.update_player(1, "Alice Smith", 26)

    print("\nDisplaying player with ID 1...")
    player_controller.get_player_by_id(1)

    print("\nDeleting player with ID 2...")
    player_controller.delete_player(2)

    print("\nDisplaying all players...")
    player_controller.get_all_players()

    # Test TournamentController
    print("\nCreating tournaments...")
    tournament_controller.create_tournament("Tournament 1", "2023-10-01")
    tournament_controller.create_tournament("Tournament 2", "2023-11-01")

    print("\nDisplaying all tournaments...")
    tournament_controller.get_all_tournaments()

    print("\nUpdating tournament with ID 1...")
    tournament_controller.update_tournament(1, "Tournament 1 Updated", "2023-10-15")

    print("\nDisplaying tournament with ID 1...")
    tournament_controller.get_tournament_by_id(1)

    print("\nDeleting tournament with ID 2...")
    tournament_controller.delete_tournament(2)

    print("\nDisplaying all tournaments...")
    tournament_controller.get_all_tournaments()


if __name__ == "__main__":
    main()
