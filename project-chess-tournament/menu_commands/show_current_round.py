from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowCurrentRound(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        try:
            current_round = self.controller.active_tournament.get_current_round()
            if current_round:
                round = {
                    "name": current_round.name,
                    "start_date": current_round.start_datetime,
                    "end_date": current_round.end_datetime,
                }
                self.controller.view.display_round_info(round)
                round_no = {
                    "current_round": self.controller.active_tournament.current_round,
                    "number_of_rounds": self.controller.active_tournament.number_of_rounds,
                }
                self.controller.view.display_current_round_no(round_no)
            else:
                self.controller.view.display_no_round_message()
        except IndexError:
            self.controller.view.display_no_tournament_message()
