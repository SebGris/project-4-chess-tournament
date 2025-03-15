from controllers.pairing import Pairing
from controllers.player_controller import PlayerController
from models.player import Player
from models.player_repository import PlayerRepository
from models.round import Round
from models.tournament import Tournament
from models.tournament_manager import TournamentManager
from models.tournament_repository import TournamentRepository
from views.player_view import PlayerView
from views.round_view import RoundView
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self, tournament_repository: TournamentRepository, view: TournamentView):
        self.tournament_repository = tournament_repository
        self.tournament_view = view
        self.tournament_manager = TournamentManager(self.get_all_tournaments())
        player_repository = PlayerRepository()
        player_view = PlayerView()
        self.round_view = RoundView()
        self.player_controller = PlayerController(player_repository, player_view)

    def get_all_tournaments(self):
        return self.tournament_repository.get_all_tournaments()

    def get_active_tournament(self):
        return self.tournament_manager.get_active_tournament()

    def get_tournament_by_id(self, tournament_id):
        tournament = self.tournament_manager.find_tournament_by_id(tournament_id)
        self.tournament_view.display_tournament_details(tournament)

    def collect_tournament_info(self):
        name = self.tournament_view.get_name()
        location = self.tournament_view.get_location()
        start_date = self.tournament_view.get_start_date()
        end_date = self.tournament_view.get_end_date()
        number_of_rounds = self.tournament_view.get_number_of_rounds()
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rounds": number_of_rounds,
        }

    def create_new_tournament(self):
        tournament_info = self.collect_tournament_info()
        self.create_tournament(**tournament_info)
        self.tournament_view.display_tournament_created(tournament_info["name"])

    def create_tournament(self, name, location, start_date, end_date, number_of_rounds):
        tournament = Tournament(name, location, start_date, end_date, number_of_rounds)
        self.tournament_manager.add_tournament(tournament)
        # self.tournament_repository.save_tournaments(self.tournaments)

    def select_tournament(self):
        tournaments = self.get_all_tournaments()
        index = self.tournament_view.get_tournament_selection(tournaments)
        self.tournament_manager.select_tournament(index)

    def update_tournament(self, tournament_id, name, date):
        updated_data = {"name": name, "date": date}
        tournament = self.tournament_manager.update_tournament(
            tournament_id, updated_data
        )
        self.tournament_view.display_tournament_updated(tournament)

    def load_all_players(self):
        try:
            all_players = {
                player_data["id"]: Player(**player_data)
                for player_data in self.load_players_data()
            }
            return all_players
        except FileNotFoundError as e:
            self.tournament_view.display_for_file_not_found(str(e))

    def add_player(self, player_data):
        player = Player(**player_data)
        self.active_tournament.players.append(player)
        return str(player.id)

    def get_players(self):
        return [
            {**player.to_dict(), "full_name": player.full_name}
            for player in self.active_tournament.players
        ]

    def start_tournament(self):
        for index in range(1, self.active_tournament.number_of_rounds):
            self.active_tournament.update_scores(round.matches)
            print(self.active_tournament.players)
            # if self.active_tournament.number_of_rounds > len(self.active_tournament.rounds):
            current_round = self.active_tournament.get_current_round()
            if current_round is None:
                self.add_round()
            elif current_round.is_finished():
                self.add_round()

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
        tournaments = self.get_all_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def display_active_tournament(self):
        tournament = self.get_active_tournament()
        self.tournament_view.display_tournament_details(tournament)

    def display_player_names(self):
        active_tournament = self.get_active_tournament()
        if active_tournament:
            players_names = [
                player.full_name for player in active_tournament.players
            ]
            self.player_controller.display_tournament_players(players_names)
        else:
            self.tournament_view.display_no_tournament_message()

    def display_current_round(self):
        active_tournament = self.get_active_tournament()
        current_round = active_tournament.get_current_round()
        if current_round:
            self.round_view.display_round_info(current_round)
            self.tournament_view.display_current_round(active_tournament)
            # self.tournament_view.display_no_tournament_message()
            # self.tournament_view.display_no_round_message()

    def display_player_pairs(self):
        active_tournament = self.get_active_tournament()
        current_round = active_tournament.get_current_round()
        if current_round:
            round_name, pairs = current_round.get_pairs_players()
            self.round_view.display_player_pairs(round_name, pairs)
            # self.controller.tournament_view.display_no_round_message()
            # self.controller.tournament_view.display_no_tournament_message()
