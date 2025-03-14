from controllers.pairing import Pairing
from controllers.player_controller import PlayerController
from models.player import Player
from models.player_repository import PlayerRepository
from models.round import Round
from models.tournament import Tournament
from models.tournament_manager import TournamentManager
from views.player_view import PlayerView
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self, manager: TournamentManager, view: TournamentView):
        self.tournament_manager = manager
        self.tournament_view = view
        player_repo = PlayerRepository()
        player_view = PlayerView()
        self.player_controller = PlayerController(player_repo, player_view)

    def show_all_tournaments(self):
        tournaments = self.tournament_manager.get_all_tournaments()
        self.tournament_view.display_tournaments(tournaments)

    def show_tournament_selection(self):
        tournaments = self.tournament_manager.get_all_tournaments()
        self.tournament_view.get_tournament_selection(tournaments)

    def get_tournament_by_id(self, tournament_id):
        tournament = self.tournament_manager.find_tournament_by_id(tournament_id)
        self.tournament_view.display_tournament_details(tournament)

    def create_tournament(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_rounds,
        description,
        player_ids,
        rounds_list,
    ):
        players_list = (
            [self.all_players[player_id] for player_id in player_ids]
            if player_ids
            else []
        )
        rounds_list = [Round(**round) for round in rounds_list] if rounds_list else []
        tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            number_of_rounds,
            description,
            players_list,
            rounds_list,
        )
        self.tournament_manager.create_tournament(tournament)
        self.tournament_view.display_new_tournament_created(tournament)

    def update_tournament(self, tournament_id, name, date):
        updated_data = {"name": name, "date": date}
        tournament = self.tournament_manager.update_tournament(
            tournament_id, updated_data
        )
        self.tournament_view.display_tournament_updated(tournament)

    def select_tournament(self, tournament_index):
        self.active_tournament = self.tournaments[tournament_index]
        self.tournament_view.menu.set_tournament_loaded(True)

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

    def update_number_of_rounds(self, new_number_of_rounds):
        self.active_tournament.set_number_of_rounds(new_number_of_rounds)

    def update_description(self, description):
        self.active_tournament.set_description(description)

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
