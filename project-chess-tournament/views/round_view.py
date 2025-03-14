from models.round import Round
from views.base_view import BaseView


class TournamentView(BaseView):
    def display_round_info(self, round: Round):
        """Display information about a round."""
        round_name = round.name
        if round_name == "Round 1":
            print("--- Liste des rounds ---")
        print(f"--- {round_name} ---")
        if round["start_date"]:
            print(f"Date de début : {round.start_date}")
        print(f"Date de fin : {round.end_date or 'round en cours'}")
