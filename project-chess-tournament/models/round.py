import uuid
from datetime import datetime
from models.match import Match
from typing import List


class Round:
    """Represents a round in a chess tournament."""

    def __init__(
        self,
        round_id: uuid.UUID,
        name,
        matches: List[Match],
        start_date=None,
        end_date=None,
    ):
        self.id = round_id
        self.name = name
        self.matches = matches if matches is not None else []
        self.start_datetime = (
            datetime.fromisoformat(start_date) if start_date else datetime.now()
        )
        self.end_datetime = datetime.fromisoformat(end_date) if end_date else None

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def end_round(self):
        """Marks the lap as completed and records the end time."""
        self.end_datetime = datetime.now()

    def is_finished(self):
        """Returns True if the round is completed, False otherwise."""
        return self.end_datetime is not None

    def get_pairs_players(self):
        """Returns the pairs of players (full name)."""
        return (
            self.name,
            [
                (
                    match.get_player_names_and_scores()
                    if match.is_finished()
                    else match.get_player_names()
                )
                for match in self.matches
            ],
        )

    def to_dict(self):
        """Convert Round object to dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "match_ids": [str(match.id) for match in self.matches],
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat() if self.end_datetime else None
            ),
        }

    @staticmethod
    def from_dict(round: dict):
        """Create a Tournament object from a dictionary."""
        return Round(
            uuid.UUID(round["id"]),
            round["name"],
            round["matches"],
            round["start_date"],
            round["end_date"],
        )
