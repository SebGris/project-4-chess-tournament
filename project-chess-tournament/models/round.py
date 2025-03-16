import uuid
from datetime import datetime
from typing import List
from models.match import Match
from dtos.round_dto import RoundDTO


class Round:
    """Represents a round in a chess tournament."""

    def __init__(self, name, round_id=None):
        self.name = name
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self._id = round_id or uuid.uuid4()
        self.matches: List[Match] = []

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

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dto(round_dto: RoundDTO):
        return Round(
            round_dto.name,
            round_dto.start_datetime,
            round_dto.end_datetime,
            round_dto.id,
            uuid.UUID(round_dto.id)
        )

    def to_dto(self):
        return RoundDTO(
            self.id,
            self.name,
            [match.id for match in self.matches],
            self.start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            self.end_datetime.strftime("%Y-%m-%d %H:%M:%S")
            if self.end_datetime
            else None
        )
