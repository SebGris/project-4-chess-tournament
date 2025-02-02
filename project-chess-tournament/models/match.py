class Match:
    """Class representing a match between two players."""

    MATCH_RESULT = {
        '1': "victoire du premier joueur",
        '2': "victoire du deuxième joueur",
        '3': "match nul"
        }

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def assign_points(self, result):
        """Attribue les points aux joueurs selon le résultat du match."""
        self.result = result
        if self.result == '1':
            self.player1.points += 1
            self.player2.points += 0
        elif self.result == '2':
            self.player1.points += 0
            self.player2.points += 1
        elif self.result == '3':
            self.player1.points += 0.5
            self.player2.points += 0.5

    def __str__(self):
        """Retourne une représentation du match et de son résultat."""
        return (f"{self.player1.first_name} {self.player1.last_name} vs "
                f"{self.player2.first_name} {self.player2.last_name} | "
                f"Résultat : {self.result}")
