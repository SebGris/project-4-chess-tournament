# Imports de modules locaux
from models.file_paths import players_file_path, tournaments_file_path
from models.json_file_receiver import JsonFileReceiver
from models.player import Player
from commands.json_commands import (FileOperation, ReadFileJsonCommand, WriteFileJsonCommand)
from commands.tournament_commands import (
    AddDescriptionCommand, DisplayCurrentRound,
    DisplayCurrentRoundNoCommand, DisplayPlayerPairsCommand,
    DisplayPlayersCommand, DisplayTournamentDetailsCommand,
    DisplayTournamentPlayersCommand,
    LoadTournamentCommand, NewTournamentCommand, RecordResultsCommand,
    UpdateNumberOfRoundsCommand
)
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController


class TournamentController():
    """Ne respecte pas le principe de responsabilité unique.
    La classe `ControllerTournament` gère la logique de l'application."""
    json_file_receiver_tournaments = JsonFileReceiver(tournaments_file_path())
    json_file_receiver_players = JsonFileReceiver(players_file_path())
    def __init__(self, tournament, menu, view):
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.player_controller = PlayerController(tournament, view)
        self.round_controller = RoundController(tournament, view)
        self.all_players = self.__load_all_players()
        self.previous_matches = []

    # Méthodes de gestion de l'état
    def new_tournament(self):
        self.__execute_command(NewTournamentCommand, self.view, self.menu)
        if self.view.request_player_addition_confirmation():
            self.player_controller.add_players()

    def add_description(self):
        self.__execute_command(AddDescriptionCommand, self.view)

    def update_number_of_rounds(self):
        self.__execute_command(UpdateNumberOfRoundsCommand, self.view)

    def save_tournament(self):
            command = WriteFileJsonCommand(self.json_file_receiver_tournaments, self.tournament.to_dict())
            file_operations = FileOperation(command)
            file_operations.execute_commands()
            return f"Tournoi {self.tournament.name} sauvegardé."

    def load_tournament(self):
        try:
            command = ReadFileJsonCommand(self.json_file_receiver_tournaments)
            file_operations = FileOperation(command)
            data = file_operations.execute_commands()
            name = data.get('name')
            location = data.get('location')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            player_ids = data.get('players', [])
            description = data.get('description')
            rounds = data.get('rounds', [])
            number_of_rounds = data.get('number_of_rounds', 4)
            players = [self.all_players[player_id] for player_id in player_ids]
            self.tournament.set_tournament(name, location, start_date, end_date, number_of_rounds, players, description, rounds)
            self.__execute_command(LoadTournamentCommand, self.menu)
        except Exception as e:
            self.view.display_message(f"Erreur lors du chargement du tournoi: {e}")

    # Méthodes d'action
    def start_tournament(self):
        if not self.tournament.players:
            self.view.display_tournament_start_error()
            return
        if self.__is_odd_number_of_players():
            self.view.display_even_players_message()
            return
        for round in self.tournament.rounds:
            self.tournament.update_scores(round.matches)
        print(self.tournament.players)
        if self.tournament.number_of_rounds > len(self.tournament.rounds):
            current_round = self.tournament.get_current_round()
            if (current_round is None):
                self.round_controller.add_round()
            elif current_round.is_finished():
                self.round_controller.add_round()
        save_message = self.save_tournament()
        self.view.display_message(save_message)
        self.__execute_display_commands(DisplayPlayerPairsCommand)

    def record_results(self):
        self.__execute_command(RecordResultsCommand, self.view)

    # Méthodes d'affichage
    def show_tournament_details(self):
        self.__execute_display_commands(
            DisplayTournamentDetailsCommand,
            DisplayTournamentPlayersCommand,
            DisplayCurrentRound,
            DisplayCurrentRoundNoCommand,
            DisplayPlayerPairsCommand
        )

    def show_players(self):
        self.__execute_display_commands(DisplayPlayersCommand)

    # Méthodes privées
    def __load_all_players(self):
        command = ReadFileJsonCommand(self.json_file_receiver_players)
        file_operations = FileOperation(command)
        players_data = file_operations.execute_commands()
        all_players = {
            player_data['id']: Player(**player_data)
            for player_data in players_data
        }
        return all_players

    def __execute_command(self, command_class, *args):
        command = command_class(self.tournament, *args)
        message = command.execute()
        self.view.display_message(message)

    def __execute_display_commands(self, *command_classes):
        for command_class in command_classes:
            command = command_class(self.tournament, self.view)
            command.execute()

    def __is_odd_number_of_players(self):
        return len(self.tournament.players) % 2 != 0
