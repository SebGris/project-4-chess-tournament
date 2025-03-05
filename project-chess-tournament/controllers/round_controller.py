from models.round import Round
from commands.tournament_commands import SaveTournamentCommand
from controllers.pairing import Pairing


class RoundController:
    """Ne respecte pas le principe DIP : Dependency Inversion Principle
    Voir https://techblog.deepki.com/SOLID-in-python/"""
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view

    def add_round(self):
        round_name = f"Round {len(self.tournament.rounds) + 1}"
        new_round = Round(round_name)
        previous_matches = {
            (match.player1.id, match.player2.id)
            for round in self.tournament.rounds
            for match in round.matches
        }
        if len(self.tournament.rounds) == 0:
            print("First round")
            pairs = Pairing.generate_first_round_pairs(self.tournament.players)
        else:
            print("Next round")
            pairs = Pairing.generate_next_round_pairs(
                self.tournament.players, previous_matches)
            print(pairs)
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.tournament.rounds.append(new_round)
        save_command = SaveTournamentCommand(self.tournament)
        save_message = save_command.execute()
        self.view.display_message(save_message)
        self.view.display_message(f"{round_name} ajouté")
