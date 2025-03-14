from commands.command import Command
from controllers.tournament_controller import TournamentController


class SelectTournamentCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if not self.controller.tournaments:
            self.controller.view.display_no_tournament_message()
            return
        tournament_index = self.controller.view.get_tournament_selection(
            self.controller.tournaments
        )
        if 0 <= tournament_index < len(self.controller.tournaments):
            self.controller.select_tournament(tournament_index)
            self.controller.view.display_tournament_selected(
                self.controller.active_tournament.name
            )
        else:
            self.controller.view.display_invalid_option_message()
