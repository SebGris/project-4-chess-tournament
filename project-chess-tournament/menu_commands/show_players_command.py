from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowPlayersCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if self.controller.active_tournament:
            players = self.controller.get_players()
            self.controller.view.display_players(players)
        else:
            self.controller.view.display_no_tournament_message()
