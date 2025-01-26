class Match:
    """Class representing a match between two players."""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def set_result(self, result):
        """Assigns a result to the match."""
        # '1' pour la victoire du premier joueur,
        # '0' pour la victoire du deuxième joueur,
        # '0.5' pour un match nul.
        if result not in ['1', '0', '0.5']:
            raise ValueError("Le résultat doit être '1', '0' ou '0.5'.")
        self.result = result
        self._assign_points()

    def _assign_points(self):
        """Attribue les points aux joueurs selon le résultat du match."""
        if self.result == '1':
            self.player1.points += 1
            self.player2.points += 0
        elif self.result == '0':
            self.player1.points += 0
            self.player2.points += 1
        elif self.result == '0.5':
            self.player1.points += 0.5
            self.player2.points += 0.5

    def __str__(self):
        """Retourne une représentation du match et de son résultat."""
        return (f"{self.player1.first_name} {self.player1.last_name} vs "
                f"{self.player2.first_name} {self.player2.last_name} | "
                f"Résultat : {self.result}")
