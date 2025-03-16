import uuid
from .player import Player


class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(self, player1: Player, player2: Player, player1_score=0.0, player2_score=0.0, match_id=None):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score
        self._id = match_id or uuid.uuid4()

    def set_score(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def update_scores(self, match_results):
        for match in match_results:
            player1_id, player1_score = match.get_player1()
            player2_id, player2_score = match.get_player2()
            for player in self.players:
                if player.id == player1_id:
                    player.score += player1_score
                elif player.id == player2_id:
                    player.score += player2_score

    def is_finished(self):
        """Returns True if player score 1 is not negative, False otherwise."""
        return self.player1_score >= 0

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

    def to_dict(self):
        return {
            "id": self.id,
            "player1_id": self.player1.id,
            "player1_score": self.player1_score,
            "player2_id": self.player2.id,
            "player2_score": self.player2_score,
        }

    @staticmethod
    def from_dict(match_dict):
        return Match(
            match_dict["player1_id"],
            match_dict["player1_score"],
            match_dict["player2_id"],
            match_dict["player2_score"],
            match_dict["id"]
        )

    @property
    def id(self):
        return str(self._id)
