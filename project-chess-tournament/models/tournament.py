class Tournament:
    """Class representing a chess tournament."""
    description = ""
    players = []  # Liste des joueurs enregistrés
    rounds = []  # Liste des tours (tour peut être un objet ou un dictionnaire)

    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        # self.number_of_rounds = number_of_rounds

    def set_description(self, texte):
        """Define the tournament description."""
        self.description = texte

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def show_results(self):
        """Displays the tournament results."""
        for round_ in self.rounds:
            print(round_)

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date.strftime('%d/%m/%Y')} - "
                f"{self.end_date.strftime('%d/%m/%Y')}  | "
                f"Description : {self.description}")
