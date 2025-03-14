from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowTournamentDetailsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        tournament = self.controller.active_tournament
        tournament_dic = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "description": tournament.description,
            "number_of_rounds": tournament.number_of_rounds,
        }
        self.controller.tournament_view.display_tournament_details(tournament_dic)
