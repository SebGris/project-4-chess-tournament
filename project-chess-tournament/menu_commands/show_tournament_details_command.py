from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowTournamentDetailsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.display_active_tournament()
