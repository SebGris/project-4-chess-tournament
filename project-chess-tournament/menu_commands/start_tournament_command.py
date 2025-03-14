from commands.command import Command
from menu_commands.show_player_pairs_command import ShowPlayerPairsCommand
from controllers.tournament_controller import TournamentController


class StartTournamentCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        active_tournament = self.controller.active_tournament
        if active_tournament:
            if not active_tournament.players:
                self.controller.tournament_view.display_tournament_start_error()
            elif self.__check_if_odd(len(active_tournament.players)):
                self.controller.tournament_view.display_even_players_message()
            else:
                self.controller.start_tournament()
                ShowPlayerPairsCommand(self.controller).execute()
        else:
            self.controller.tournament_view.display_no_tournament_message()

    def __check_if_odd(self, number):
        return number % 2 != 0
