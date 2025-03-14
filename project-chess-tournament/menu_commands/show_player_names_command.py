from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowPlayerNamesCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if self.controller.active_tournament:
            players_names = [
                player.full_name for player in self.controller.active_tournament.players
            ]
            self.controller.view.display_tournament_players(players_names)
        else:
            self.controller.view.display_no_tournament_message()
