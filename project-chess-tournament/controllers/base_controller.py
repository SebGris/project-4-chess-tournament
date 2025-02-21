from utils.file_utils import get_file_path


class BaseController:
    """Base class for controllers."""
    def __init__(self):
        self.players_file_path = get_file_path("players.json")
        self.tournament_file_path = get_file_path("tournament.json")
