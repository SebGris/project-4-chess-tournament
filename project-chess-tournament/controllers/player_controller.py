from models.player import Player


class PlayerController:
    def __init__(self, repository, view):
        self.repository = repository
        self.view = view

    def get_all_players(self):
        players = self.repository.get_all_players()
        self.view.display_all_players(players)

    def get_player_by_id(self, player_id):
        player = self.repository.find_player_by_id(player_id)
        self.view.display_player(player)

    def create_player(self, name, age):
        player_id = len(self.repository.get_all_players()) + 1
        player = Player(player_id, name, age)
        created_player = self.repository.create_player(player)
        self.view.display_player_created(created_player)

    def update_player(self, player_id, name, age):
        updated_data = {"name": name, "age": age}
        player = self.repository.update_player(player_id, updated_data)
        self.view.display_player_updated(player)