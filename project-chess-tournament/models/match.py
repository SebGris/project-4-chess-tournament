class Match:
    """Represents a match between two players in a chess tournament."""

    MATCH_RESULT = {
        '1': "victoire du premier joueur",
        '2': "victoire du deuxième joueur",
        '3': "match nul"
        }

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

    def get_players(self):
        """Returns the players who took part in the match."""
        return self.player1[0], self.player2[0]

    def __str__(self):
        """Returns a text representation of the match."""
        return (f"{self.player1[0]} vs {self.player2[0]} | "
                f"Scores: {self.player1[1]} - {self.player2[1]}")
