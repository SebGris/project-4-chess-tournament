import uuid


class Player:
    """Class representing a chess player."""

    def __init__(self, last_name, first_name, birth_date, id_chess):
        self.id = uuid.uuid4()
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id_chess = id_chess
        self.score = 0.0  # Points accumulated during the tournament

    def update_score(self, points):
        """Adds points to the player's score."""
        self.score += points

    def reset_score(self):
        """Resets the player's score to zero."""
        self.score = 0.0

    def __repr__(self):
        return (f"{self.get_full_name()} score: {self.score}")

    def __str__(self):
        """Returns a string representation of the player."""
        return (f"{self.get_full_name()} | "
                f"Né(e) le {self.birth_date} | "
                f"ID échecs {self.id_chess} | "
                f"Score {self.score} points | "
                f"ID {self.id}")

    def to_dict(self):
        """Convert Player object to dictionary."""
        return {
            "id": str(self.id),
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "id_chess": self.id_chess,
            "score": self.score
        }

    def get_full_name(self):
        """Returns the full name of the player."""
        return f"{self.first_name} {self.last_name}"
