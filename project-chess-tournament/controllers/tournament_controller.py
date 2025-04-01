from typing import Optional
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
    """Controller for managing tournaments in the chess tournament application."""
    def __init__(
        self,
        tournament_repository: TournamentRepository,
        player_repository: PlayerRepository,
        round_repository: RoundRepository,
        match_repository: MatchRepository,
        view: TournamentView,
    ):
        """Initializes the TournamentController with the repositories and view."""
        self.tournament_repository = tournament_repository
        self.player_repository = player_repository
        self.round_repository = round_repository
        self.match_repository = match_repository
        self.view = view
        self.tournaments = self.get_tournaments()
        self.active_tournament: Optional[Tournament] = None

    def get_tournaments(self):
        """Fetches all tournaments from the repository."""
        return self.tournament_repository.get_all()

    def get_active_tournament(self):
        """Returns the active tournament."""
        return self.active_tournament

    def get_active_round(self):
        """Returns the active round of the active tournament."""
        if self.active_tournament.rounds:
            return self.active_tournament.rounds[-1]
        return None

    def collect_tournament_info(self):
        """Collects tournament information from the user."""
        return {
            "name": self.view.get_name(),
            "location": self.view.get_location(),
            "start_date": self.view.get_start_date(),
            "end_date": self.view.get_end_date(),
            "total_rounds": self.view.get_total_of_rounds(),
        }

    def create_new_tournament(self):
        """Creates a new tournament."""
        tournament_info = self.collect_tournament_info()
        self.create_tournament(**tournament_info)
        self.view.display_tournament_created(tournament_info["name"])

    def create_tournament(self, name, location, start_date, end_date, total_rounds):
        """Creates a new tournament and adds it to the list."""
        tournament = Tournament(name, location, start_date, end_date, total_rounds)
        self.tournaments.append(tournament)
        # Set the newly created tournament as the active tournament
        self.active_tournament = self.tournaments[-1]
        self.save_tournaments()

    def select_tournament(self):
        """Selects a tournament from the list."""
        index = self.view.get_tournament_selection(self.tournaments)
        self.active_tournament = self.tournaments[index]
        self.update_scores(self.active_tournament.get_all_matches())

    def save_tournaments(self):
        """Saves the tournaments to the repository."""
        self.tournament_repository.save(self.tournaments)

    def add_players(self):
        """Adds players to the active tournament."""
        self.view.display_add_player_message()
        players_data = iter(self.view.get_player_data, None)
        players = [Player(**data) for data in players_data]
        self.active_tournament.add_players(players)
        self.player_repository.save(players)
        self.save_tournaments()

    def start_round(self):
        """Starts a new round in the active tournament."""
        if self._check_if_start():
            self.add_round()
            active_round = self.get_active_round()
            self.round_repository.save(active_round)
            self.match_repository.save(active_round.matches)
            self.save_tournaments()

    def _check_if_start(self):
        """Checks if the tournament can be started."""
        if not self._has_players():
            self.view.display_start_error_without_players()
            return False
        if self._has_odd_number_of_players():
            self.view.display_start_error_even_players()
            return False
        if self._has_unfinished_matches():
            self.view.display_start_error_unfinished_match()
            return False
        if self._tournament_is_finished():
            self.view.display_start_error_tournament_finished()
            return False
        return True

    def _has_players(self):
        """Checks if the tournament has players."""
        return bool(self.active_tournament.players)

    def _has_odd_number_of_players(self):
        """Checks if the tournament has an odd number of players."""
        return len(self.active_tournament.players) % 2 != 0

    def _has_unfinished_matches(self):
        """Checks if there are unfinished matches in the tournament."""
        for round in self.active_tournament.rounds:
            for match in round.matches:
                if not match.is_finished():
                    return True
        return False

    def _tournament_is_finished(self):
        """Checks if the tournament is finished."""
        return self.active_tournament.is_finished()

    def add_round(self):
        """Adds a new round to the active tournament."""
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

    def update_total_rounds(self):
        """Updates the total number of rounds in the active tournament."""
        new_number = self.view.get_total_of_rounds()
        self.active_tournament.set_total_of_rounds(new_number)
        self.view.display_updated_number_rounds_message(new_number)

    def update_description(self):
        """Updates the description of the active tournament."""
        description = self.view.get_tournament_description()
        self.active_tournament.set_description(description)
        self.view.display_successful_description_message()

    def enter_scores(self):
        """Enters the scores for the matches in the current round."""
        round = self.get_active_round()
        if round is None:
            self.view.display_no_round_error()
        elif round.is_finished():
            self.view.display_round_finished_message()
        else:
            self.view.display_record_results_message(round)
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
                    self.match_repository.save(match)
            round.end_round()
            self.round_repository.save(round)
            self.update_scores(round.matches)

    def update_scores(self, matches: list[Match]):
        """Updates the scores of players based on the matches."""
        for match in matches:
            player1_id, player1_score = match.get_player1()
            player2_id, player2_score = match.get_player2()
            for player in self.active_tournament.players:
                if player.id == player1_id:
                    player.score += player1_score
                elif player.id == player2_id:
                    player.score += player2_score

    def display_active_tournament_details(self):
        """Displays the details of the active tournament."""
        self.view.display_tournament_details(self.active_tournament)

    def display_tournaments_details(self):
        """Displays the details of all tournaments."""
        self.view.display_tournaments_details(self.tournaments)

    def display_current_round_info(self):
        """Displays information about the current round."""
        self.view.display_current_round_info(self.active_tournament)

    def display_player_names(self):
        """Displays the names of players in the active tournament."""
        self.view.display_players_name(self.active_tournament.players)

    def display_player_pairs(self):
        """Displays the pairs of players in the current round."""
        self.view.display_player_pairs(self.get_active_round())

    def display_players(self):
        """Displays the players in the active tournament."""
        self.view.display_players_details(self.active_tournament.players)

    def report_tournaments(self):
        """Reports the list of tournaments."""
        tournaments: list[Tournament] = self.tournament_repository.get_all()
        tournaments = [tournament.to_dict() for tournament in tournaments]
        self.view.report_tournaments(tournaments)

    def report_name_dates(self):
        """Reports the name and dates of the active tournament."""
        tournament = self.active_tournament.to_dict()
        self.view.report_name_and_dates(tournament)

    def report_players(self):
        """Reports the players in the active tournament."""
        players = [
            player.to_dict()
            for player in self.active_tournament.players
        ]
        self.view.report_players(players, self.active_tournament)

    def report_rounds_matches(self):
        """Reports the rounds and matches of the active tournament."""
        rounds_dict = []
        for round in self.active_tournament.rounds:
            round_dict = round.to_dict()
            matches_dict = []
            for match in round.matches:
                match_dict = match.to_dict()
                match_dict["index"] = f"N° {round.matches.index(match) + 1}"
                match_dict["player1"] = match.player1.full_name
                match_dict["player2"] = match.player2.full_name
                matches_dict.append(match_dict)
            round_dict["matches"] = matches_dict
            rounds_dict.append(round_dict)
        self.view.report_rounds_matches(rounds_dict)
