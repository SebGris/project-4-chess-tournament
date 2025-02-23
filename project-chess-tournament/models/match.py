class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def set_result(self, player1_score, player2_score):
        self.player1_score = player1_score
        self.player2_score = player2_score

    def to_dict(self):
        return {
            "player1": str(self.player1.id),
            "player1_score": self.player1_score,
            "player2": str(self.player2.id),
            "player2_score": self.player2_score
        }

    def __str__(self):
        """Returns a text representation of the match."""
        return (
            f"{self.player1[0]} vs {self.player2[0]} | "
            f"Scores: {self.player1[1]} - {self.player2[1]}"
        )
