import uuid
from .player import Player
from typing import Dict


class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(
        self,
        match_id: uuid.UUID,
        player1: Player,
        player2: Player,
        player1_score=0.0,
        player2_score=0.0,
    ):
        self.id = match_id
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def set_score(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def is_finished(self):
        """Returns True if player score 1 is not negative, False otherwise."""
        return self.player1_score >= 0

    def to_dict(self):
        return {
            "id": str(self.id),
            "player1_id": str(self.player1.id),
            "player1_score": self.player1_score,
            "player2_id": str(self.player2.id),
            "player2_score": self.player2_score,
        }

    def get_player_names(self):
        """Returns a tuple of the full names of player1 and player2."""
        return self.player1.full_name, self.player2.full_name

    def get_player_names_and_scores(self):
        """Returns a tuple of the full names of player1, player2 and score."""
        names = self.get_player_names()
        scores = self.player1_score, self.player2_score
        return names + scores

    def get_player1(self):
        return self.player1.id, self.player1_score

    def get_player2(self):
        return self.player2.id, self.player2_score

    @staticmethod
    def from_dict(match_dict: Dict[str, str]) -> "Match":
        match = Match(
            uuid.UUID(match_dict["id"]),
            match_dict["player1_id"],
            match_dict["player1_score"],
            match_dict["player2_id"],
            match_dict["player2_score"],
        )
        return match
