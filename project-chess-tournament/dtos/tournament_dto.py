from dataclasses import dataclass
from typing import List


@dataclass
class TournamentDTO:
    id: str
    name: str
    location: str
    start_date: str
    end_date: str
    description: str
    number_of_rounds: int
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
            tournament_data["number_of_rounds"],
            tournament_data["player_ids"],
            tournament_data["round_ids"]
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "player_ids": self.player_ids,
            "round_ids": self.round_ids
        }
