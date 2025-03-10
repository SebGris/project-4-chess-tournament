from commands.command import Command

class CreateTournamentCommand(Command):
    """Command to create a new tournament without players."""
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        tournament_info = self.collect_tournament_info()
        self.tournament_controller.create_tournament(**tournament_info)
        self.tournament_controller.view.display_new_tournament_created(tournament_info['name'])

    def collect_tournament_info(self):
        name = self.tournament_controller.view.get_tournament_name()
        location = self.tournament_controller.view.get_tournament_location()
        start_date = self.tournament_controller.view.get_tournament_start_date()
        end_date = self.tournament_controller.view.get_tournament_end_date()
        number_of_rounds = self.tournament_controller.view.get_tournament_number_of_rounds()
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rounds": number_of_rounds,
        }
