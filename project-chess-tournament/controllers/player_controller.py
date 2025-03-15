import uuid
from models.player import Player
from models.player_repository import PlayerRepository
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, repository: PlayerRepository, view: PlayerView):
        self.repository = repository
        self.view = view

    def get_all_players(self):
        players = self.repository.get_all_players()
        self.view.display_all_players(players)

    def get_player_by_id(self, player_id: uuid.UUID):
        player = self.repository.find_player_by_id(player_id)
        self.view.display_player(player)

    def create_player(self, last_name: str, first_name: str, birth_date: str, id_chess: str):
        player_id = uuid.uuid4()
        player = Player(player_id, last_name, first_name, birth_date, id_chess)
        self.repository.create_player(player)
        self.view.display_player_created(player)

    def update_player(self, player_id: uuid.UUID, last_name: str, first_name: str, birth_date: str, id_chess: str):
        updated_data = {"last_name": last_name, "first_name": first_name, "birth_date": birth_date, "id_chess": id_chess}
        player = self.repository.update_player(player_id, updated_data)
        self.view.display_player_updated(player)

    def display_tournament_players(self, players_names):
        self.view.display_tournament_players(players_names)

    def display_players(self, players):
        self.view.display_players(players)
