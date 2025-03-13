import uuid
from typing import List
from models.player import Player
from models.round import Round


class Tournament:

    def __init__(self, tournament_id: uuid.UUID, name: str, location: str, start_date: str, end_date: str, description: str, players: List[Player], rounds: List[Round], number_of_rounds: int):
        self.id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []
        self.number_of_rounds = number_of_rounds
        self.current_round = 0

    def add_player(self, player: Player):
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
            "description": self.description,
            "player_ids": [str(player.id) for player in self.players],
            "round_ids": [str(round.id) for round in self.rounds],
            "number_of_rounds": self.number_of_rounds,
        }

    @staticmethod
    def from_dict(tournament: dict):
        """Create a Tournament object from a dictionary."""
        return Tournament(
            uuid.UUID(tournament["id"]),
            tournament["name"],
            tournament["location"],
            tournament["start_date"],
            tournament["end_date"],
            tournament["description"],
            tournament["player_ids"],
            tournament["rounds"],
            tournament["number_of_rounds"],
        )
