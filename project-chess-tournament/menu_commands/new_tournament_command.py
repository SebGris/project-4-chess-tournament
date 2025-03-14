from commands.command import Command
from controllers.tournament_controller import TournamentController


class NewTournamentCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.create_new_tournament()
