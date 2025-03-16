from controllers.pairing import Pairing
from controllers.player_controller import PlayerController
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from repositories.player_repository import PlayerRepository
from repositories.tournament_repository import TournamentRepository
from views.player_view import PlayerView
from views.round_view import RoundView
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self, tournament_repository: TournamentRepository, view: TournamentView):
        self.tournament_repository = tournament_repository
        self.tournament_view = view
        self.round_view = RoundView()
        self.player_controller = PlayerController(PlayerRepository(), PlayerView())
        self.tournaments = self.tournament_repository.get_tournaments()
        self.active_tournament = None

    def get_active_tournament(self):
        return self.active_tournament

    def collect_tournament_info(self):
        return {
            "name": self.tournament_view.get_name(),
            "location": self.tournament_view.get_location(),
            "start_date": self.tournament_view.get_start_date(),
            "end_date": self.tournament_view.get_end_date(),
            "number_of_rounds": self.tournament_view.get_number_of_rounds(),
        }

    def create_new_tournament(self):
        tournament_info = self.collect_tournament_info()
        self.create_tournament(**tournament_info)
        self.tournament_view.display_tournament_created(tournament_info["name"])

    def create_tournament(self, name, location, start_date, end_date, number_of_rounds):
        tournament = Tournament(name, location, start_date, end_date, number_of_rounds)
        self.tournaments.append(tournament)
        self.tournament_repository.save_tournaments(self.tournaments)

    def select_tournament(self):
        index = self.tournament_view.get_tournament_selection(self.tournaments)
        self.active_tournament = self.tournaments[index]

    def load_all_players(self):
        try:
            all_players = {
                player_data["id"]: Player(**player_data)
                for player_data in self.load_players_data()
            }
            return all_players
        except FileNotFoundError as e:
            self.tournament_view.display_for_file_not_found(str(e))

    def add_players(self):
        while True:
            player_data = self.player_controller.get_player_data()
            if player_data:
                player_id = self.add_player(player_data)
                player_data["id"] = player_id
                full_name = f"{player_data['first_name']} {player_data['last_name']}"
                self.tournament_view.display_add_player_message(full_name)
                existing_players = self.controller.load_players_data()
                existing_players.append(player_data)
                self.controller.save_players_data(existing_players)
            else:
                break


    def add_player(self, player_data):
        player = Player(**player_data)
        self.active_tournament.players.append(player)
        return player.id

    def start_tournament(self):
        if self.__check_if_start():
            for index in range(1, self.active_tournament.number_of_rounds):
                self.active_tournament.update_scores(round.matches)
                print(self.active_tournament.players)
                # if self.active_tournament.number_of_rounds > len(self.active_tournament.rounds):
                current_round = self.active_tournament.get_current_round()
                if current_round is None:
                    self.add_round()
                elif current_round.is_finished():
                    self.add_round()

    def __check_if_start(self):
        if not self.active_tournament.players:
            self.tournament_view.display_start_error_without_players()
            return False
        elif self.__check_if_odd(len(self.active_tournament.players)):
            self.tournament_view.display_start_error_even_players()
            return False
        return True

    def __check_if_odd(self, number):
        return number % 2 != 0

    def add_round(self):
        round_name = f"Round {len(self.active_tournament.rounds) + 1}"
        new_round = Round(round_name)
        previous_matches = {
            (match.player1.id, match.player2.id)
            for round in self.active_tournament.rounds
            for match in round.matches
        }
        if len(self.active_tournament.rounds) == 0:
            print("First round")
            pairs = Pairing.generate_first_round_pairs(self.active_tournament.players)
        else:
            print("Next round")
            pairs = Pairing.generate_next_round_pairs(
                self.active_tournament.players, previous_matches
            )
            print(pairs)
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.active_tournament.rounds.append(new_round)
        self.tournament_view.display_added_round_message(round_name)

    def update_number_of_rounds(self):
        new_number = self.tournament_view.get_number_of_rounds()
        self.active_tournament.set_number_of_rounds(new_number)
        self.tournament_view.display_updated_number_rounds_message(new_number)

    def update_description(self):
        description = self.tournament_view.get_tournament_description()
        self.active_tournament.set_description(description)
        self.tournament_view.display_successful_description_message()

    def enter_scores(self):
        round_instance = self.active_tournament.get_current_round()
        self.tournament_view.display_record_results_message(round_instance.name)
        for match in round_instance.matches:
            if round_instance.is_finished():
                continue
            self.tournament_view.display_match_summary(match.get_player_names())
            result = self.tournament_view.get_match_result()
            if result == "1":
                match.set_score(1, 0)
            elif result == "2":
                match.set_score(0, 1)
            elif result == "0":
                match.set_score(0.5, 0.5)
        round_instance.end_round()

    def display_available_tournaments(self):
        self.tournament_view.display_tournaments(self.tournaments)

    def display_active_tournament(self):
        self.tournament_view.display_tournament_details(self.active_tournament)

    def display_players(self):
        self.player_controller.display_players(self.active_tournament.players)

    def display_player_names(self):
        self.player_controller.display_players_name(self.active_tournament.players)

    def display_current_round(self):
        current_round = self.active_tournament.get_current_round()
        if current_round:
            self.round_view.display_round_info(current_round)
            self.tournament_view.display_current_round(self.active_tournament)

    def display_player_pairs(self):
        current_round = self.active_tournament.get_current_round()
        if current_round:
            round_name, pairs = current_round.get_pairs_players()
            self.round_view.display_player_pairs(round_name, pairs)
