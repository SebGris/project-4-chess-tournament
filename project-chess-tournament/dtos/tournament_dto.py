from dataclasses import dataclass, asdict
from typing import List


@dataclass
class TournamentDTO:
    id: str
    name: str
    location: str
    start_date: str
    end_date: str
    description: str
    total_rounds: int
    player_ids: List[str]
    round_ids: List[str]

    @staticmethod
    def from_dict(tournament_data):
        return TournamentDTO(
            tournament_data["id"],
            tournament_data["name"],
            tournament_data["location"],
            tournament_data["start_date"],
            tournament_data["end_date"],
            tournament_data["description"],
            tournament_data["total_rounds"],
            tournament_data["player_ids"],
            tournament_data["round_ids"]
        )

    def to_dict(self):
        return asdict(self)
