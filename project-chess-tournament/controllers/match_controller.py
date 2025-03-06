from models.match import Match
from views.match_view import MatchView


class MatchController:
    @staticmethod
    def create_match(player1, player2, player1_score=0, player2_score=0):
        match = Match(player1, player2, player1_score, player2_score)
        MatchView.afficher_match(match)
        return match
