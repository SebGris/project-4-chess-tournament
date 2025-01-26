class Player:
    """Class representing a chess player."""

    def __init__(self, last_name,  first_name, date_of_birth, id_chess):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.id_chess = id_chess
        self.points = 0  # Points accumulated during the tournament

    def __str__(self):
        """Returns a string representation of the player."""
        return (f"{self.first_name} {self.last_name} - "
                f"{self.date_of_birth} - "
                f"ID échecs : {self.id_chess} - "
                f"Points : {self.points}")
