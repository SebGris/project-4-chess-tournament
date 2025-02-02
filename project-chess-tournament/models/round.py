from datetime import datetime
from models.match import Match
from models.pairing import Pairing


class Round:
    """Represents a round in a chess tournament."""

    def __init__(self, round_number, players, previous_matches):
        """
        Initialise a round with a number, a list of matches and timestamps.
        :param round_number: Round number (e.g. 1 for "Round 1").
        """
        self.name = f"Round {round_number}"
        self.matches = []  # Liste des matchs sous forme de tuples
        self.start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.end_time = None  # Sera rempli lorsque le tour se termine
        # Générer les paires selon le tour
        if round_number == 1:
            pairs = Pairing.generate_first_round_pairs(players)
        else:
            pairs = Pairing.generate_next_round_pairs(
                players, previous_matches)

        for player1, player2 in pairs:
            self.matches.append(Match(player1, player2))

    def end_round(self):
        """Marks the lap as completed and records the end time."""
        self.end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_played_matches(self):
        """Retourne la liste des matchs joués."""
        return [(match.player1[0], match.player2[0]) for match in self.matches]
