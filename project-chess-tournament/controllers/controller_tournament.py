from commands.command import (
    AddDescriptionCommand, DisplayTournamentCommand,
    LoadTournamentCommand,
    NewTournamentCommand,
    SaveTournamentCommand
)
from controllers.base_controller import BaseController
from models.player import Player
from models.round import Round
from models.tournament import Tournament


class ControllerTournament(BaseController):
    def __init__(self, tournament, menu, view):
        super().__init__()  # Appel au constructeur de BaseController
        self.tournament = tournament
        self.menu = menu
        self.view = view
        self.previous_matches = []

    def new_tournament(self):
        command = NewTournamentCommand(self.tournament, self.menu, self.view)
        message = command.execute()
        self.view.display_message(message)

    def add_players(self, players=None):
        """Adding players to the tournament"""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
        elif players is not None:
            for player in players:
                self.tournament.add_player(player)
            self.save_tournament(save_with_players=True)
        else:
            while True:
                choice = self.view.get_add_player()
                if choice == 'o':
                    self.__add_player()
                else:
                    break
            self.save_tournament(save_with_players=True)

    def __add_player(self):
        """
        Adds a player to the tournament by requesting information via the view.
        """
        player_details = self.view.get_player()
        if not player_details["first_name"]:
            # Si l'utilisateur valide sans entrer de nom
            self.view.display_message("Ajout annulé.")
        else:
            player = Player(
                player_details["last_name"],
                player_details["first_name"],
                player_details["birth_date"],
                player_details["id_chess"]
                )
            self.tournament.add_player(player)
            self.view.display_message(
                f"Joueur {player.get_full_name()} ajouté avec succès !"
                )

    def start_tournament(self):
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
            player1_name = match.player1[0].get_full_name()
            player2_name = match.player2[0].get_full_name()
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

    def add_description(self):
        command = AddDescriptionCommand(self.tournament, self.view)
        message = command.execute()
        self.view.display_message(message)

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

    def display_tournament(self):
        command = DisplayTournamentCommand(self.tournament)
        message = command.execute()
        self.view.display_message(message)

    def save_tournament(self):
        """Save tournament to a JSON file."""
        file_path = self.view.get_tournament_file_path()
        command = SaveTournamentCommand(self.tournament, file_path)
        message = command.execute()
        self.view.display_message(message)

    def load_tournament(self):
        """Load tournament from a JSON file."""
        # file_path = self.view.get_tournament_file_path()
        file_path = self.tournament_file_path
        command = LoadTournamentCommand(self.tournament, self.menu, file_path)
        message = command.execute()
        self.view.display_message(message)

    def add_new_tournament_test(self, players=None):
        """Tournament variable for testing"""
        players = players or []
        self.tournament = Tournament(
            "Championnat de Paris", "Paris", "01/06/2025", "07/06/2025",
            players=players
        )
        self.view.display_message("Tournoi ajouté avec succès !")
