from models.round import Round
from repositories.base_repository import BaseRepository


class RoundRepository(BaseRepository):
    """Repository for managing rounds in a chess tournament."""
    FILE_PATH = "rounds.json"

    def __init__(self):
        super().__init__(Round)
