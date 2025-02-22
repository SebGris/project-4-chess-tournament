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


class DisplayTournamentCommand(Command):
    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        return (
            f"Tournoi : {self.tournament.name}\n"
            f"Lieu : {self.tournament.location}\n"
            f"Date : du {self.tournament.start_date} au "
            f"{self.tournament.end_date}\n"
            f"Joueurs : {', '.join(self.tournament.players)}\n"
            f"Description : {self.tournament.description}"
        )


class NewTournamentCommand(Command):
    def __init__(self, tournament, menu, view, save_path=None):
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.save_path = save_path

    def execute(self):
        name = self.view.get_tournament_name()
        location = self.view.get_tournament_location()
        start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()
        players = self.view.get_tournament_players()
        self.tournament.set_tournament(
            name, location, start_date, end_date, players
        )
        self.menu.set_tournament_loaded(True)
        if self.save_path is None:
            self.save_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(self.tournament, self.save_path)
        save_message = save_command.execute()
        return f"Nouveau tournoi {name} créé et {save_message}"


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
            players = data.get('players', [])
            description = data.get('description')
            self.tournament.set_tournament(
                name, location, start_date, end_date, players, description
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
    def __init__(self, tournament, view, save_path=None):
        self.tournament = tournament
        self.view = view
        self.save_path = save_path

    def execute(self):
        description = self.view.get_tournament_description()
        self.tournament.set_description(description)
        if self.save_path is None:
            self.save_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(self.tournament, self.save_path)
        save_message = save_command.execute()
        return f"Description ajoutée: {description} et {save_message}"


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
