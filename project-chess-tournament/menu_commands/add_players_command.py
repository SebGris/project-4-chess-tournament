from commands.command import Command
from controllers.tournament_controller import TournamentController


class AddPlayersCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        while True:
            player_data = self.controller.view.get_player_data()
            if player_data:
                player_id = self.controller.add_player(player_data)
                player_data["id"] = player_id
                full_name = f"{player_data['first_name']} {player_data['last_name']}"
                self.controller.view.display_add_player_message(full_name)
                existing_players = self.controller.load_players_data()
                existing_players.append(player_data)
                self.controller.save_players_data(existing_players)
            else:
                break
