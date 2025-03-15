from models.tournament import Tournament


class TournamentManager:
    def __init__(self, all_tournaments):
        self.tournaments = all_tournaments
        self.active_tournament = None

    def add_tournament(self, tournament: Tournament):
        self.tournaments.append(tournament)

    def select_tournament(self, index: int):
        self.active_tournament = self.tournaments[index]

    def get_active_tournament(self) -> Tournament:
        return self.active_tournament
