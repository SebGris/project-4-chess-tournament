from typing import List
from dtos.round_dto import RoundDTO
from repositories.base_repository import BaseRepository
from services.file_service import FileService


class RoundRepository(BaseRepository):
    FILE_PATH = "rounds.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_rounds(self):
        return [
            RoundDTO.from_dict(round_dict)
            for round_dict in self.file_service.read_from_file()
        ]

    def get_round_by_id(self, id: str):
        return next((r for r in self.get_rounds() if r.id == id), None)

    def get_rounds_by_ids(self, ids: List[str]):
        return [round for round in self.get_rounds() if round.id in ids]

    def write_rounds_to_file(self, rounds: List[RoundDTO]):
        self.file_service.write_to_file(
            [round.to_dict() for round in rounds]
        )

    def create(self, new_round: RoundDTO):
        rounds = self.get_rounds()
        rounds.append(new_round)
        self.write_rounds_to_file(rounds)

    def save(self, updated_round: RoundDTO):
        old_rounds = self.get_rounds()
        # deletes the round in rounds that has the same id as updated_round
        rounds = [r for r in old_rounds if r.id != updated_round.id]
        rounds.append(updated_round)
        self.write_rounds_to_file(rounds)
