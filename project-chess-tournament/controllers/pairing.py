import random


class Pairing:
    """Handles the generation of player pairs for each round of the tournament."""

    @staticmethod
    def generate_first_round_pairs(players):
        """
        Randomly shuffles the players and generates pairs for the first round.

        Args:
            players (list): List of players participating in the tournament.

        Returns:
            list: A list of tuples, where each tuple contains two players paired together.
        """
        random.shuffle(players)
        return [(players[i], players[i + 1]) for i in range(0, len(players), 2)]

    @staticmethod
    def generate_next_round_pairs(players, previous_matches):
        """
        Generates pairs for subsequent rounds based on player scores, avoiding repeated matches.

        Args:
            players (list): List of players sorted by their scores.
            previous_matches (set): A set of tuples representing matches that have already been played.

        Returns:
            list: A list of tuples, where each tuple contains two players paired together.
        """
        # Sort players by score in descending order
        players.sort(key=lambda p: p.score, reverse=True)
        pairs, used_players = [], set()
        num_pairs_needed = len(previous_matches)

        for index, player1 in enumerate(players):
            if player1 in used_players:
                continue

            for j in range(index + 1, len(players)):
                player2 = players[j]
                if player2 in used_players:
                    continue

                # Ensure the pair has not played together in previous matches
                if ((player1, player2) not in previous_matches and (player2, player1) not in previous_matches):
                    pairs.append((player1, player2))
                    used_players.update({player1, player2})
                    break

            # Stop if the required number of pairs has been generated
            if len(pairs) == num_pairs_needed:
                break

        # Pair remaining players if more pairs are needed
        remaining_players = [p for p in players if p not in used_players]
        players.sort(key=lambda p: p.score, reverse=True)
        while len(pairs) < num_pairs_needed and len(remaining_players) >= 2:
            player1 = remaining_players.pop(0)
            player2 = remaining_players.pop(0)
            pairs.append((player1, player2))
        return pairs
