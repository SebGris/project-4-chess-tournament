import uuid
from dataclasses import dataclass, asdict
from typing import List
from dtos.tournament_dto import TournamentDTO
from models.player import Player
from models.round import Round
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository


@dataclass
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

    def update_scores(self):
        matches = [match for round in self.rounds for match in round.matches]
        for match in matches:
            player1_id, player1_score = match.get_player1()
            player2_id, player2_score = match.get_player2()
            for player in self.players:
                if player.id == player1_id:
                    player.score += player1_score
                elif player.id == player2_id:
                    player.score += player2_score

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dto(
        tournament_dto: TournamentDTO,
        player_repo: PlayerRepository,
        round_repo: RoundRepository,
        match_repo: MatchRepository
    ):
        tournament = Tournament(
            tournament_dto.name,
            tournament_dto.location,
            tournament_dto.start_date,
            tournament_dto.end_date,
            tournament_dto.total_rounds,
            uuid.UUID(tournament_dto.id)
        )
        players_dto = player_repo.get_players_by_ids(tournament_dto.player_ids)
        tournament.players.extend([Player.from_dto(p) for p in players_dto])
        rounds_dto = round_repo.get_rounds_by_ids(tournament_dto.round_ids)
        tournament.rounds.extend(
            [Round.from_dto(r, match_repo, player_repo) for r in rounds_dto]
        )
        return tournament

    def to_dto(self):
        return TournamentDTO(
            self.id,
            self.name,
            self.location,
            self.start_date,
            self.end_date,
            self.description,
            self.total_rounds,
            [player.id for player in self.players],
            [round.id for round in self.rounds]
        )
    
    def to_dict(self):
        return asdict(self)
