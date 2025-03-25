from models.player import Player
from repositories.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, player_repository: PlayerRepository, view: PlayerView):
        self.player_repository = player_repository
        self.view = view

    def add_players(self):
        # iter : l'itération s'arrête lorsque la fonction retourne la valeur
        # de sentinelle
        added_players = [
            Player(**player_data)
            for player_data in iter(self.view.get_player_data, None)
        ]
        for player in added_players:
            self.view.display_add_player_message(player)
        self.player_repository.save(added_players)

    def report_players(self):
        players: list[Player] = sorted(
            self.player_repository.get_all(),
            key=lambda player: player.last_name
        )
        self.view.report_players([player.to_dict() for player in players])
