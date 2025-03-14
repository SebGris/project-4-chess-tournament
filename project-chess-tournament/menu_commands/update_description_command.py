from commands.command import Command
from controllers.tournament_controller import TournamentController


class UpdateDescriptionCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        description = self.controller.tournament_view.get_tournament_description()
        self.controller.update_description(description)
        self.controller.tournament_view.display_successful_description_message()
