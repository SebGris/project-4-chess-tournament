import uuid
from models.tournament import Tournament
from models.base_repository import BaseRepository
from services.file_service import FileService
from typing import List, Dict, Optional


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_all_tournaments(self) -> List[Tournament]:
        tournaments_dict = self.file_service.read_from_file()
        return [Tournament.from_dict(tournament) for tournament in tournaments_dict]

    def find_tournament_by_id(self, tournament_id):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def create_tournament(self, tournament: Tournament) -> Tournament:
        tournaments = self.get_all_tournaments()
        tournaments.append(tournament)
        self.file_service.write_to_file(
            [tournament.to_dict() for tournament in tournaments]
        )
        return tournament

    def update_tournament(self, tournament_id: uuid.UUID, updated_data: Dict[str, str]) -> Optional[Tournament]:
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                tournament.name = updated_data["name"]
                tournament.date = updated_data["date"]
                self.file_service.write_to_file(
                    [tournament.to_dict() for tournament in tournaments]
                )
                return tournament
        return None
