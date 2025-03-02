from datetime import datetime
from models.match import Match
from models.player import Player


class Round:
    """Represents a round in a chess tournament."""

    def __init__(
        self, name, matches=None, start_datetime=None, end_datetime=None
    ):
        self.name = name
        self.matches = (
            self.convert_dict_to_matches(matches)
            if matches is not None else []
        )
        self.start_datetime = (
            datetime.fromisoformat(start_datetime)
            if start_datetime
            else datetime.now()
        )
        self.end_datetime = (
            datetime.fromisoformat(end_datetime) if end_datetime else None
        )

    def convert_dict_to_matches(self, matches):
        return [
            Match(
                Player(
                    match['player1']['last_name'],
                    match['player1']['first_name'],
                    id=match['player1']['id']
                ),
                Player(
                    match['player2']['last_name'],
                    match['player2']['first_name'],
                    id=match['player2']['id']
                ),
                match['player1_score'],
                match['player2_score']
            )
            for match in matches
        ]

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def end_round(self):
        """Marks the lap as completed and records the end time."""
        self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_pairs_players(self):
        """Returns the pairs of players (full name)."""
        return (
            self.name,
            [
                match.get_player_full_names()
                for match in self.matches
            ]
        )

    def to_dict(self):
        """Convert Round object to dictionary."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat() if self.end_datetime else None
            )
        }

    def __str__(self):
        """Returns a string representation of the round."""
        matches_str = "\n".join(str(match) for match in self.matches)
        return (
            f"Round: {self.name}\n"
            f"Start: {self.start_datetime}\n"
            f"End: {self.end_datetime}\n"
            f"Matches:\n{matches_str}"
        )
