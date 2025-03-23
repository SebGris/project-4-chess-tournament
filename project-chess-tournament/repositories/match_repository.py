from models.match import Match
from repositories.base_repository import BaseRepository


class MatchRepository(BaseRepository):
    FILE_PATH = "matches.json"

    def __init__(self):
        super().__init__(Match)
