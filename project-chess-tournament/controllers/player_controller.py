from models.player import Player
from repositories.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    """Controller for managing players in the chess tournament application."""
    def __init__(self, player_repository: PlayerRepository, view: PlayerView):
        """Initializes the PlayerController with the player repository and view."""
        self.player_repository = player_repository
        self.view = view

    def add_players(self):
        """Adds players to the tournament."""
        # iter : l'itération s'arrête lorsque la fonction retourne la valeur
        # de sentinelle
        self.view.display_add_player_message()
        added_players = [
            Player(**player_data)
            for player_data in iter(self.view.get_player_data, None)
        ]
        for player in added_players:
            self.view.display_player_success_message(player)
        self.player_repository.save(added_players)

    def report_players(self):
        """Reports the list of players."""
        players: list[Player] = sorted(
            self.player_repository.get_all(),
            key=lambda player: player.last_name
        )
        self.view.report_players([player.to_dict() for player in players])
