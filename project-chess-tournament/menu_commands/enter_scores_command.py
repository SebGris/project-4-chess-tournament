from commands.command import Command
from controllers.tournament_controller import TournamentController


class EnterScoresCommand(Command):
    def __init__(self, tournament_controller: TournamentController):
        self.tournament_controller = tournament_controller

    def execute(self):
        self.tournament_controller.enter_scores()
