from commands.command import (
    AddDescriptionCommand, AddPlayersCommand,
    DisplayTournamentCommand, EndRoundCommand, LoadAllPlayersCommand,
    LoadTournamentCommand, NewTournamentCommand, SaveTournamentCommand,
    StartTournamentCommand, UpdateNumberOfRoundsCommand
)
from controllers.base_controller import BaseController
from controllers.pairing import Pairing
from models.player import Player
from models.round import Round
from models.tournament import Tournament


class ControllerTournament(BaseController):
    def __init__(self, tournament, menu, view):
        super().__init__()  # Appel au constructeur de BaseController
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.all_players = self.load_all_players()
        self.previous_matches = []

    def load_all_players(self):
        command = LoadAllPlayersCommand(self.players_file_path)
        players_data = command.execute()
        all_players = {
            player_data['id']: Player(**player_data)
            for player_data in players_data
        }
        return all_players

    def start_tournament_old(self):
        """Starts a tournament and manages the rounds."""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
        elif (len(self.tournament.players) % 2) != 0:
            self.view.display_message(
                "Le nombre de joueurs doit être pair."
                )
        else:
            while not self.tournament.is_complete():
                round_instance = Round(
                    self.tournament.current_round,
                    self.tournament.players,
                    self.previous_matches
                )
                self.__record_results(round_instance)
                round_instance.end_round()
                for match in round_instance.matches:
                    print(match)
                self.previous_matches.extend(
                    round_instance.get_played_matches()
                )
                self.tournament.rounds.append(round_instance)
                self.tournament.current_round += 1
            self.save_tournament(save_with_players=True)
            self.view.display_result(self.tournament.players)

    def __record_results(self, round_instance):
        """Records the results of matches in the current round."""
        print(f"\nEnregistrement des résultats du {round_instance.name}:")
        for match in round_instance.matches:
            player1_name = match.player1[0].full_name()
            player2_name = match.player2[0].full_name()
            print(f"\n{player1_name} vs {player2_name}")
            result = self.view.get_match_result()
            if result == "1":
                match.set_score(1, 0)
                match.player1[0].update_score(1)
            elif result == "2":
                match.set_score(0, 1)
                match.player2[0].update_score(1)
            elif result == "0":
                match.set_score(0.5, 0.5)
                match.player1[0].update_score(0.5)
                match.player2[0].update_score(0.5)

    def display_description(self):
        """Displays the description of the tournament."""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        self.view.display_description(self.tournament)

    def display_tournament_result(self):
        """Affiche les résultats du tournoi."""
        self.view.show_message("Résultats du tournoi :")
        self.tournament.display_result()

    def display_tournament_players(self):
        """Displays the list of players registered for the tournament."""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        self.view.display_players(self.tournament.players)

    def add_new_tournament_test(self, players=None):
        """Tournament variable for testing"""
        players = players or []
        self.tournament = Tournament(
            "Championnat de Paris", "Paris", "01/06/2025", "07/06/2025",
            players=players
        )
        self.view.display_message("Tournoi ajouté avec succès !")

    def load_tournament(self):
        # file_path = self.view.get_tournament_file_path()
        file_path = self.tournament_file_path
        command = LoadTournamentCommand(
            self.tournament, self.menu, file_path, self.all_players
        )
        message = command.execute()
        self.view.display_message(message)

    def save_tournament(self):
        file_path = self.view.get_tournament_file_path()
        command = SaveTournamentCommand(self.tournament, file_path)
        message = command.execute()
        self.view.display_message(message)

    def display_tournament(self):
        command = DisplayTournamentCommand(self.tournament)
        message = command.execute()
        self.view.display_message(message)

    def new_tournament(self):
        command = NewTournamentCommand(
            self.tournament, self.menu, self.view, self.tournament_file_path
        )
        response = command.execute()
        self.view.display_message(response)
        if response.lower() == 'oui':
            self.add_players()

    def add_description(self):
        command = AddDescriptionCommand(
            self.tournament, self.view, self.tournament_file_path
        )
        message = command.execute()
        self.view.display_message(message)

    def add_players(self):
        players = []
        while True:
            player_data = self.view.get_player_data()
            if player_data:
                player = Player(**player_data)
                players.append(player)
                self.view.display_message(f"Joueur {player.full_name} ajouté.")
            else:
                break
        command = AddPlayersCommand(
            self.tournament, players, self.tournament_file_path,
            self.players_file_path
        )
        message = command.execute()
        self.view.display_message(message)

    def start_tournament(self):
        command = StartTournamentCommand(self.tournament)
        message = command.execute()
        self.view.display_message(message)

    def update_number_of_rounds(self):
        command = UpdateNumberOfRoundsCommand(
            self.tournament, self.view, self.tournament_file_path
        )
        message = command.execute()
        self.view.display_message(message)

    def add_round(self):
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
        save_path = self.view.get_tournament_file_path()
        save_command = SaveTournamentCommand(self.tournament, save_path)
        save_message = save_command.execute()
        self.view.display_message(f"{round_name} ajouté et {save_message}")

    def end_round(self):
        command = EndRoundCommand(self.tournament, self.view)
        message = command.execute()
        self.view.display_message(message)
