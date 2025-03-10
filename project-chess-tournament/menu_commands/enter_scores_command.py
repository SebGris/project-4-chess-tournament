from commands.command import Command

class EnterScoresCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller
    
    def execute(self):
        self.tournament_controller.enter_scores()