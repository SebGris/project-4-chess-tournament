from dtos.match_dto import MatchDTO
from repositories.base_repository import BaseRepository
from services.file_service import FileService
from typing import List


class MatchRepository(BaseRepository):
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_matches(self):
        return [
            MatchDTO.from_dict(match_dic)
            for match_dic in self.file_service.read_from_file()
        ]

    def get_match_by_id(self, id: str):
        return next((m for m in self.get_matches() if m.id == id), None)

    def get_matches_by_ids(self, ids: List[str]):
        return [match for match in self.get_matches() if match.id in ids]

    def write_matches_to_file(self, matches: List[MatchDTO]):
        self.file_service.write_to_file(
            [match.to_dict() for match in matches]
        )

    def create_match(self, match: MatchDTO) -> MatchDTO:
        matches = self.get_matches()
        matches.append(match)
        self.write_matches_to_file(matches)
        return match

    def save(self, new_matches: List[MatchDTO]):
        matches = self.get_matches()
        matches.extend(new_matches)
        self.write_matches_to_file(matches)
