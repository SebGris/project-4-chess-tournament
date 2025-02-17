class Match:
    """Represents a match between two players in a chess tournament."""

    def __init__(self, player1, player2):
        """
        Initialises a match with two players and default scores of 0.
        :param player1: Player object representing the first player.
        :param player2: Player object representing the second player.
        """
        self.player1 = [player1, 0]  # Joueur 1 et son score
        self.player2 = [player2, 0]  # Joueur 2 et son score

    def set_score(self, score1, score2):
        """
        Scores the players after a match.
        """
        self.player1[1] = score1
        self.player2[1] = score2

    def to_dict(self):
        """Convert Match object to dictionary."""
        return {
            "player1": self.player1[0].to_dict(),
            "player2": self.player2[0].to_dict(),
            "score1": self.player1[1],
            "score2": self.player2[1]
        }

    @classmethod
    def from_dict(cls, data, all_players):
        match_instance = cls(
            player1=all_players[data["player1"]["id"]],
            player2=all_players[data["player2"]["id"]]
        )
        match_instance.set_score(data["score1"], data["score2"])
        return match_instance

    def __str__(self):
        """Returns a text representation of the match."""
        return (
            f"{self.player1[0]} vs {self.player2[0]} | "
            f"Scores: {self.player1[1]} - {self.player2[1]}"
        )
