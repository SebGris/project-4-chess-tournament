class Player:
    """Class representing a chess player."""

    def __init__(self, last_name,  first_name, date_of_birth, id_chess):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.id_chess = id_chess
        self.score = 0.0  # Points accumulated during the tournament

    def update_score(self, points):
        """Adds points to the player's score."""
        self.score += points

    def __str__(self):
        """Returns a string representation of the player."""
        return (f"{self.get_full_name()} | "
                f"Né(e) le {self.date_of_birth} | "
                f"ID échecs {self.id_chess} | "
                f"Score {self.score} points")

    def get_full_name(self):
        """Returns the full name of the player."""
        return f"{self.first_name} {self.last_name}"
