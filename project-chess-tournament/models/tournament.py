import uuid
from typing import List
from models.player import Player
from models.round import Round
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository


class Tournament:

    def __init__(self, name, location, start_date, end_date, total_rounds,
                 tournament_id=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self._id = tournament_id or uuid.uuid4()
        self.players: List[Player] = []
        self.rounds: List[Round] = []
        self.description = None

    def get_all_matches(self):
        matches = []
        for round in self.rounds:
            matches.extend(round.matches)
        return matches

    def add_player(self, player: Player):
        self.players.append(player)

    def add_players(self, players: List[Player]):
        self.players.extend(players)

    def add_round(self, round: Round):
        self.rounds.append(round)

    def add_rounds(self, rounds: List[Round]):
        self.rounds.extend(rounds)

    def set_description(self, description):
        self.description = description

    def set_total_of_rounds(self, total_rounds):
        self.total_rounds = total_rounds

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dict(tournament_data):
        tournament = Tournament(
            tournament_data["name"],
            tournament_data["location"],
            tournament_data["start_date"],
            tournament_data["end_date"],
            tournament_data["total_rounds"],
            uuid.UUID(tournament_data["id"])
        )
        player_repo = PlayerRepository()
        round_repo = RoundRepository()
        match_repo = MatchRepository()
        tournament.set_description(tournament_data["description"])
        players_dto = player_repo.get_players_by_ids(tournament_data["player_ids"])
        tournament.players.extend([Player.from_dto(p) for p in players_dto])
        rounds_dto = round_repo.get_rounds_by_ids(tournament_data["round_ids"])
        tournament.rounds.extend(
            [Round.from_dto(r, match_repo) for r in rounds_dto]
        )
        return tournament

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "total_rounds": self.total_rounds,
            "player_ids": [player.id for player in self.players],
            "round_ids": [round.id for round in self.rounds]
        }
