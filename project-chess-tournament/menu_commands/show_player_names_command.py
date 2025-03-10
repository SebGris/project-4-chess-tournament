from commands.command import Command

class ShowPlayerNamesCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.active_tournament:
            players_names = [player.full_name for player in self.tournament_controller.active_tournament.players]
            self.tournament_controller.view.display_tournament_players(players_names)
        else:
            self.tournament_controller.view.display_no_tournament_message()
