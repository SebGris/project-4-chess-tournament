from commands.tournament_commands import (
    AddDescriptionCommand, AddPlayersCommand, DisplayPlayersCommand,
    DisplayPlayersNamesCommand, DisplayRoundCommand, DisplayTournamentCommand,
    LoadAllPlayersCommand, LoadTournamentCommand, NewTournamentCommand,
    SaveTournamentCommand, UpdateNumberOfRoundsCommand
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
        if self.view.get_user_confirmation(
            "Voulez-vous ajouter des joueurs ?"
        ):
            self.add_players()

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
            self.view.display_message(
                "Le tournoi ne peut pas commencer sans joueurs."
            )
            return
        if len(self.tournament.players) % 2 != 0:
            self.view.display_message(
                "Le nombre de joueurs doit être pair "
                "pour commencer le tournoi."
            )
            return
        self.__add_round()
        self.tournament.current_round += 1
        message = self.__get_pairs_message(self.tournament.current_round)
        self.view.display_message(message)

    # Méthodes d'accès
    # Méthodes d'affichage
    def display_tournament(self):
        command = DisplayTournamentCommand(self.tournament, self.view)
        command.execute()
        command = DisplayPlayersNamesCommand(self.tournament, self.view)
        command.execute()
        command = DisplayRoundCommand(self.tournament, self.view)
        message = command.execute()
        rounds_data = '\n'.join(
            self.__get_pairs_message(i + 1)
            for i in range(len(self.tournament.rounds))
         )
        self.view.display_message(message + rounds_data)

    def display_players(self):
        command = DisplayPlayersCommand(self.tournament, self.view)
        command.execute()

    def record_results(self, round_instance):
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
        save_command = SaveTournamentCommand(self.tournament)
        save_message = save_command.execute()
        self.view.display_message(f"{round_name} ajouté et {save_message}")

    def __get_pairs_message(self, round_number):
        if round_number > len(self.tournament.rounds) or round_number < 1:
            return "Numéro de round invalide."
        current_round = self.tournament.rounds[round_number - 1]
        pairs = [
            (match.player1.full_name, match.player2.full_name)
            for match in current_round.matches
        ]
        pairs_message = "\n".join(
            [f"{pair[0]} vs {pair[1]}" for pair in pairs]
        )
        return (
            f"{current_round.name} avec les paires suivantes:\n"
            f"{pairs_message}"
        )

    def __execute_command(self, command_class, *args):
        command = command_class(self.tournament, *args)
        message = command.execute()
        self.view.display_message(message)
