from models.player import Player
from models.round import Round
from models.tournament import Tournament
from utils.file_utils import save_to_json, load_from_json


class ControllerTournament:
    """Manages the logic of the tournament."""
    TOURNAMENT_FILENAME = "tournament.json"

    def __init__(self, view):
        self.view = view
        self.tournament = None
        self.previous_matches = []

    def entering_a_tournament(self, tournament=None):
        """
        Manages the entry to a tournament.
        - If a tournament is supplied, it is used directly.
        - If not, the user is invited to create one.
        """
        if tournament is None:
            data = self.view.prompt_for_tournament()
            tournament = Tournament(*data)
        self.tournament = tournament
        self.view.display_message("Tournoi ajouté avec succès !")

    def tournament_exists(self):
        """
        Checks whether a tournament is currently defined in the controller.
        :return: True if a tournament exists, otherwise False.
        """
        return self.tournament is not None

    def add_players(self):
        """Adding players to the tournament"""
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        while True:
            choice = self.view.prompt_for_add_player()
            if choice == 'o':
                self.add_player()
            else:
                break

    def add_player(self, player=None):
        """
        Adds a player to the tournament by requesting information via the view.
        """
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        if player is None:
            player_details = self.view.prompt_for_player()
            if not player_details["first_name"]:
                # Si l'utilisateur valide sans entrer de nom
                self.view.display_message("Ajout annulé.")
                return
            player = Player(
                player_details["last_name"],
                player_details["first_name"],
                player_details["birth_date"],
                player_details["id_chess"],
                id=player_details.get("id")
                )
        self.tournament.add_player(player)
        self.save_players_to_json()
        self.view.display_message(
            f"Joueur {player.get_full_name()} ajouté avec succès !"
            )

    def start_tournament(self):
        """Starts a tournament and manages the rounds."""
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        if (len(self.tournament.players) % 2) != 0:
            self.view.display_message(
                "Le nombre de joueurs doit être pair."
                )
            return
        while not self.tournament.is_complete():
            round_instance = Round(
                self.tournament.current_round,
                self.tournament.players,
                self.previous_matches
            )
            self.record_results(round_instance)
            round_instance.end_round()
            for match in round_instance.matches:
                print(match)
            self.previous_matches.extend(round_instance.get_played_matches())
            self.tournament.current_round += 1
        self.view.display_result(self.tournament.players)

    def record_results(self, round_instance):
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
            # Save the tournament state after each match result is recorded
            self.save_tournament_to_json()

    def add_description(self):
        """Add a description to the tournament."""
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        description = self.view.prompt_for_description()
        self.tournament.set_description(description)

    def show_results(self):
        """Affiche les résultats du tournoi."""
        self.view.show_message("Résultats du tournoi :")
        self.tournament.show_results()

    def display_players(self):
        """Displays the list of players registered for the tournament."""
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        self.view.display_players(self.tournament.players)

    def display_tournament(self):
        """Displays the tournament."""
        if not self.tournament_exists():
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        self.view.display_tournament(self.tournament)
        self.view.display_tournament_players(self.tournament)

    def save_players_to_json(self):
        """Save players to a JSON file."""
        save_to_json(
            [player.to_dict() for player in self.tournament.players],
            "players.json"
        )

    def save_tournament_to_json(self, save_players=False):
        """Save tournament to a JSON file."""
        save_to_json(self.tournament.to_dict(), self.TOURNAMENT_FILENAME)
        if save_players:
            self.save_players_to_json()

    def load_tournament_from_json(self):
        """Load tournament from a JSON file."""
        data = load_from_json(self.TOURNAMENT_FILENAME)
        all_players = {player.id: player for player in self.load_all_players()}
        self.tournament = Tournament.from_dict(data, all_players)
        self.view.display_message("Tournoi chargé avec succès !")

    def load_all_players(self):
        """Load all players from a JSON file."""
        data = load_from_json("players.json")
        return [Player.from_dict(player_data) for player_data in data]
