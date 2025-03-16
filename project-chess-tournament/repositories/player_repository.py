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

    def get_player_by_id(self, id):
        players = self.get_players()
        for player in players:
            if player.id == id:
                return player
        return None

    def save_players(self, players: List[PlayerDTO]):
        self.file_service.write_to_file(
            [player.to_dict() for player in players]
        )

    def create_player(self, player: PlayerDTO) -> PlayerDTO:
        players = self.get_players()
        players.append(player)
        self.save_players(players)
        return player

    def create_players(self, new_players: List[PlayerDTO]):
        players = self.get_players()
        players.extend(new_players)
        self.save_players(players)
