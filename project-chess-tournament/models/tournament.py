class Tournament:
    """Class representing a chess tournament."""
    description = ""
    total_rounds = 4
    players = []  # Liste des joueurs enregistrés

    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = 1

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
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'current_round': self.current_round
        }

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date} - "
                f"{self.end_date}  | "
                f"Nombre de tours : {self.total_rounds} | "
                f"Tour actuel : {self.current_round}/{self.total_rounds}\n"
                f"Joueurs inscrits : {len(self.players)}\n"
                f"Description : {self.description}")
