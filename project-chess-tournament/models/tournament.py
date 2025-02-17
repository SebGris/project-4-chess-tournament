import uuid
from models.round import Round


class Tournament:
    """Class representing a chess tournament."""
    total_rounds = 4

    def __init__(self, name, location, start_date, end_date,
                 id=None, current_round=1, description="Aucune description", players=None, rounds=None):
        # Use provided ID or generate a unique one
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.description = description
        self.players = players if players is not None else []
        self.rounds = rounds if rounds is not None else []

    def set_description(self, texte):
        """Define the tournament description."""
        self.description = texte

    def set_number_of_rounds(self, number):
        """Define the number of rounds."""
        self.total_rounds = number

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def is_complete(self):
        """Checks if the tournament is over."""
        return self.current_round > self.total_rounds

    def to_dict(self):
        """Convert Tournament object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'current_round': self.current_round,
            'description': self.description,
            'player_ids': [player.id for player in self.players],
            'rounds': [round_instance.to_dict() for round_instance in self.rounds]
        }

    @classmethod
    def from_dict(cls, data, all_players):
        return cls(
            id=data["id"],
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            current_round=data["current_round"],
            description=data["description"],
            players=[
                all_players[player_id] for player_id in data["player_ids"]
            ],
            rounds=[Round.from_dict(round_data, all_players) for round_data in data["rounds"]]
        )

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date} - "
                f"{self.end_date} | "
                f"Nombre de tours : {self.total_rounds} | "
                f"Tour actuel : {self.current_round}/{self.total_rounds}\n"
                f"Description : {self.description}\n"
                f"Joueurs inscrits : {len(self.players)}\n")
