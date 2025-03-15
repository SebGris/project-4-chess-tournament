import uuid
from typing import List
from models.player import Player
from models.round import Round


class Tournament:

    def __init__(self, name, location, start_date, end_date, number_of_rounds, tournament_id=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self._id = tournament_id or uuid.uuid4()
        self.players = []
        self.rounds = []
        self.current_round = 0
        self.description = None

    def add_player(self, player: Player):
        self.players.append(player)

    def add_players(self, players: List[Player]):
        self.players.extend(players)

    def add_round(self, player: Round):
        self.players.append(player)

    def add_rounds(self, players: List[Round]):
        self.players.extend(players)

    def set_description(self, description):
        self.description = description

    def set_number_of_rounds(self, number_of_rounds):
        self.number_of_rounds = number_of_rounds

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
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "player_ids": [player.id for player in self.players],
            "round_ids": [round.id for round in self.rounds]
        }

    @staticmethod
    def from_dict(dict_):
        tournament = Tournament(
            dict_["name"],
            dict_["location"],
            dict_["start_date"],
            dict_["end_date"],
            dict_["number_of_rounds"],
            dict_.get("id")
        )
        tournament.set_description(dict_["description"])
        return tournament

    @property
    def id(self):
        return str(self._id)
