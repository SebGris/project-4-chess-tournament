from abc import ABC, abstractmethod


class Command(ABC):
    """Base class for all commands."""
    @abstractmethod
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
