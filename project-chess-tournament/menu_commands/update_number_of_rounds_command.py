from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateNumberOfRoundsCommand(Command):
    def __init__(self, tournament_controller: TournamentController):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.active_tournament:
            new_number_of_rounds = (
                self.tournament_controller.view.get_tournament_number_of_rounds()
            )
            self.tournament_controller.update_number_of_rounds(new_number_of_rounds)
            self.tournament_controller.view.display_updated_number_rounds_message(
                new_number_of_rounds
            )
        else:
            self.tournament_controller.view.display_no_tournament_message()
