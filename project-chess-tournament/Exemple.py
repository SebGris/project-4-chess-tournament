import json
import os
from abc import ABC, abstractmethod

# Modèles
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

# Dépôts de données
class PlayerRepository:
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

class TournamentRepository:
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
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)
        return tournament

    def update_tournament(self, tournament_id, updated_data):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                tournament.name = updated_data["name"]
                tournament.date = updated_data["date"]
                with open(self.FILE_PATH, "w") as file:
                    json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)
                return tournament
        return None

    def delete_tournament(self, tournament_id):
        tournaments = self.get_all_tournaments()
        tournaments = [tournament for tournament in tournaments if tournament.id != tournament_id]
        with open(self.FILE_PATH, "w") as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)
        return True

# Vues
class PlayerView:
    def display_player(self, player):
        print(f"Player ID: {player.id}, Name: {player.name}, Age: {player.age}")

    def display_players(self, players):
        for player in players:
            self.display_player(player)

    def display_player_created(self, player):
        print(f"Player created: ID: {player.id}, Name: {player.name}, Age: {player.age}")

    def display_player_updated(self, player):
        print(f"Player updated: ID: {player.id}, Name: {player.name}, Age: {player.age}")

    def display_player_deleted(self, success):
        print(f"Player deleted: {success}")

class TournamentView:
    def display_tournament(self, tournament):
        print(f"Tournament ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}")

    def display_tournaments(self, tournaments):
        for tournament in tournaments:
            self.display_tournament(tournament)

    def display_tournament_created(self, tournament):
        print(f"Tournament created: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}")

    def display_tournament_updated(self, tournament):
        print(f"Tournament updated: ID: {tournament.id}, Name: {tournament.name}, Date: {tournament.date}")

    def display_tournament_deleted(self, success):
        print(f"Tournament deleted: {success}")

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

    def create_player(self, name, age):
        player_id = len(self.repository.get_all_players()) + 1
        player = Player(player_id, name, age)
        self.repository.create_player(player)
        self.view.display_player_created(player)

    def update_player(self, player_id, name, age):
        player = self.repository.update_player(player_id, {"name": name, "age": age})
        if player:
            self.view.display_player_updated(player)
        else:
            print("Player not found.")

    def delete_player(self, player_id):
        success = self.repository.delete_player(player_id)
        self.view.display_player_deleted(success)

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

    def create_tournament(self, name, date):
        tournament_id = len(self.repository.get_all_tournaments()) + 1
        tournament = Tournament(tournament_id, name, date)
        self.repository.create_tournament(tournament)
        self.view.display_tournament_created(tournament)

    def update_tournament(self, tournament_id, name, date):
        tournament = self.repository.update_tournament(tournament_id, {"name": name, "date": date})
        if tournament:
            self.view.display_tournament_updated(tournament)
        else:
            print("Tournament not found.")

    def delete_tournament(self, tournament_id):
        success = self.repository.delete_tournament(tournament_id)
        self.view.display_tournament_deleted(success)

# Interface de commande
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Commandes concrètes
class CreatePlayerCommand(Command):
    def __init__(self, controller, name, age):
        self.controller = controller
        self.name = name
        self.age = age

    def execute(self):
        self.controller.create_player(self.name, self.age)

class GetAllPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.get_all_players()

class UpdatePlayerCommand(Command):
    def __init__(self, controller, player_id, name, age):
        self.controller = controller
        self.player_id = player_id
        self.name = name
        self.age = age

    def execute(self):
        self.controller.update_player(self.player_id, self.name, self.age)

class GetPlayerByIdCommand(Command):
    def __init__(self, controller, player_id):
        self.controller = controller
        self.player_id = player_id

    def execute(self):
        self.controller.get_player_by_id(self.player_id)

class DeletePlayerCommand(Command):
    def __init__(self, controller, player_id):
        self.controller = controller
        self.player_id = player_id

    def execute(self):
        self.controller.delete_player(self.player_id)

class CreateTournamentCommand(Command):
    def __init__(self, controller, name, date):
        self.controller = controller
        self.name = name
        self.date = date

    def execute(self):
        self.controller.create_tournament(self.name, self.date)

class GetAllTournamentsCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.get_all_tournaments()

class UpdateTournamentCommand(Command):
    def __init__(self, controller, tournament_id, name, date):
        self.controller = controller
        self.tournament_id = tournament_id
        self.name = name
        self.date = date

    def execute(self):
        self.controller.update_tournament(self.tournament_id, self.name, self.date)

class GetTournamentByIdCommand(Command):
    def __init__(self, controller, tournament_id):
        self.controller = controller
        self.tournament_id = tournament_id

    def execute(self):
        self.controller.get_tournament_by_id(self.tournament_id)

class DeleteTournamentCommand(Command):
    def __init__(self, controller, tournament_id):
        self.controller = controller
        self.tournament_id = tournament_id

    def execute(self):
        self.controller.delete_tournament(self.tournament_id)

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
            name = input("Enter player name: ")
            age = int(input("Enter player age: "))
            command = CreatePlayerCommand(self.player_controller, name, age)
        elif choice == "2":
            command = GetAllPlayersCommand(self.player_controller)
        elif choice == "3":
            player_id = int(input("Enter player ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            command = UpdatePlayerCommand(self.player_controller, player_id, name, age)
        elif choice == "4":
            player_id = int(input("Enter player ID: "))
            command = GetPlayerByIdCommand(self.player_controller, player_id)
        elif choice == "5":
            player_id = int(input("Enter player ID to delete: "))
            command = DeletePlayerCommand(self.player_controller, player_id)
        elif choice == "6":
            name = input("Enter tournament name: ")
            date = input("Enter tournament date (YYYY-MM-DD): ")
            command = CreateTournamentCommand(self.tournament_controller, name, date)
            self.tournament_loaded = True  # Tournament is loaded after creation
        elif choice == "7":
            command = GetAllTournamentsCommand(self.tournament_controller)
            self.tournament_loaded = True  # Tournament is loaded after retrieval
        elif choice == "8" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID to update: "))
            name = input("Enter new name: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            command = UpdateTournamentCommand(self.tournament_controller, tournament_id, name, date)
        elif choice == "9" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID: "))
            command = GetTournamentByIdCommand(self.tournament_controller, tournament_id)
        elif choice == "10" and self.tournament_loaded:
            tournament_id = int(input("Enter tournament ID to delete: "))
            command = DeleteTournamentCommand(self.tournament_controller, tournament_id)
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
    tournament_controller = TournamentController(TournamentRepository(), TournamentView())

    # Initialisation du contrôleur de menu
    menu_view = MenuView()
    menu_controller = MenuController(menu_view, player_controller, tournament_controller)

    while True:
        menu_view.display_menu(menu_controller.tournament_loaded)
        choice = menu_view.get_user_choice()
        command = menu_controller.execute_choice(choice)

        if command is None:
            break

        command.execute()

if __name__ == "__main__":
    main()
