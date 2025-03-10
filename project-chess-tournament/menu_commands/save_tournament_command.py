from commands.command import Command
from services.json_file_service import JsonFileService, tournaments_file_path

class SaveTournamentCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.tournaments:
            data = [tournament.to_dict() for tournament in self.tournament_controller.tournaments]
            filename = tournaments_file_path()
            JsonFileService.save_to_file(data, filename)
            self.tournament_controller.view.display_save_success_message(filename)
        else:
            self.tournament_controller.view.display_no_tournament_message()
