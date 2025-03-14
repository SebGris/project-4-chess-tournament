from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateNumberOfRoundsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if self.controller.active_tournament:
            new_number_of_rounds = (
                self.controller.view.get_tournament_number_of_rounds()
            )
            self.controller.update_number_of_rounds(new_number_of_rounds)
            self.controller.view.display_updated_number_rounds_message(
                new_number_of_rounds
            )
        else:
            self.controller.view.display_no_tournament_message()
