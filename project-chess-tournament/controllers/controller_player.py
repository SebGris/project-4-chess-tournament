import json
import os
from models.player import Player


class ControllerPlayer:
    """Controller for adding players,
    running the tournament and managing results."""

    def __init__(self, view):
        self.players = []
        self.view = view

    def get_players(self):
        """Get some players."""
        counter = 1
        while True:
            last_name, first_name, birth_date, id_chess = \
                self.view.prompt_for_player(counter)
            if not last_name:
                return
            player = Player(last_name, first_name, birth_date, id_chess)
            self.players.append(player)
            # self.save_player(player)
            counter = counter + 1

    def add_players(self, players):
        """Add players to the list."""
        self.players.extend(players)

    def save_players_to_json(self, filename="players.json"):
        """Save players to a JSON file."""
        data_folder = os.path.join(os.getcwd(), 'data/tournaments')
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'w') as file:
            json.dump([player.to_dict() for player in self.players], file, indent=4)
        self.view.show_saving_success()
