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
        used_player = set()
        for index, player in enumerate(players):
            if player in used_player:
                continue
            for x in range(index + 1, len(players)):
                if players[x] in used_player:
                    continue
                tpl = (player, players[x])
                if tpl not in previous_matches_sorted:
                    pairs.append(tpl)
                    used_player.add(player)
                    used_player.add(players[x])
                    break
        
        return pairs
