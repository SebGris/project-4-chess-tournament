from commands.create_player_command import CreatePlayerCommand


class CreatePlayersCommand:
    def execute(self):
        joueur1_command = CreatePlayerCommand("Dupont", "Jean", "01/01/1990")
        joueur2_command = CreatePlayerCommand("Martin", "Paul", "02/02/1992")
        joueur1 = joueur1_command.execute()
        joueur2 = joueur2_command.execute()
        return joueur1, joueur2
