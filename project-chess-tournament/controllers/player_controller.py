import uuid
from models.player import Player
from repositories.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, repository: PlayerRepository, view: PlayerView):
        self.repository = repository
        self.view = view

    def add_players(self):
        players_data = []
        while player_data := self.view.get_player_data():
            players_data.append(player_data)
        self.create_players(players_data)

    def create_players(self, players_data):
        players = []
        for player_data in players_data:
            player = self._create_player_instance(**player_data)
            players.append(player)
            self.view.display_add_player_message(player)
        self.repository.create_players(players)

    def display_players_name(self, players):
        self.view.display_players_name(players)

    def display_players(self, players):
        self.view.display_players(players)

    def _create_player_instance(self, last_name, first_name, birth_date, id_chess):
        player_id = uuid.uuid4()
        player = Player(last_name, first_name, birth_date, id_chess, player_id)
        return player
