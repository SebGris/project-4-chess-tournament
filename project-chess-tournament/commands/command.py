from utils.json_file_manager import JsonFileManager
from commands.base_command import Command


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
            rounds = data.get('rounds', [])
            self.tournament.set_tournament(
                name, location, start_date, end_date, players,
                description, rounds
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


class DisplayTournamentCommand(Command):
    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        players_data = ', '.join(player for player in self.tournament.players)
        rounds_data = ', '.join(round.name for round in self.tournament.rounds)
        return (
            f"Tournoi : {self.tournament.name}\n"
            f"Lieu : {self.tournament.location}\n"
            f"Date : du {self.tournament.start_date} au "
            f"{self.tournament.end_date}\n"
            f"Joueurs : {players_data}\n"
            f"Description : {self.tournament.description}\n"
            f"Rounds: {rounds_data}"
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
        self.tournament.set_tournament(
            name, location, start_date, end_date, [], None, []
        )
        self.menu.set_tournament_loaded(True)
        if self.save_path is None:
            self.save_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(self.tournament, self.save_path)
        save_message = save_command.execute()
        self.view.display_message(
            f"Nouveau tournoi {name} créé et {save_message}"
        )
        return self.view.ask_to_add_players()


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


class AddPlayersCommand(Command):
    def __init__(self, tournament, players, tournament_file_path=None,
                 players_file_path=None):
        self.tournament = tournament
        self.players = players
        self.tournament_file_path = tournament_file_path
        self.players_file_path = players_file_path

    def execute(self):
        for player in self.players:
            self.tournament.add_player(player['id'])
        if self.tournament_file_path is None:
            self.tournament_file_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(
            self.tournament, self.tournament_file_path)
        save_message = save_command.execute()
        if self.players_file_path is None:
            self.players_file_path = self.view.get_players_file_path()
        existing_players = JsonFileManager.read(self.players_file_path)
        updated_players = existing_players + self.players
        JsonFileManager.write(self.players_file_path, updated_players)
        return f"Joueurs ajoutés et {save_message}"


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
