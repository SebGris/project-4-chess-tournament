from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowTournamentDetailsCommand(Command):
    def __init__(self, tournament_controller: TournamentController):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.tournaments:
            tournament = self.tournament_controller.active_tournament
            tournament_dic = {
                "name": tournament.name,
                "location": tournament.location,
                "start_date": tournament.start_date,
                "end_date": tournament.end_date,
                "description": tournament.description,
                "number_of_rounds": tournament.number_of_rounds,
            }
            self.tournament_controller.view.display_tournament_details(tournament_dic)
        else:
            self.tournament_controller.view.display_no_tournament_message()
