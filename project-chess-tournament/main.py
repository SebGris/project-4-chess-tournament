# from controllers.menu_controller import MenuController
# from models.menu import Menu
# from views.menu_view import MenuView

from commands.create_match_command import CreateMatchCommand
from commands.create_round_command import CreateRoundCommand
from commands.create_tournament_command import CreateTournamentCommand
from menu_commands.create_players_command import CreatePlayersCommand
from menu_commands.save_tournament_command import SaveTournamentCommand
from menu_commands.load_tournament_command import LoadTournamentCommand

def main():
    # Création de joueurs
    create_players_command = CreatePlayersCommand()
    joueurs = create_players_command.execute()
    joueur1, joueur2 = joueurs

    # Création de matchs
    match1_command = CreateMatchCommand(joueur1, joueur2, player1_score=2, player2_score=1)
    match1 = match1_command.execute()

    # Création de rounds
    round1_command = CreateRoundCommand("Round 1", [match1])
    round1 = round1_command.execute()

    # Création de tournoi
    tournoi_command = CreateTournamentCommand("Tournoi 1", [joueur1, joueur2], [round1])
    tournoi = tournoi_command.execute()

    # Sauvegarde du tournoi en JSON
    save_tournament_command = SaveTournamentCommand(tournoi)
    save_tournament_command.execute()

    # Chargement du tournoi depuis JSON
    load_tournament_command = LoadTournamentCommand()
    data = load_tournament_command.execute()
    print(data)

if __name__ == "__main__":
    main()
    # menu = Menu()
    # menu_view = MenuView()
    # controller = MenuController(menu, menu_view)
    # controller.run()
