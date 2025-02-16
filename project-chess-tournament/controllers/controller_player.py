from models.player import Player
from utils.file_utils import save_to_json, load_from_json


class ControllerPlayer:
    """Controller for adding players"""
    PLAYERS_FILENAME = "players.json"

    def __init__(self, view):
        self.players = []
        self.view = view

    def get_players(self):
        """Get some players."""
        counter = 1
        while True:
            last_name, first_name, birth_date, id_chess, id = \
                self.view.prompt_for_player(counter)
            if not last_name:
                return
            player = Player(last_name, first_name, birth_date, id_chess, id)
            self.players.append(player)
            counter = counter + 1

    def add_players(self, players):
        """Add players to the list."""
        self.players.extend(players)

    def display_players(self):
        """Display the players."""
        self.view.display_players(self.players)

    def save_players_to_json(self):
        """Save players to a JSON file."""
        save_to_json(
            [player.to_dict() for player in self.players],
            self.PLAYERS_FILENAME
        )
        self.view.show_saving_success()

    def load_players_from_json(self):
        data = load_from_json(self.PLAYERS_FILENAME)
        self.players = [Player.from_dict(player_data) for player_data in data]
        self.view.display_message("Joueurs chargés avec succès !")
