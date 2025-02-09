import random


class PairingPerso:
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
        pairs = []
        players.sort(key=lambda p: p.score, reverse=True)
        previous_matches_sorted = [
            (min(match), max(match)) for match in previous_matches
        ]
        for index, player in enumerate(players):
            for x in range(index + 1, len(players)):
                tpl = (player, players[x])
                if tpl not in previous_matches_sorted:
                    pairs.append(tpl)
                    break
        return pairs
