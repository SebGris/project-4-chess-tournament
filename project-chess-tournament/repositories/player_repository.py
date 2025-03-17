from dtos.player_dto import PlayerDTO
from repositories.base_repository import BaseRepository
from services.file_service import FileService
from typing import List


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_players(self):
        return [
            PlayerDTO.from_dict(player_dict)
            for player_dict in self.file_service.read_from_file()
        ]

    def get_player_by_id(self, id: str):
        return next((ply for ply in self.get_players() if ply.id == id), None)

    def get_players_by_ids(self, ids: List[str]):
        return [player for player in self.get_players() if player.id in ids]

    def write_players_to_file(self, players: List[PlayerDTO]):
        self.file_service.write_to_file(
            [player.to_dict() for player in players]
        )

    def save(self, new_players: List[PlayerDTO]):
        players = self.get_players()
        players.extend(new_players)
        self.write_players_to_file(players)
