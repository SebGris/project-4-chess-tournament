from models.player import Player
from repositories.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, player_repository: PlayerRepository, view: PlayerView):
        self.player_repository = player_repository
        self.view = view
        self.added_players = []

    def add_players(self):
        self.added_players.clear()
        players_data = []
        while player_data := self.view.get_player_data():
            players_data.append(player_data)
        self._create_and_add_players(players_data)
        return self.added_players

    def _create_and_add_players(self, players_data):
        for player_data in players_data:
            player = Player(**player_data)
            self.added_players.append(player)
            self.view.display_add_player_message(player)
        self.player_repository.save(self.added_players)

    def report_players(self):
        players: list[Player] = self.player_repository.get_all()
        players.sort(key=lambda player: player.last_name)
        # Convert the list of players to a list of dictionaries
        players = [player.to_dict() for player in players]
        self.view.report_players(players)
