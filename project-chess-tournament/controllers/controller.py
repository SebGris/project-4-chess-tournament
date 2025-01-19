from models.player import Player


class Controller:
    def __init__(self, view):
        self.players = []
        self.view = view
    
    def get_players(self):
        """Get some players."""
        while len(self.players) < 2:  # nombre magique
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)
    
    def run(self):
        """Run the game."""
        self.get_players()
