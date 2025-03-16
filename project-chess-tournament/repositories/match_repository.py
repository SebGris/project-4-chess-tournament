from models.base_repository import BaseRepository
from models.match import Match
from services.file_service import FileService
from typing import List


class MatchRepository(BaseRepository):
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_all_matches(self) -> List[Match]:
        matches_dict = self.file_service.read_from_file()
        return [Match.from_dict(match) for match in matches_dict]

    def create_match(self, match: Match) -> Match:
        matches = self.get_all_matches()
        matches.append(match)
        self.file_service.write_to_file([match.to_dict() for match in matches])
        return match
