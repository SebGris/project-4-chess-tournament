class Command:
    """Base class for all commands."""
    def execute(self):
        raise NotImplementedError("You should implement this method.")
