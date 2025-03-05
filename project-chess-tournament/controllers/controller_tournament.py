# Imports de modules locaux
from models.player import Player
from commands.tournament_commands import (
    AddDescriptionCommand, DisplayCurrentRound,
    DisplayCurrentRoundNoCommand, DisplayPlayerPairsCommand,
    DisplayPlayersCommand, DisplayTournamentDetailsCommand,
    DisplayTournamentPlayersCommand, LoadAllPlayersCommand,
    LoadTournamentCommand, NewTournamentCommand, RecordResultsCommand,
    UpdateNumberOfRoundsCommand
)
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController


class ControllerTournament():
    """Ne respecte pas le principe de responsabilité unique.
    La classe `ControllerTournament` gère la logique de l'application."""
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

    def load_tournament(self):
        self.__execute_command(
            LoadTournamentCommand, self.all_players, self.menu
        )

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
            if current_round is None:
                self.round_controller.add_round()
            elif current_round.is_finished():
                self.round_controller.add_round()
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
        command = LoadAllPlayersCommand(self.tournament)
        players_data = command.execute()
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
