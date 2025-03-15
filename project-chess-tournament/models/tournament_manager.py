from models.tournament import Tournament
from models.tournament_repository import TournamentRepository


class TournamentManager:
    def __init__(self, tournament_repository: TournamentRepository):
        self.tournament_repository = tournament_repository
        self.tournaments = self.tournament_repository.get_all_tournaments()
        self.active_tournament = None

    def add_tournament(self, tournament: Tournament):
        self.tournaments.append(tournament)
        self.tournament_repository.save_tournaments(self.tournaments)

    def select_tournament(self, index):
        self.active_tournament = self.tournaments[index]

    def get_active_tournament(self):
        return self.active_tournament

    def get_all_tournaments(self):
        return self.tournament_repository.get_all_tournaments()
