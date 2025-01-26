class Round:
    """Class representing one round in a tournament."""

    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []  # Liste des matchs pour ce tour

    def add_match(self, match):
        """Add a match to this round."""
        self.matches.append(match)

    def __str__(self):
        """Returns a representation of the round with all the matches."""
        return (f" Tour {self.round_number}: "
                "\n".join(str(match) for match in self.matches))
