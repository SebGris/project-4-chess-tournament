from commands.command import Command


class AddPlayersCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        while True:
            player_data = self.tournament_controller.view.get_player_data()
            if player_data:
                player_id = self.tournament_controller.add_player(player_data)
                player_data["id"] = player_id
                full_name = f"{player_data['first_name']} {player_data['last_name']}"
                self.tournament_controller.view.display_add_player_message(full_name)
                existing_players = self.tournament_controller.load_players_data()
                existing_players.append(player_data)
                self.tournament_controller.save_players_data(existing_players)
            else:
                break
