from models.player import Player
from models.round import Round
from models.tournament import Tournament
from controllers.base_controller import Controller
from commands.file_commands import ReadJsonFileCommand, WriteJsonFileCommand


class ControllerTournament(Controller):
    """Manages the logic of the tournament."""

    def __init__(self, view):
        self.view = view
        self.tournament = None
        self.previous_matches = []

    def new_tournament(self, tournament=None):
        """
        Manages the entry to a tournament.
        - If a tournament is supplied, it is used directly.
        - If not, the user is invited to create one.
        """
        if tournament is None:
            data = self.view.prompt_for_tournament()
            tournament = Tournament(*data)
        self.tournament = tournament
        self.save_tournament_to_json()
        self.view.display_message("Tournoi ajouté avec succès !")

    def add_players(self, players=None):
        """Adding players to the tournament"""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
        elif players is not None:
            for player in players:
                self.tournament.add_player(player)
            self.save_tournament_to_json(save_with_players=True)
        else:
            while True:
                choice = self.view.prompt_for_add_player()
                if choice == 'o':
                    self.__add_player()
                else:
                    break
            self.save_tournament_to_json(save_with_players=True)

    def __add_player(self):
        """
        Adds a player to the tournament by requesting information via the view.
        """
        player_details = self.view.prompt_for_player()
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
                self.previous_matches.extend(round_instance.get_played_matches())
                self.tournament.rounds.append(round_instance)
                self.tournament.current_round += 1
            self.save_tournament_to_json(save_with_players=True)
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
        """Add a description to the tournament."""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        description = self.view.prompt_for_description()
        self.tournament.set_description(description)

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
        """Displays the tournament."""
        if self.tournament is None:
            self.view.display_message(
                "Aucun tournoi en cours. Créez un tournoi d'abord."
                )
            return
        self.view.display_description(self.tournament)
        self.view.display_tournament_players(self.tournament)

    def save_players_to_json(self):
        """Save players to a JSON file."""
        write_command = WriteJsonFileCommand(
            self.players_file_path,
            [player.to_dict() for player in self.tournament.players]
        )
        write_command.execute()

    def save_tournament_to_json(self, save_with_players=False):
        """Save tournament to a JSON file."""
        tournament_data = self.tournament.to_dict()
        tournament_data['rounds'] = [
            round_instance.to_dict() for round_instance in self.tournament.rounds
        ]
        write_command = WriteJsonFileCommand(
            self.tournament_file_path, tournament_data)
        write_command.execute()
        if save_with_players:
            self.save_players_to_json()

    def load_tournament_from_json(self):
        """Load tournament from a JSON file."""
        read_command = ReadJsonFileCommand(self.tournament_file_path)
        data = read_command.execute()
        all_players = {player.id: player for player in self.load_all_players()}
        self.tournament = Tournament.from_dict(data, all_players)
        self.view.display_message("Tournoi chargé avec succès !")

    def load_all_players(self):
        """Load all players from a JSON file."""
        read_command = ReadJsonFileCommand(self.players_file_path)
        data = read_command.execute()
        return [Player.from_dict(player_data) for player_data in data]

    def add_new_tournament_test(self, players=None):
        """Tournament variable for testing"""
        players = players or []
        self.tournament = Tournament(
            "Championnat de Paris", "Paris", "01/06/2025", "07/06/2025",
            players=players
        )
        self.view.display_message("Tournoi ajouté avec succès !")
