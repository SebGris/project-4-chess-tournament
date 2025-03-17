from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowCurrentRound(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.display_current_round_info()
