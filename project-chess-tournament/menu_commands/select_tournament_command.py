from commands.command import Command
from controllers.tournament_controller import TournamentController


class SelectTournamentCommand(Command):
    def __init__(self, tournament_controller: TournamentController):
        self.tournament_controller = tournament_controller

    def execute(self):
        if not self.tournament_controller.tournaments:
            self.tournament_controller.view.display_no_tournament_message()
            return
        tournament_index = self.tournament_controller.view.get_tournament_selection(
            self.tournament_controller.tournaments
        )
        if 0 <= tournament_index < len(self.tournament_controller.tournaments):
            self.tournament_controller.select_tournament(tournament_index)
            self.tournament_controller.view.display_tournament_selected(
                self.tournament_controller.active_tournament.name
            )
        else:
            self.tournament_controller.view.display_invalid_option_message()
