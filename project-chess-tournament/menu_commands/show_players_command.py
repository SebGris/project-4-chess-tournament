from commands.command import Command

class ShowPlayersCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.active_tournament:
            players = self.tournament_controller.get_players()
            self.tournament_controller.view.display_players(players)
        else:
            self.tournament_controller.view.display_no_tournament_message()
