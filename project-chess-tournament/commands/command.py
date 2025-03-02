class Command:
    """Base class for all commands."""
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
