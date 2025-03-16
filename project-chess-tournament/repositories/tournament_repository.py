from models.tournament import Tournament
from repositories.base_repository import BaseRepository
from services.file_service import FileService
from typing import List


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def __init__(self, player_repository):
        super().__init__()
        self.file_service = FileService(self.get_file_path())
        self.player_repository = player_repository

    def get_tournaments(self) -> List[Tournament]:
        tournaments_dict = self.file_service.read_from_file()
        all_players = {player.id: player for player in self.player_repository.get_players()}
        tournaments = []
        for tournament_dict in tournaments_dict:
            tournament = Tournament.from_dict(tournament_dict)
            players = [all_players[player_id] for player_id in tournament_dict["player_ids"] if player_id in all_players]
            tournament.add_players(players)
            tournaments.append(tournament)
        return tournaments

    def save_tournaments(self, tournaments: List[Tournament]):
        tournaments_dict = [tournament.to_dict() for tournament in tournaments]
        self.file_service.write_to_file(tournaments_dict)
