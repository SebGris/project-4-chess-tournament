from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateNumberOfRoundsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.update_number_of_rounds()
