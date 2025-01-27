from models.player import Player


class ControllerPlayer:
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
            self.save_player(player)
            counter = counter + 1

    def save_player(self, players):
        """Save players in JSON."""
        self.view.show_saving_success()
        pass

    def add_players_to_json(self):
        """Add players."""
        self.get_players()
        self.view.display_players(self.players)
