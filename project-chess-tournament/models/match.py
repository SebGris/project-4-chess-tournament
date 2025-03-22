import uuid
from models.player import Player
from repositories.player_repository import PlayerRepository


class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(
        self,
        player1: Player,
        player2: Player,
        player1_score=0.0,
        player2_score=0.0,
        match_id=None,
    ):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score
        self._id = match_id or uuid.uuid4()

    def set_score(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def is_finished(self):
        """If the sum of the two scores is not zero."""
        return self.player1_score + self.player2_score != 0

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

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dict(match_data):
        player_repo = PlayerRepository()
        player1 = player_repo.get_player_by_id(match_data["player1"])
        player2 = player_repo.get_player_by_id(match_data["player2"])
        match = Match(
            player1,
            player2,
            match_data["player1_score"],
            match_data["player2_score"],
            match_data["id"],
        )
        return match

    def to_dict(self):
        return {
            "id": self.id,
            "player1": self.player1.id,
            "player2": self.player2.id,
            "player1_score": self.player1_score,
            "player2_score": self.player2_score,
        }
