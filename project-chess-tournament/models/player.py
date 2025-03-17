import uuid
from datetime import datetime
from typing import Optional
from dtos.player_dto import PlayerDTO


class Player:
    def __init__(self, last_name, first_name, birth_date, chess_id,
                 player_id=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = 0.0
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

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dto(player_dto: PlayerDTO):
        return Player(
            player_dto.last_name,
            player_dto.first_name,
            player_dto.birth_date,
            player_dto.chess_id,
            uuid.UUID(player_dto.id)
        )

    def to_dto(self):
        return PlayerDTO(
            self.id,
            self.last_name,
            self.first_name,
            self.birth_date,
            self.chess_id
        )
