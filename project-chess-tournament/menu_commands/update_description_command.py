from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateDescriptionCommand(Command):
    def __init__(self, tournament_controller: TournamentController):
        self.tournament_controller = tournament_controller

    def execute(self):
        description = self.tournament_controller.view.get_tournament_description()
        self.tournament_controller.update_description(description)
        self.tournament_controller.view.display_successful_description_message()
