class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_all_players(self):
        players = self.model.get_all_players()
        self.view.display_all_players(players)

    def get_player_by_id(self, player_id):
        player = self.model.find_player_by_id(player_id)
        self.view.display_player(player)

    def create_player(self, name, age):
        player_id = len(self.model.get_all_players()) + 1
        player = Player(player_id, name, age)
        created_player = self.model.create_player(player)
        self.view.display_player_created(created_player)

    def update_player(self, player_id, name, age):
        updated_data = {"name": name, "age": age}
        player = self.model.update_player(player_id, updated_data)
        self.view.display_player_updated(player)