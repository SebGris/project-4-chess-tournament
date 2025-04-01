from models.match import Match
from repositories.base_repository import BaseRepository


class MatchRepository(BaseRepository):
    """Repository for managing Match objects in a JSON file."""
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__(Match)
