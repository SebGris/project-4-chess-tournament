from commands.command import Command

class ShowPlayerPairsCommand(Command):
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller

    def execute(self):
        if self.tournament_controller.active_tournament:
            try:
                current_round = self.tournament_controller.active_tournament.get_current_round()
                round_name, pairs = current_round.get_pairs_players()
                self.tournament_controller.view.display_player_pairs(round_name, pairs)
            except Exception as e:
                self.tournament_controller.view.display_no_round_message()
        else:
            self.tournament_controller.view.display_no_tournament_message()
