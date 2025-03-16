from dataclasses import dataclass, asdict


@dataclass
class MatchDTO:
    id: str
    player1: str
    player2: str
    player1_score: str
    player2_score: str

    @classmethod
    def from_dict(cls, match_data):
        return cls(**match_data)

    def to_dict(self):
        return asdict(self)
