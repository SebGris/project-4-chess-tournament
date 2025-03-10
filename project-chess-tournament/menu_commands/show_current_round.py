from commands.command import Command

class ShowCurrentRound(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        current_round = self.tournament_controller.active_tournament.get_current_round()
        if current_round:
            round = {
                "name": current_round.name,
                "start_date": current_round.start_datetime,
                "end_date": current_round.end_datetime
            }
            self.tournament_controller.view.display_round_info(round)
            round_no = {
                "current_round": self.tournament_controller.active_tournament.current_round,
                "number_of_rounds": self.tournament_controller.active_tournament.number_of_rounds
            }
            self.tournament_controller.view.display_current_round_no(round_no)
        else:
            self.tournament_controller.view.display_no_round_message()