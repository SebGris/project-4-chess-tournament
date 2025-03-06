from commands.command import Command
from controllers.tournament_controller import TournamentController


class CreateTournamentCommand(Command):
    def __init__(self, nom, joueurs, rounds):
        self.nom = nom
        self.joueurs = joueurs
        self.rounds = rounds

    def execute(self):
        return TournamentController.create_tournament(self.nom, self.joueurs, self.rounds)
