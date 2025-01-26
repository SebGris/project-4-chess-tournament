from datetime import datetime
from models.round import Round
from models.match import Match


class Tournament:
    """Class representing a chess tournament."""

    def __init__(self, name, location, start_date, end_date,
                 number_of_rounds=4, current_round=1, description=""):
        self.name = name
        self.location = location
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds = []  # Liste des tours
        self.players = []  # Liste des joueurs enregistrés
        self.description = description

    def _validate_date(self, date_str):
        """Validates and converts a character string representing a
         date into a datetime object."""
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Format de date invalide. Utilisez JJ/MM/AAAA.")

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def start_round(self):
        """Commence un nouveau tour avec les matchs."""
        if self.current_round > self.number_of_rounds:
            print("Le tournoi est terminé.")
            return
        round_ = Round(self.current_round)
        self.rounds.append(round_)
        # Générer les matchs pour ce tour (matchs pairs de joueurs)
        for i in range(0, len(self.players), 2):
            if i + 1 < len(self.players):  # Assurer qu'il y a deux joueurs
                match = Match(self.players[i], self.players[i+1])
                round_.add_match(match)
        self.current_round += 1

    def show_results(self):
        """Displays the tournament results."""
        for round_ in self.rounds:
            print(round_)

    def __str__(self):
        """Returns a string representation of the tournament."""
        return (f"Tournoi: {self.name} | Lieu: {self.location} | "
                f"Dates: {self.start_date.strftime('%d/%m/%Y')} - "
                f"{self.end_date.strftime('%d/%m/%Y')} | "
                f"Tours: {self.number_of_rounds} | "
                f"Tour actuel: {self.current_round}")
