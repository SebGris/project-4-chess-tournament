from dataclasses import dataclass, asdict


@dataclass
class PlayerDTO:
    id: str
    last_name: str
    first_name: str
    birth_date: str
    chess_id: str

    @classmethod
    def from_dict(cls, player_data):
        return cls(**player_data)

    def to_dict(self):
        return asdict(self)
