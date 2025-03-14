from commands.command import Command
from controllers.tournament_controller import TournamentController


class ShowPlayerPairsCommand(Command):
    def __init__(self, controller: TournamentController):
        self.controller = controller

    def execute(self):
        if self.controller.active_tournament:
            try:
                current_round = self.controller.active_tournament.get_current_round()
                round_name, pairs = current_round.get_pairs_players()
                self.controller.view.display_player_pairs(round_name, pairs)
            except Exception:
                self.controller.view.display_no_round_message()
        else:
            self.controller.view.display_no_tournament_message()
