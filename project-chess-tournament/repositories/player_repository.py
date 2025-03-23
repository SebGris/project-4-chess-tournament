from models.player import Player
from repositories.base_repository import BaseRepository


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        super().__init__(Player)
