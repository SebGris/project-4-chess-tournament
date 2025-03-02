class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def set_result(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def to_dict(self):
        return {
            "player1": {
                "id": str(self.player1.id),
                "last_name": self.player1.last_name,
                "first_name": self.player1.first_name
            },
            "player1_score": self.player1_score,
            "player2": {
                "id": str(self.player2.id),
                "last_name": self.player2.last_name,
                "first_name": self.player2.first_name
            },
            "player2_score": self.player2_score
        }

    def get_player_full_names(self):
        """Returns a tuple of the full names of player1 and player2."""
        return self.player1.full_name, self.player2.full_name

    def __str__(self):
        """Returns a text representation of the match."""
        return (
            f"{self.player1[0]} vs {self.player2[0]} | "
            f"Scores: {self.player1[1]} - {self.player2[1]}"
        )
