import json
import os
from models.player import Player


class PlayerRepository:
    FILE_PATH = "players.json"

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                json.dump([], file)

    def get_all_players(self):
        with open(self.FILE_PATH, "r") as file:
            players_dict = json.load(file)
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
        with open(self.FILE_PATH, "w") as file:
            json.dump(
                [player.to_dict() for player in players],
                file,
                indent=4
            )
        return player

    def update_player(self, player_id, updated_data):
        players = self.get_all_players()
        for player in players:
            if player.id == player_id:
                player.name = updated_data["name"]
                player.age = updated_data["age"]
                with open(self.FILE_PATH, "w") as file:
                    json.dump(
                        [player.to_dict() for player in players],
                        file,
                        indent=4
                    )
                return player
        return None
