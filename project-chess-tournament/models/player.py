class Player:
    """Player."""

    def __init__(self, last_name,  first_name="", date_of_birth=""):
        """Has a name."""
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        # add id chess

    def get_data(self):
        return (self.last_name, self.first_name, self.date_of_birth)