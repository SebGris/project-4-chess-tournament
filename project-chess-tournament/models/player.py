import uuid
from datetime import datetime


class Player:
    """Class representing a chess player."""

    def __init__(self, last_name, first_name, birth_date=None, id_chess=None,
                 score=0.0, id=None):
        self.id = uuid.UUID(id) if id else uuid.uuid4()
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = f"{self.first_name} {self.last_name}"
        self.birth_date = birth_date
        self.id_chess = id_chess
        self.score = score

    def formatted_birth_date(self):
        """Returns the birth date in dd/mm/yyyy format."""
        if self.birth_date:
            try:
                birth_date = datetime.strptime(
                    self.birth_date, "%Y-%m-%dT%H:%M:%S")
                return birth_date.strftime("%d/%m/%Y")
            except ValueError:
                return self.birth_date
        return None

    def update_score(self, points):
        """Adds points to the player's score."""
        self.score += points

    def reset_score(self):
        """Resets the player's score to zero."""
        self.score = 0.0

    def __repr__(self):
        return f"Player(full_name={self.full_name}, score={self.score})"

    def __str__(self):
        """Returns a string representation of the player."""
        return (f"{self.full_name} | "
                f"Né(e) le {self.formatted_birth_date()} | "
                f"ID échecs {self.id_chess}")

    def to_dict(self):
        """Convert Player object to dictionary."""
        return {
            "id": str(self.id),
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "id_chess": self.id_chess
        }
