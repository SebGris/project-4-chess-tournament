from models.tournament import Tournament
from models.tournament_repository import TournamentRepository

# from typing import List


class TournamentManager:
    def __init__(self, repository: TournamentRepository):
        self.repository = repository
        self.tournaments = []
        self.active_tournament = None

    def ajouter_tournoi(self, tournament: Tournament):
        self.tournaments.append(tournament)
        self.repository.save_tournaments(self.tournaments)

    def selectionner_tournoi(self, nom):
        for tournament in self.tournaments:
            if tournament.nom == nom:
                self.active_tournament = tournament
                print(f"Tournoi actif : {tournament.nom}")
                return
        print("Tournoi non trouvé.")

    def obtenir_tournoi_actif(self):
        return self.active_tournament

    def get_all_tournaments(self):
        return self.repository.get_all_tournaments()
