from dataclasses import dataclass, asdict
from typing import List


@dataclass
class RoundDTO:
    id: str
    name: str
    match_ids: List[str]
    start_datetime: str
    end_datetime: str

    @classmethod
    def from_dict(cls, round_data):
        return cls(**round_data)

    def to_dict(self):
        return asdict(self)
