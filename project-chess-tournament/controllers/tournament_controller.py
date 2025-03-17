from typing import List
from controllers.pairing import Pairing
from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository
from repositories.tournament_repository import TournamentRepository
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(
        self,
        tournament_repository: TournamentRepository,
        player_repository: PlayerRepository,
        round_repository: RoundRepository,
        match_repository: MatchRepository,
        view: TournamentView
    ):
        self.tournament_repository = tournament_repository
        self.player_repository = player_repository
        self.round_repository = round_repository
        self.match_repository = match_repository
        self.view = view
        self.tournaments = self.get_tournaments()
        self.active_tournament = None

    def get_tournaments(self):
        return [
            Tournament.from_dto(
                tournament_dto,
                self.player_repository,
                self.round_repository,
                self.match_repository
            )
            for tournament_dto in self.tournament_repository.get_tournaments()
        ]

    def get_active_tournament(self):
        return self.active_tournament

    def get_active_round(self):
        return (
            self.active_tournament.rounds[-1]
            if self.active_tournament.rounds
            else None
        )

    def collect_tournament_info(self):
        return {
            "name": self.view.get_name(),
            "location": self.view.get_location(),
            "start_date": self.view.get_start_date(),
            "end_date": self.view.get_end_date(),
            "total_rounds": self.view.get_total_of_rounds(),
        }

    def create_new_tournament(self):
        """Create a new tournament."""
        tournament_info = self.collect_tournament_info()
        self.create_tournament(**tournament_info)
        self.view.display_tournament_created(tournament_info["name"])

    def create_tournament(
        self, name, location, start_date, end_date, total_rounds
    ):
        tournament = Tournament(
            name, location, start_date, end_date, total_rounds
        )
        self.tournaments.append(tournament)
        # Set the newly created tournament as the active tournament
        self.active_tournament = self.tournaments[-1]
        self.save_tournaments()

    def select_tournament(self):
        index = self.view.get_tournament_selection(self.tournaments)
        self.active_tournament = self.tournaments[index]
        self.update_scores(self.active_tournament.get_all_matches())

    def save_tournaments(self):
        tournaments_dto = [
            tournament.to_dto() for tournament in self.tournaments
        ]
        self.tournament_repository.write_tournaments_to_file(tournaments_dto)

    def add_players(self):
        players_data = iter(self.view.get_player_data, None)
        players = [Player(**data) for data in players_data]
        self.active_tournament.add_players(players)
        players_dto = [player.to_dto() for player in players]
        self.player_repository.save(players_dto)
        self.save_tournaments()

    def start_round(self):
        if self.__check_if_start():
            self.add_round()
            active_round = self.get_active_round()
            self.round_repository.save(active_round.to_dto())
            matches_dto = [match.to_dto() for match in active_round.matches]
            self.match_repository.save_a_list(matches_dto)
            self.save_tournaments()

    def __check_if_start(self):
        if not self.__has_players():
            self.view.display_start_error_without_players()
            return False
        if self.__has_odd_number_of_players():
            self.view.display_start_error_even_players()
            return False
        if self.__has_unfinished_matches():
            self.view.display_start_error_unfinished_match()
            return False
        return True

    def __has_players(self):
        return bool(self.active_tournament.players)

    def __has_odd_number_of_players(self):
        return len(self.active_tournament.players) % 2 != 0

    def __has_unfinished_matches(self):
        for round in self.active_tournament.rounds:
            for match in round.matches:
                if not match.is_finished():
                    return True
        return False

    def add_round(self):
        number_rounds = len(self.active_tournament.rounds)
        new_round = Round(f"Round {number_rounds + 1}")
        if number_rounds == 0:
            pairs = Pairing.generate_first_round_pairs(
                self.active_tournament.players
            )
        else:
            previous_matches = {
                (match.player1.id, match.player2.id)
                for round in self.active_tournament.rounds
                for match in round.matches
            }
            pairs = Pairing.generate_next_round_pairs(
                self.active_tournament.players, previous_matches
            )
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.active_tournament.rounds.append(new_round)
        self.view.display_added_round_message(new_round)
        self.display_player_pairs()

    def update_total_of_rounds(self):
        new_number = self.view.get_total_of_rounds()
        self.active_tournament.set_total_of_rounds(new_number)
        self.view.display_updated_number_rounds_message(new_number)

    def update_description(self):
        description = self.view.get_tournament_description()
        self.active_tournament.set_description(description)
        self.view.display_successful_description_message()

    def enter_scores(self):
        round = self.get_active_round()
        if round is None:
            self.view.display_no_round_error()
        elif round.is_finished():
            self.view.display_round_finished_message()
        else:
            self.view.display_record_results_message(round.name)
            for match in round.matches:
                if not match.is_finished():
                    self.view.display_match_summary(match.get_player_names())
                    result = self.view.get_match_result()
                    if result == "1":
                        match.set_score(1, 0)
                    elif result == "2":
                        match.set_score(0, 1)
                    elif result == "0":
                        match.set_score(0.5, 0.5)
                    else:
                        self.view.display_invalid_result_message()
                    self.match_repository.save(match.to_dto())
            round.end_round()
            self.round_repository.save(round.to_dto())
            self.update_scores(round.matches)

    def update_scores(self, matches: List[Match]):
        for match in matches:
            player1_id, player1_score = match.get_player1()
            player2_id, player2_score = match.get_player2()
            for player in self.active_tournament.players:
                if player.id == player1_id:
                    player.score += player1_score
                elif player.id == player2_id:
                    player.score += player2_score

    def display_active_tournament_details(self):
        self.view.display_tournament_details(self.active_tournament)

    def display_all_tournaments_details(self):
        self.view.display_tournaments_details(self.tournaments)

    def display_all_tournaments(self):
        self.view.display_tournaments(self.tournaments)

    def display_current_round_info(self):
        self.view.display_current_round_info(self.active_tournament)

    def display_player_names(self):
        self.view.display_players_name(self.active_tournament.players)

    def display_player_pairs(self):
        self.view.display_player_pairs(self.get_active_round())

    def display_players(self):
        self.view.display_players_details(self.active_tournament.players)
