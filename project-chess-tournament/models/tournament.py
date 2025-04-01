import uuid
from models.player import Player
from models.round import Round
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository


class Tournament:
    """Represents a chess tournament."""
    def __init__(self, name, location, start_date, end_date, total_rounds,
                 tournament_id=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.total_rounds = total_rounds
        self._id = tournament_id or uuid.uuid4()
        self.players: list[Player] = []
        self.rounds: list[Round] = []
        self.description = None

    def get_all_matches(self):
        """Returns all matches from all rounds."""
        return [match for round in self.rounds for match in round.matches]

    def add_players(self, players: list[Player]):
        """Adds players to the tournament."""
        self.players.extend(players)

    def set_description(self, description):
        """Sets the description of the tournament."""
        self.description = description

    def set_total_of_rounds(self, total_rounds):
        """Sets the total number of rounds."""
        self.total_rounds = total_rounds

    def is_finished(self):
        """Checks if the tournament is finished."""
        # if the number of rounds is equal to the total number of rounds
        # and all rounds are finished, the tournament is finished
        if len(self.rounds) == self.total_rounds:
            return all(round.is_finished() for round in self.rounds)
        return False

    @property
    def id(self):
        return str(self._id)

    @staticmethod
    def from_dict(tournament_data):
        """Creates a Tournament instance from a dictionary."""
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
        tournament.set_description(tournament_data["description"])
        players = player_repo.get_by_ids(tournament_data["player_ids"])
        tournament.players.extend(players)
        rounds = round_repo.get_by_ids(tournament_data["round_ids"])
        tournament.rounds.extend(rounds)
        return tournament

    def to_dict(self):
        """Converts the tournament instance to a dictionary."""
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
