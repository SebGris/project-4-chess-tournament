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
        self.matches = []
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

    def to_dict(self):
        """Convert Round object to dictionary."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @classmethod
    def from_dict(cls, data, all_players):
        round_instance = cls(
            round_number=int(data["name"].split()[1]),
            players=[all_players[player_id] for player_id in data["player_ids"]],
            previous_matches=[]
        )
        round_instance.start_time = data["start_time"]
        round_instance.end_time = data["end_time"]
        round_instance.matches = [Match.from_dict(match_data, all_players) for match_data in data["matches"]]
        return round_instance
