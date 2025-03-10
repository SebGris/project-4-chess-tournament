import uuid
from models.round import Round


class Tournament:
    """Class representing a chess tournament. La classe représente un tournoi de manière assez complète. Elle pourrait être divisée pour séparer la gestion des joueurs, des scores et des rounds, mais elle reste cohérente dans sa responsabilité de représenter un tournoi."""
    def __init__(self, name=None, location=None, start_date=None,
                 end_date=None, number_of_rounds=4, description=None,
                 players=None, rounds=None):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = 0
        self.players = players if players is not None else []
        self.description = description
        self.rounds = rounds if rounds is not None else []
        self.number_of_rounds = number_of_rounds

    def set_tournament(self, name, location, start_date, end_date,
                       number_of_rounds, description=None, players= None,
                       rounds=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.description = description
        self.rounds = [Round(**round) for round in rounds] if rounds else []
        self.number_of_rounds = number_of_rounds

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
            "player_ids": [str(player.id) for player in self.players],
            "description": self.description,
            "rounds": [round.to_dict() for round in self.rounds],
            "number_of_rounds": self.number_of_rounds
        }
