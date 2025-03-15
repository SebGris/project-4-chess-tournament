import uuid
from models.base_repository import BaseRepository
from models.match import Match
from services.file_service import FileService
from typing import List, Dict, Optional


class MatchRepository(BaseRepository):
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_all_matches(self) -> List[Match]:
        matches_dict = self.file_service.read_from_file()
        return [Match.from_dict(match) for match in matches_dict]

    def find_match_by_id(self, match_id: uuid.UUID) -> Optional[Match]:
        matches = self.get_all_matches()
        for match in matches:
            if match.id == match_id:
                return match
        return None

    def create_match(self, match: Match) -> Match:
        matches = self.get_all_matches()
        matches.append(match)
        self.file_service.write_to_file([match.to_dict() for match in matches])
        return match

    def update_match(
        self, match_id: uuid.UUID, updated_data: Dict[str, str]
    ) -> Optional[Match]:
        matches = self.get_all_matches()
        for match in matches:
            if match.id == match_id:
                match.last_name = updated_data["last_name"]
                match.first_name = updated_data["first_name"]
                match.birth_date = updated_data["birth_date"]
                match.id_chess = updated_data["id_chess"]
                self.file_service.write_to_file([match.to_dict() for match in matches])
                return match
        return None
