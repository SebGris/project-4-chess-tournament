from models.round import Round
from repositories.base_repository import BaseRepository


class RoundRepository(BaseRepository):
    FILE_PATH = "rounds.json"

    def __init__(self):
        super().__init__(Round)
