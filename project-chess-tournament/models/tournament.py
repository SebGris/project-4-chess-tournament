import uuid
from typing import List
from models.player import Player
from models.round import Round
from dtos.tournament_dto import TournamentDTO
from repositories.player_repository import PlayerRepository


class Tournament:

    def __init__(self, name, location, start_date, end_date, number_of_rounds, tournament_id=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self._id = tournament_id or uuid.uuid4()
        self.players: List[Player] = []
        self.rounds: List[Round] = []
        self.description = None

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

    def set_number_of_rounds(self, number_of_rounds):
        self.number_of_rounds = number_of_rounds

    @staticmethod
    def from_dto(tournament_dto: TournamentDTO, player_repo: PlayerRepository):
        players = [
            Player.from_dto(player_repo.get_player_by_id(id))
            for id in tournament_dto.player_ids
        ]
        tournament = Tournament(
            tournament_dto.name,
            tournament_dto.location,
            tournament_dto.start_date,
            tournament_dto.end_date,
            tournament_dto.number_of_rounds,
            tournament_dto.id
        )
        tournament.add_players(players)
        return tournament

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

    @property
    def id(self):
        return str(self._id)
