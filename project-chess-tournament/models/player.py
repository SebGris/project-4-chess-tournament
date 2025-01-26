class Player:
    """Player."""

    def __init__(self, last_name,  first_name="", date_of_birth="",
                 id_chess_player=""):
        """Has a name."""
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.id_chess_player = id_chess_player
