from utils.file_utils import get_file_path
from utils.json_file_manager import JsonFileManager

class TournamentFileManager:
    def __init__(self):
        self.tournaments_file_path = get_file_path("tournaments.json")
        self.players_file_path = get_file_path("players.json")

    def save_tournament(self, tournament):
        data = tournament.to_dict()
        JsonFileManager.write(self.tournaments_file_path, data)

    def load_tournament(self):
        return JsonFileManager.read(self.tournaments_file_path)

    def load_all_players(self):
        return JsonFileManager.read(self.players_file_path)

    def save_players(self, players):
        JsonFileManager.write(self.players_file_path, players)
