from utils.json_file_manager import JsonFileManager
from datetime import datetime


class Command:
    """Base class for all commands."""
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class LoadTournamentCommand(Command):
    def __init__(self, tournament, menu, tournament_file_path, all_players):
        self.tournament = tournament
        self.menu = menu
        self.tournament_file_path = tournament_file_path
        self.all_players = all_players

    def execute(self):
        try:
            data = JsonFileManager.read(self.tournament_file_path)
            name = data.get('name')
            location = data.get('location')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            player_ids = data.get('players', [])
            description = data.get('description')
            rounds = data.get('rounds', [])
            number_of_rounds = data.get('number_of_rounds', 4)
            players = [self.all_players[player_id] for player_id in player_ids]
            self.tournament.set_tournament(
                name, location, start_date, end_date, number_of_rounds,
                players, description, rounds
            )
            self.menu.set_tournament_loaded(True)
            return f"Tournoi {name} chargé."
        except ValueError as e:
            return str(e)


class SaveTournamentCommand(Command):
    def __init__(self, tournament, tournament_file_path):
        self.tournament = tournament
        self.tournament_file_path = tournament_file_path

    def execute(self):
        try:
            data = self.tournament.to_dict()
            JsonFileManager.write(self.tournament_file_path, data)
            return f"Tournoi {self.tournament.name} sauvegardé."
        except ValueError as e:
            return str(e)


class DisplayTournamentCommand(Command):
    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        players_data = ', '.join(
            player.full_name for player in self.tournament.players
        )
        return (
            f"Tournoi : {self.tournament.name} | Lieu : "
            f"{self.tournament.location}\n"
            f"Date : du {self.tournament.start_date} au "
            f"{self.tournament.end_date}\n"
            f"Joueurs : {players_data}\n"
            f"Nombre de joueurs : {len(self.tournament.players)}\n"
            f"Description : {self.tournament.description}\n"
            f"Nombre de tours: {self.tournament.number_of_rounds}\n"
            f"Tour actuel : {self.tournament.current_round}/"
            f"{self.tournament.number_of_rounds}\n"
            # f"Rounds:\n{rounds_data}"
        )


class NewTournamentCommand(Command):
    def __init__(self, tournament, menu, view, tournament_file_path=None):
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.tournament_file_path = tournament_file_path

    def execute(self):
        name = self.view.get_tournament_name()
        location = self.view.get_tournament_location()
        start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()
        number_of_rounds = 4
        self.tournament.set_tournament(
            name, location, start_date, end_date, number_of_rounds,
            [], None, [],
        )
        self.menu.set_tournament_loaded(True)
        if self.tournament_file_path is None:
            self.tournament_file_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(
            self.tournament, self.tournament_file_path)
        save_message = save_command.execute()
        self.view.display_message(
            f"Nouveau tournoi {name} créé et {save_message}"
        )
        return self.view.ask_to_add_players()


class AddDescriptionCommand(Command):
    def __init__(self, tournament, view, tournament_file_path=None):
        self.tournament = tournament
        self.view = view
        self.tournament_file_path = tournament_file_path

    def execute(self):
        description = self.view.get_tournament_description()
        self.tournament.set_description(description)
        if self.tournament_file_path is None:
            self.tournament_file_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(
            self.tournament, self.tournament_file_path)
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
            self.tournament.add_player(player)
        if self.tournament_file_path is None:
            self.tournament_file_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(
            self.tournament, self.tournament_file_path)
        save_message = save_command.execute()
        if self.players_file_path is None:
            self.players_file_path = self.view.get_players_file_path()
        existing_players = JsonFileManager.read(self.players_file_path)
        updated_players = existing_players + [
            player.to_dict() for player in self.players
        ]
        JsonFileManager.write(self.players_file_path, updated_players)
        return f"Joueurs ajoutés et {save_message}"


class UpdateNumberOfRoundsCommand(Command):
    def __init__(self, tournament, view, tournament_file_path=None):
        self.tournament = tournament
        self.view = view
        self.tournament_file_path = tournament_file_path

    def execute(self):
        number_of_rounds = self.view.get_tournament_number_of_rounds()
        self.tournament.set_number_of_rounds(number_of_rounds)
        if self.tournament_file_path is None:
            self.tournament_file_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(
            self.tournament, self.tournament_file_path)
        save_message = save_command.execute()
        return (
            f"Nombre de tours mis à jour à {number_of_rounds} "
            f"et {save_message}"
        )


class EndRoundCommand(Command):
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view

    def execute(self):
        if not self.tournament.rounds:
            return "Aucun tour en cours."
        current_round = self.tournament.rounds[-1]
        current_round["end_datetime"] = datetime.now().isoformat()
        save_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(self.tournament, save_path)
        save_message = save_command.execute()
        return f"{current_round['name']} terminé et {save_message}"


class LoadAllPlayersCommand(Command):
    def __init__(self, players_file_path):
        self.players_file_path = players_file_path

    def execute(self):
        try:
            if self.players_file_path is None:
                self.players_file_path = self.view.get_players_file_path()
            players_data = JsonFileManager.read(self.players_file_path)
            return players_data
        except ValueError as e:
            return str(e)


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
