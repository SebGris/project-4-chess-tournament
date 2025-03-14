from commands.command import Command
from controllers.tournament_controller import TournamentController


class CreateTournamentCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        tournament_info = self.collect_tournament_info()
        self.controller.create_tournament(**tournament_info)
        self.controller.view.display_new_tournament_created(tournament_info["name"])

    def collect_tournament_info(self):
        name = self.controller.view.get_tournament_name()
        location = self.controller.view.get_tournament_location()
        start_date = self.controller.view.get_tournament_start_date()
        end_date = self.controller.view.get_tournament_end_date()
        number_of_rounds = self.controller.view.get_tournament_number_of_rounds()
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rounds": number_of_rounds,
        }
