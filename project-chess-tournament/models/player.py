class Player:
    """Class representing a chess player."""

    def __init__(self, last_name,  first_name, birth_date, id_chess):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id_chess = id_chess
        self.score = 0.0  # Points accumulated during the tournament

    def update_score(self, points):
        """Adds points to the player's score."""
        self.score += points

    def __lt__(self, other):
        # Comparer d'abord par nom de famille, puis prénom, puis date
        if self.last_name == other.last_name:
            if self.first_name == other.first_name:
                return self.birth_date < other.birth_date
            return self.first_name < other.first_name
        return self.last_name < other.last_name

    def __repr__(self):
        return (f"Player({self.last_name}, {self.first_name}, "
                f"{self.birth_date})")

    def __str__(self):
        """Returns a string representation of the player."""
        return (f"{self.get_full_name()} | "
                f"Né(e) le {self.birth_date} | "
                f"ID échecs {self.id_chess} | "
                f"Score {self.score} points")

    def get_full_name(self):
        """Returns the full name of the player."""
        return f"{self.first_name} {self.last_name}"
