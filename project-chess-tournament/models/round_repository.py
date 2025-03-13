import uuid
from models.base_repository import BaseRepository
from models.round import Round
from services.file_service import FileService
from typing import List, Dict, Optional


class RoundRepository(BaseRepository):
    FILE_PATH = "rounds.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_all_rounds(self) -> List[Round]:
        rounds_dict = self.file_service.read_from_file()
        return [Round.from_dict(round) for round in rounds_dict]

    def find_round_by_id(self, round_id: uuid.UUID) -> Optional[Round]:
        rounds = self.get_all_rounds()
        for round in rounds:
            if round.id == round_id:
                return round
        return None

    def create_round(self, round: Round) -> Round:
        rounds = self.get_all_rounds()
        rounds.append(round)
        self.file_service.write_to_file([round.to_dict() for round in rounds])
        return round

    def update_round(self, round_id: uuid.UUID, updated_data: Dict[str, str]) -> Optional[Round]:
        rounds = self.get_all_rounds()
        for round in rounds:
            if round.id == round_id:
                round.last_name = updated_data["last_name"]
                round.first_name = updated_data["first_name"]
                round.birth_date = updated_data["birth_date"]
                round.id_chess = updated_data["id_chess"]
                self.file_service.write_to_file(
                    [round.to_dict() for round in rounds]
                )
                return round
        return None