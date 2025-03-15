from models.round import Round
from views.base_view import BaseView


class RoundView(BaseView):
    def display_round_info(self, round: Round):
        """Display information about a round."""
        round_name = round.name
        if round_name == "Round 1":
            print("--- Liste des rounds ---")
        print(f"--- {round_name} ---")
        if round.start_date:
            print(f"Date de début : {round.start_date}")
            print(f"Date de fin : {round.end_date or 'round en cours'}")

    def display_player_pairs(self, round_name, pairs):
        """Display pairs of players for a round."""
        print(f"{round_name} avec les paires suivantes :")
        for index, pair in enumerate(pairs, start=1):
            if len(pair) == 2:
                print(f"{index}. {pair[0]} vs {pair[1]}")
            else:
                print(f"{index}. {pair[0]} score {pair[2]} vs {pair[1]} score {pair[3]}")
