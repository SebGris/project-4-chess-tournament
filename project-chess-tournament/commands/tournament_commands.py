from commands.command import Command
from utils.file_utils import get_file_path
from utils.json_file_manager import JsonFileManager


class TournamentCommand(Command):
    def __init__(self, tournament, view=None, menu=None):
        self.tournament = tournament
        self.view = view
        self.menu = menu
        self.tournaments_file_path = get_file_path("tournaments.json")
        self.players_file_path = get_file_path("players.json")

    def save_tournament(self):
        data = self.tournament.to_dict()
        JsonFileManager.write(self.tournaments_file_path, data)
        return f"Tournoi {self.tournament.name} sauvegardé."


class LoadTournamentCommand(TournamentCommand):
    def __init__(self, tournament, all_players, menu):
        super().__init__(tournament, menu=menu)
        self.all_players = all_players

    def execute(self):
        try:
            data = JsonFileManager.read(self.tournaments_file_path)
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


class LoadAllPlayersCommand(TournamentCommand):
    def execute(self):
        try:
            if self.players_file_path is None:
                self.players_file_path = self.view.get_players_file_path()
            players_data = JsonFileManager.read(self.players_file_path)
            return players_data
        except ValueError as e:
            return str(e)


class SaveTournamentCommand(TournamentCommand):
    def execute(self):
        try:
            return self.save_tournament()
        except ValueError as e:
            return str(e)


class NewTournamentCommand(TournamentCommand):
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
        if self.tournaments_file_path is None:
            self.tournaments_file_path = self.view.get_tournaments_file_path()
        save_message = self.save_tournament()
        return f"Nouveau tournoi {name} créé et {save_message}"


class AddDescriptionCommand(TournamentCommand):
    def execute(self):
        description = self.view.get_tournament_description()
        self.tournament.set_description(description)
        if self.tournaments_file_path is None:
            self.tournaments_file_path = self.view.get_tournaments_file_path()
        save_message = self.save_tournament()
        return f"Description ajoutée: {description} et {save_message}"


class AddPlayersCommand(TournamentCommand):
    def __init__(self, tournament, players):
        super().__init__(tournament)
        self.players = players

    def execute(self):
        for player in self.players:
            self.tournament.add_player(player)
        if self.tournaments_file_path is None:
            self.tournaments_file_path = self.view.get_tournaments_file_path()
        save_message = self.save_tournament()
        if self.players_file_path is None:
            self.players_file_path = self.view.get_players_file_path()
        existing_players = JsonFileManager.read(self.players_file_path)
        updated_players = existing_players + [
            player.to_dict() for player in self.players
        ]
        JsonFileManager.write(self.players_file_path, updated_players)
        return f"Joueurs ajoutés et {save_message}"


class UpdateNumberOfRoundsCommand(TournamentCommand):
    def execute(self):
        number_of_rounds = self.view.get_tournament_number_of_rounds()
        self.tournament.set_number_of_rounds(number_of_rounds)
        if self.tournaments_file_path is None:
            self.tournaments_file_path = self.view.get_tournaments_file_path()
        save_message = self.save_tournament()
        return (
            f"Nombre de tours mis à jour à {number_of_rounds} "
            f"et {save_message}"
        )


class DisplayCommand(Command):
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view


class DisplayRoundCommand(DisplayCommand):
    def execute(self):
        return (
            f"Tour actuel : {self.tournament.current_round}/"
            f"{self.tournament.number_of_rounds}\n"
        )


class DisplayPlayersCommand(DisplayCommand):
    def execute(self):
        # Transforms Player objects into displayable data for the View.
        players_data = []
        for player in self.tournament.players:
            players_data.append({
                "full_name": player.full_name,
                "birth_date": player.birth_date.strftime("%d/%m/%Y"),
                "id_chess": player.id_chess
            })
        self.view.display_players(players_data)


class DisplayPlayersNamesCommand(DisplayCommand):
    def execute(self):
        players_names = [
            player.full_name for player in self.tournament.players
        ]
        self.view.display_players_full_names(players_names)


class DisplayTournamentCommand(DisplayCommand):
    def execute(self):
        tournament = {
            "name": self.tournament.name,
            "location": self.tournament.location,
            "start_date": self.tournament.start_date,
            "end_date": self.tournament.end_date,
            "description": self.tournament.description,
            "number_of_rounds": self.tournament.number_of_rounds
        }
        self.view.display_tournament(tournament)
