from commands.command import Command
from controllers.round_controller import RoundController


class CreateRoundCommand(Command):
    def __init__(self, nom, matchs):
        self.nom = nom
        self.matchs = matchs

    def execute(self):
        return RoundController.create_round(self.nom, self.matchs)
