from models.tournament import Tournament
from repositories.base_repository import BaseRepository


class TournamentRepository(BaseRepository):
    """Repository for managing tournaments."""
    FILE_PATH = "tournaments.json"

    def __init__(self):
        super().__init__(Tournament)
