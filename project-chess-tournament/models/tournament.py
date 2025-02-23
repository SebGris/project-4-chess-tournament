import uuid
from models.round import Round


class Tournament:
    """Class representing a chess tournament."""
    def __init__(self, name=None, location=None, start_date=None,
                 end_date=None, number_of_rounds=4, players=None,
                 description=None, rounds=None):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = 1
        self.players = players if players is not None else []
        self.description = description
        self.rounds = rounds if rounds is not None else []
        self.number_of_rounds = number_of_rounds

    def set_tournament(self, name, location, start_date, end_date,
                       number_of_rounds, players, description=None,
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
            player1_id, player1_score = match[0]
            player2_id, player2_score = match[1]
            for player in self.players:
                if str(player.id) == player1_id:
                    player.score += player1_score
                elif str(player.id) == player2_id:
                    player.score += player2_score

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
            "players": [str(player.id) for player in self.players],
            "description": self.description,
            "rounds": [round.to_dict() for round in self.rounds],
            "number_of_rounds": self.number_of_rounds
        }

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date} - "
                f"{self.end_date} | "
                f"Nombre de tours : {self.number_of_rounds} | "
                f"Tour actuel : {self.current_round}/{self.number_of_rounds}\n"
                f"Description : {self.description}\n"
                f"Joueurs inscrits : {len(self.players)}\n")
