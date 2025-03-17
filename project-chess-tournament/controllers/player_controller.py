from models.player import Player
from repositories.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, repository: PlayerRepository, view: PlayerView):
        self.repository = repository
        self.view = view
        self.added_players = []

    def get_players_from_repository(self):
        return self.repository.get_players()

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
        self.repository.save(self.added_players)
