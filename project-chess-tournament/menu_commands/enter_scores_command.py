from commands.command import Command
from controllers.tournament_controller import TournamentController


class EnterScoresCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.enter_scores()
