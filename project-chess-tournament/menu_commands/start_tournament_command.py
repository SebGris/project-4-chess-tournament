from commands.command import Command
from menu_commands.show_player_pairs_command import ShowPlayerPairsCommand
from controllers.tournament_controller import TournamentController


class StartTournamentCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        self.controller.start_tournament()
        ShowPlayerPairsCommand(self.controller).execute()
