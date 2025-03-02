from commands.tournament_commands import (
    AddDescriptionCommand, AddPlayersCommand, DisplayCurrentRound,
    DisplayCurrentRoundNoCommand, DisplayPlayerPairsCommand,
    DisplayPlayersCommand, DisplayPlayersNamesCommand,
    DisplayTournamentCommand, LoadAllPlayersCommand, LoadTournamentCommand,
    NewTournamentCommand, RecordResultsCommand, SaveTournamentCommand,
    UpdateNumberOfRoundsCommand
)
from controllers.pairing import Pairing
from models.player import Player
from models.round import Round


class ControllerTournament():
    def __init__(self, tournament, menu, view):
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.all_players = self.__load_all_players()
        self.previous_matches = []

    # Méthodes de gestion de l'état
    def new_tournament(self):
        self.__execute_command(NewTournamentCommand, self.view, self.menu)
        if self.view.request_player_addition_confirmation():
            self.add_players()

    def add_players(self):
        players = []
        while True:
            player_data = self.view.get_player_data()
            if player_data:
                player = Player(**player_data)
                players.append(player)
                self.view.display_add_player_message(player.full_name)
            else:
                break
        self.__execute_command(AddPlayersCommand, players)

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
        self.__add_round()
        self.__execute_display_commands(DisplayPlayerPairsCommand)

    def record_results(self):
        self.__execute_command(RecordResultsCommand, self.view)
        self.__save_tournament()

    # Méthodes d'accès
    # Méthodes d'affichage
    def display_tournament(self):
        self.__execute_display_commands(
            DisplayTournamentCommand,
            DisplayPlayersNamesCommand,
            DisplayCurrentRound,
            DisplayCurrentRoundNoCommand,
            DisplayPlayerPairsCommand
        )

    def display_players(self):
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

    def __add_round(self):
        round_name = f"Round {len(self.tournament.rounds) + 1}"
        new_round = Round(round_name)
        previous_matches = {
            (match.player1.id, match.player2.id)
            for round in self.tournament.rounds
            for match in round.matches
        }
        if len(self.tournament.rounds) == 0:
            pairs = Pairing.generate_first_round_pairs(self.tournament.players)
        else:
            pairs = Pairing.generate_next_round_pairs(
                self.tournament.players, previous_matches)
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.tournament.rounds.append(new_round)
        self.__save_tournament()
        self.view.display_message(f"{round_name} ajouté")

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

    def __save_tournament(self):
        save_command = SaveTournamentCommand(self.tournament)
        save_message = save_command.execute()
        self.view.display_message(save_message)
