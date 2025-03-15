import uuid
from datetime import datetime
from typing import Optional, Dict


class Player:
    def __init__(self, last_name: str, first_name: str, birth_date: str, id_chess: str, player_id=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.id_chess = id_chess
        self._id = player_id or uuid.uuid4()
        self.full_name = f"{self.first_name} {self.last_name}"

    def formatted_birth_date(self) -> Optional[str]:
        """Returns the birth date in dd/mm/yyyy format."""
        if self.birth_date:
            try:
                birth_date = datetime.strptime(self.birth_date, "%Y-%m-%dT%H:%M:%S")
                return birth_date.strftime("%d/%m/%Y")
            except ValueError:
                return self.birth_date
        return None

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "id_chess": self.id_chess
        }

    @staticmethod
    def from_dict(player_dict: Dict[str, str]) -> 'Player':
        player = Player(
            player_dict["last_name"],
            player_dict["first_name"],
            player_dict["birth_date"],
            player_dict["id_chess"],
            uuid.UUID(player_dict["id"])
        )
        player.full_name = f"{player.first_name} {player.last_name}"
        return player

    @property
    def id(self):
        return str(self._id)
