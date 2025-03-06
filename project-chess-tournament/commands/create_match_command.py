from commands.command import Command
from controllers.match_controller import MatchController


class CreateMatchCommand(Command):
    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def execute(self):
        return MatchController.create_match(
            self.player1, self.player2, self.player1_score, self.player2_score
        )
