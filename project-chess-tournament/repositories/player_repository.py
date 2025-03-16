from models.player import Player
from repositories.base_repository import BaseRepository
from services.file_service import FileService
from typing import List


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        super().__init__()
        self.file_service = FileService(self.get_file_path())

    def get_players(self) -> List[Player]:
        players_dict = self.file_service.read_from_file()
        return [Player.from_dict(player) for player in players_dict]

    def save_players(self, players: List[Player]):
        self.file_service.write_to_file([player.to_dict() for player in players])

    def create_player(self, player: Player) -> Player:
        players = self.get_players()
        players.append(player)
        self.save_players(players)
        return player

    def create_players(self, new_players: List[Player]):
        players = self.get_players()
        players.extend(new_players)
        self.save_players(players)
