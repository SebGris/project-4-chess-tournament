from commands.command import Command
from controllers.player_controller import PlayerController


class CreatePlayerCommand(Command):
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def execute(self):
        return PlayerController.create_player(self.nom, self.prenom, self.date_naissance)
