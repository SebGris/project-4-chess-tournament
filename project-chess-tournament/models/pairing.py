import random


class Pairing:
    """Management of the generation of pairs of players for each round."""

    @staticmethod
    def generate_first_round_pairs(players):
        """Randomly shuffle the players for the first round."""
        random.shuffle(players)
        return [
            (players[i], players[i + 1])
            for i in range(0, len(players), 2)
        ]

    @staticmethod
    def generate_next_round_pairs(players, previous_matches):
        """
        Generates pairs based on the score,
         avoiding matches that have already been played.
        """
        players.sort(key=lambda p: p.score, reverse=True)
        pairs = []
        used_players = set()

        for i, player1 in enumerate(players):
            if player1 in used_players:
                continue

            for j in range(i + 1, len(players)):
                player2 = players[j]

                if player2 in used_players:
                    continue

                if ((player1, player2) not in previous_matches and
                   (player2, player1) not in previous_matches):
                    pairs.append((player1, player2))
                    used_players.update({player1, player2})
                    break

        return pairs
