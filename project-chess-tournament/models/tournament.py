import uuid


class Tournament:
    """Class representing a chess tournament."""
    total_rounds = 4

    def __init__(self, name=None, location=None, start_date=None,
                 end_date=None, players=None, description=None,
                 rounds=None):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = 1
        self.players = players if players is not None else []
        self.description = description
        self.rounds = rounds if rounds is not None else []

    def set_tournament(self, name, location, start_date, end_date, players,
                       description=None, rounds=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.description = description
        self.rounds = rounds if rounds is not None else []

    def set_description(self, description):
        """Define the tournament description."""
        self.description = description

    def add_player(self, player_id):
        """Add a player to the tournament."""
        self.players.append(player_id)

    def set_number_of_rounds(self, number):
        """Define the number of rounds."""
        self.total_rounds = number

    def is_complete(self):
        """Checks if the tournament is over."""
        return self.current_round > self.total_rounds

    def to_dict(self):
        """Convert Tournament object to dictionary."""
        return {
            "id": str(self.id),
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players,
            "description": self.description,
            "rounds": [round.to_dict() for round in self.rounds]
        }

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date} - "
                f"{self.end_date} | "
                f"Nombre de tours : {self.total_rounds} | "
                f"Tour actuel : {self.current_round}/{self.total_rounds}\n"
                f"Description : {self.description}\n"
                f"Joueurs inscrits : {len(self.players)}\n")
