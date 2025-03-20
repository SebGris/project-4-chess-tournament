from typing import List
from models.match import Match
from repositories.base_repository import BaseRepository
from services.file_service import FileService


class MatchRepository(BaseRepository):
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_matches(self):
        return [
            Match.from_dict(match_dic)
            for match_dic in self.file_service.read_from_file()
        ]

    def get_match_by_id(self, id: str):
        return next((m for m in self.get_matches() if m.id == id), None)

    def get_matches_by_ids(self, ids: List[str]):
        return [match for match in self.get_matches() if match.id in ids]

    def write_matches_to_file(self, matches: List[Match]):
        self.file_service.write_to_file([match.to_dict() for match in matches])

    def create(self, new_match: Match):
        matches = self.get_matches()
        matches.append(new_match)
        self.write_matches_to_file(matches)

    def save(self, updated_match: Match):
        self.save_a_list([updated_match])

    def save_a_list(self, updated_matches: List[Match]):
        old_matches = self.get_matches()
        # deletes matches with the same identifier as those in updated_matches
        matches = [
            o for o in old_matches if o.id not in [u.id for u in updated_matches]
        ]
        matches.extend(updated_matches)
        self.write_matches_to_file(matches)
