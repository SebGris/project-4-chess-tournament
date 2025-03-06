from models.player import Player
from commands.tournament_commands import AddPlayersCommand
from views.player_view import PlayerView


class PlayerController:
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view

    @staticmethod
    def create_player(nom, prenom, date_naissance):
        joueur = Player(nom, prenom, date_naissance)
        PlayerView.afficher_joueur(joueur)
        return joueur

    def add_players(self):
        players = []
        while True:
            player_data = self.view.get_player_data()
            if player_data:
                player = Player(**player_data)
                players.append(player)
                self.view.display_add_player_message(player.full_name)
            else:
                break
        self.__execute_command(AddPlayersCommand, players)

    def __execute_command(self, command_class, *args):
        command = command_class(self.tournament, *args)
        message = command.execute()
        self.view.display_message(message)
