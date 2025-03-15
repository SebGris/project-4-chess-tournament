from models.tournament import Tournament
from typing import List


class TournamentManager:
    def __init__(self, all_tournaments):
        self.tournaments = all_tournaments
        self.active_tournament = None

    def add_tournament(self, tournament: Tournament) -> List[Tournament]:
        self.tournaments.append(tournament)
        self.active_tournament = tournament
        return self.tournaments

    def select_tournament(self, index: int) -> Tournament:
        self.active_tournament = self.tournaments[index]
        return self.active_tournament
