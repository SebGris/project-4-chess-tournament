from utils.json_file_manager import JsonFileManager
from commands.base_command import Command


class ChangeMenuCommand:
    def __init__(self, menu_controller, menu_name, menu_title):
        self.menu_controller = menu_controller
        self.menu_name = menu_name
        self.menu_title = menu_title

    def execute(self):
        self.menu_controller.display_menu(self.menu_name, self.menu_title)


class AddPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players()  # TODO Ajoute un seul joueur ?


class LoadPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.load_players_from_json()


class DisplayPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_players()


class NewTournamentCommand(Command):
    def __init__(self, tournament, menu, view):
        self.tournament = tournament
        self.menu = menu
        self.view = view

    def execute(self):
        name = self.view.get_tournament_name()
        location = self.view.get_tournament_location()
        start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()
        players = self.view.get_tournament_players()
        print(players)
        self.tournament.set_tournament(
            name, location, start_date, end_date, players
        )
        self.menu.set_tournament_loaded(True)
        return f"Nouveau tournoi {name} créé."


class AddPlayersToTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players()


class LoadTournamentCommand(Command):
    def __init__(self, tournament, menu, file_path):
        self.tournament = tournament
        self.menu = menu
        self.file_path = file_path

    def execute(self):
        try:
            data = JsonFileManager.read(self.file_path)
            name = data.get('name')
            location = data.get('location')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            description = data.get('description')
            players = data.get('players', [])
            self.tournament.set_tournament(
                name, location, start_date, end_date, description, players
            )
            self.menu.set_tournament_loaded(True)
            return f"Tournoi {name} chargé."
        except ValueError as e:
            return str(e)


class SaveTournamentCommand(Command):
    def __init__(self, tournament, file_path):
        self.tournament = tournament
        self.file_path = file_path

    def execute(self):
        try:
            data = self.tournament.to_dict()
            JsonFileManager.write(self.file_path, data)
            return f"Tournoi {self.tournament.name} sauvegardé."
        except ValueError as e:
            return str(e)


class StartTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.start_tournament()


class DisplayTournamentsCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_tournaments()  # TODO Affiche les tournois


class AddDescriptionCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_description()


class DisplayDescriptionCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_description()


class DisplayTournamentPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_tournament_players()


class DisplayTournamentResultCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_tournament_result()


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
