from models.player import Player
from controllers.base_controller import BaseController
from commands.file_commands import ReadJsonFileCommand, WriteJsonFileCommand


class ControllerPlayer(BaseController):
    """Controller for adding players"""

    def __init__(self, view):
        self.players = []
        self.view = view

    def add_players(self, players=None):
        """Add players to the list."""
        if players is None:
            counter = 1
            while True:
                last_name, first_name, birth_date, id_chess = \
                    self.view.prompt_for_player(counter)
                if not last_name:
                    return
                player = Player(
                    last_name, first_name, birth_date, id_chess
                )
                self.players.append(player)
                counter = counter + 1
        else:
            self.players.extend(players)

    def display_players(self):
        """Display the players."""
        self.view.display_players(self.players)

    def save_players_to_json(self):
        """Save players to a JSON file."""
        write_command = WriteJsonFileCommand(
            self.players_file_path,
            [player.to_dict() for player in self.players]
        )
        write_command.execute()
        self.view.show_saving_success()

    def load_players_from_json(self):
        read_command = ReadJsonFileCommand(self.players_file_path)
        data = read_command.execute()
        self.players = [Player.from_dict(player_data) for player_data in data]
        self.view.display_message("Joueurs chargés avec succès !")
