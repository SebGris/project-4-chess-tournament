from datetime import datetime
from models.match import Match


class Round:
    """Represents a round in a chess tournament."""

    def __init__(
        self, name, matches=None, start_datetime=None, end_datetime=None
    ):
        self.name = name
        self.matches = matches if matches is not None else []
        self.start_datetime = (
            datetime.fromisoformat(start_datetime) if start_datetime else \
            datetime.now()
        )
        self.end_datetime = (
            datetime.fromisoformat(end_datetime) if end_datetime else None
        )

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def end_round(self):
        """Marks the lap as completed and records the end time."""
        self.end_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        """Convert Round object to dictionary."""
        return {
            "name": self.name,
            "matches": self.matches,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat() if self.end_datetime else None
            )
        }
