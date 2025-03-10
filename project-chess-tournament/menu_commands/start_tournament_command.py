from commands.command import Command
from menu_commands.save_tournament_command import SaveTournamentCommand
from menu_commands.show_player_pairs_command import ShowPlayerPairsCommand

class StartTournamentCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        active_tournament = self.tournament_controller.active_tournament
        if active_tournament:
            if not active_tournament.players:
                self.tournament_controller.view.display_tournament_start_error()
            elif self.__check_if_odd(len(active_tournament.players)):
                self.tournament_controller.view.display_even_players_message()
            else:
                self.tournament_controller.start_tournament()
                SaveTournamentCommand(self.tournament_controller).execute()
                ShowPlayerPairsCommand(self.tournament_controller).execute()
        else:
            self.tournament_controller.view.display_no_tournament_message()
    
    def __check_if_odd(self, number):
        return number % 2 != 0