from models.player import Player
from models.players import Players


class ControllerPlayer:
    def __init__(self, view):
        self.players = Players()
        self.view = view
    
    def get_players(self):
        """Get some players."""
        while True:
            (last_name, first_name, date_of_birth) = self.view.prompt_for_player()
            if not last_name:
                return
            self.players.append(Player(last_name, first_name, date_of_birth))

    def display_players(self):
        """Display players."""
        self.view.display_players(self.players.get_data())

    def save_players(self):
        """Save players in JSON."""
        pass

    def add_players(self):
        """Run."""
        self.get_players()
        self.display_players()
        if self.view.save_players() is True:
            if self.save_players() is True:
                 self.view.show_saving_success()

    