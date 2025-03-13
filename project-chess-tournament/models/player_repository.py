from models.base_repository import BaseRepository
from models.player import Player
from services.file_service import FileService


class PlayerRepository(BaseRepository):
    FILE_PATH = "players.json"

    def __init__(self):
        self.file_service = FileService(self.get_file_path())

    def get_all_players(self):
        players_dict = self.file_service.read_from_file()
        return [Player.from_dict(player) for player in players_dict]

    def find_player_by_id(self, player_id):
        players = self.get_all_players()
        for player in players:
            if player.id == player_id:
                return player
        return None

    def create_player(self, player):
        players = self.get_all_players()
        players.append(player)
        self.file_service.write_to_file([player.to_dict() for player in players])
        return player

    def update_player(self, player_id, updated_data):
        players = self.get_all_players()
        for player in players:
            if str(player.id) == player_id:
                player.last_name = updated_data["last_name"]
                player.first_name = updated_data["first_name"]
                player.birth_date = updated_data["birth_date"]
                player.id_chess = updated_data["id_chess"]
                self.file_service.write_to_file(
                    [player.to_dict() for player in players]
                )
                return player
        return None
