import uuid
from models.tournament import Tournament
from models.base_repository import BaseRepository
from services.file_service import FileService
from typing import List, Dict, Optional


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self, player_repository):
        super().__init__()
        self.file_service = FileService(self.get_file_path())
        self.player_repository = player_repository

    def get_all_tournaments(self) -> List[Tournament]:
        tournaments_dict = self.file_service.read_from_file()
        all_players = {player.id: player for player in self.player_repository.get_all_players()}
        tournaments = []
        for tournament_dict in tournaments_dict:
            tournament = Tournament.from_dict(tournament_dict)
            players = [all_players[player_id] for player_id in tournament_dict["player_ids"] if player_id in all_players]
            tournament.add_players(players)
            tournaments.append(tournament)
        return tournaments

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

    def update_tournament(
        self, id: uuid.UUID, data: Dict[str, str]
    ) -> Optional[Tournament]:
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == id:
                tournament.name = data["name"]
                self.file_service.write_to_file(
                    [tournament.to_dict() for tournament in tournaments]
                )
                return tournament
        return None
