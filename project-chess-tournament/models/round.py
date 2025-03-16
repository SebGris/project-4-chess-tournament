import uuid
from datetime import datetime
from typing import List
from models.match import Match
from dtos.round_dto import RoundDTO


class Round:
    """Represents a round in a chess tournament."""

    def __init__(self, name, round_id=None):
        self.name = name
        self.match_ids: List[Match] = []
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self._id = round_id or uuid.uuid4()

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.match_ids.append(match)

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
                for match in self.match_ids
            ],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": (
                self.end_datetime.isoformat() if self.end_datetime else None),
            "match_ids": [match.id for match in self.match_ids]
        }

    @staticmethod
    def from_dict(round):
        return Round(
            round["name"],
            round["start_datetime"],
            round["end_datetime"],
            round["id"]
        )

    @staticmethod
    def from_dto(round_dto: RoundDTO):
        return Round(
            round_dto.name,
            round_dto.start_datetime,
            round_dto.end_datetime,
            round_dto.id,
            uuid.UUID(round_dto.id)
        )

    @property
    def id(self):
        return str(self._id)
