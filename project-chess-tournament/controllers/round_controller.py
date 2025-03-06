from models.round import Round
from controllers.pairing import Pairing
from views.round_view import RoundView


class RoundController:
    """Ne respecte pas le principe DIP : Dependency Inversion Principle
    Voir https://techblog.deepki.com/SOLID-in-python/"""
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view

    @staticmethod
    def create_round(nom, matchs):
        round = Round(nom, matchs)
        RoundView.afficher_round(round)
        return round

    def add_round(self):
        round_name = f"Round {len(self.tournament.rounds) + 1}"
        new_round = Round(round_name)
        previous_matches = {
            (match.player1.id, match.player2.id)
            for round in self.tournament.rounds
            for match in round.matches
        }
        if len(self.tournament.rounds) == 0:
            print("First round")
            pairs = Pairing.generate_first_round_pairs(self.tournament.players)
        else:
            print("Next round")
            pairs = Pairing.generate_next_round_pairs(
                self.tournament.players, previous_matches)
            print(pairs)
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.tournament.rounds.append(new_round)
        self.view.display_message(f"{round_name} ajouté")
