import uuid
from datetime import datetime
from typing import List
from dtos.round_dto import RoundDTO
from models.match import Match
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository


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

    def set_start_date(self, start_datetime):
        self.start_datetime = start_datetime

    def set_end_date(self, end_datetime):
        self.end_datetime = end_datetime

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
    def from_dto(
        round_dto: RoundDTO,
        match_repo: MatchRepository,
        player_repo: PlayerRepository
    ):
        round = Round(
            round_dto.name,
            uuid.UUID(round_dto.id)
        )
        matches_dto = match_repo.get_matches_by_ids(round_dto.match_ids)
        round.matches.extend(
            [Match.from_dto(m, player_repo) for m in matches_dto]
        )
        round.set_start_date(round_dto.start_datetime)
        round.set_end_date(round_dto.end_datetime)
        return round

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
