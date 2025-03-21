from typing import List
from models.tournament import Tournament
from repositories.base_repository import BaseRepository
from services.file_service import FileService


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_tournaments(self):
        return [
            Tournament.from_dict(tournament_dict)
            for tournament_dict in self.file_service.read_from_file()
        ]

    def write_tournaments_to_file(self, tournaments: List[Tournament]):
        self.file_service.write_to_file(
            [tournament.to_dict() for tournament in tournaments]
        )
