from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateNumberOfRoundsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if self.controller.active_tournament:
            new_number_of_rounds = (
                self.controller.tournament_view.get_number_of_rounds()
            )
            self.controller.update_number_of_rounds(new_number_of_rounds)
            self.controller.tournament_view.display_updated_number_rounds_message(
                new_number_of_rounds
            )
        else:
            self.controller.tournament_view.display_no_tournament_message()
