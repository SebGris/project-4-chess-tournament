import uuid


class Player:
    """Class representing a chess player."""
    def __init__(self, last_name, first_name, birth_date, chess_id,
                 player_id=None):
        """Initialize a Player instance."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0.0
        self._id = player_id or uuid.uuid4()
        self.full_name = f"{self.first_name} {self.last_name}"

    @property
    def id(self):
        return str(self._id)

    @classmethod
    def from_dict(cls, player_data):
        """Create a Player instance from a dictionary."""
        return cls(
            player_data["last_name"],
            player_data["first_name"],
            player_data["birth_date"],
            player_data["chess_id"],
            player_data.get("id"),
        )

    def to_dict(self):
        """Convert the Player instance to a dictionary."""
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
        }
