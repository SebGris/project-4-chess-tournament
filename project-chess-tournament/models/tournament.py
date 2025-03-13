import uuid


class Tournament:

    def __init__(
        self,
        name,
        location,
        start_date=None,
        end_date=None,
        description=None,
        players=None,
        rounds=None,
        number_of_rounds=4,
    ):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []
        self.number_of_rounds = number_of_rounds
        self.current_round = 0

    def set_description(self, description):
        """Define the tournament description."""
        self.description = description

    def set_number_of_rounds(self, number_of_rounds):
        """Define the number of rounds."""
        self.number_of_rounds = number_of_rounds

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def update_scores(self, match_results):
        for match in match_results:
            player1_id, player1_score = match.get_player1()
            player2_id, player2_score = match.get_player2()
            for player in self.players:
                if player.id == player1_id:
                    player.score += player1_score
                elif player.id == player2_id:
                    player.score += player2_score

    def get_current_round(self):
        if len(self.rounds) == 0:
            return None
        return self.rounds[self.current_round]

    def get_current_round_no(self):
        for index, round in enumerate(self.rounds):
            if round.is_finished() is False:
                return index + 1
        return 0

    # def get_current_round(self):
    #     for round in self.rounds:
    #         if round.is_finished() is False:
    #             return round
    #     return None

    def is_complete(self):
        """Checks if the tournament is over."""
        return self.current_round > self.number_of_rounds

    def to_dict(self):
        """Convert Tournament object to dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "player_ids": [player_id for player_id in self.players],
            "description": self.description,
            "rounds": [round for round in self.rounds],
            "number_of_rounds": self.number_of_rounds,
        }

    @staticmethod
    def from_dict(tournament_dict):
        """Create a Tournament object from a dictionary."""
        return Tournament(
            name=tournament_dict["name"],
            location=tournament_dict["location"],
            start_date=tournament_dict.get("start_date"),
            end_date=tournament_dict.get("end_date"),
            number_of_rounds=tournament_dict.get("number_of_rounds", 4),
            description=tournament_dict.get("description"),
            players=tournament_dict.get("player_ids", []),
            rounds=tournament_dict.get("rounds", []),
        )
