from models.base_repository import BaseRepository
from models.round import Round
from services.file_service import FileService
from typing import List


class RoundRepository(BaseRepository):
    FILE_PATH = "rounds.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_all_rounds(self) -> List[Round]:
        rounds_dict = self.file_service.read_from_file()
        return [Round.from_dict(round) for round in rounds_dict]

    def create_round(self, round: Round) -> Round:
        rounds = self.get_all_rounds()
        rounds.append(round)
        self.file_service.write_to_file([round.to_dict() for round in rounds])
        return round
