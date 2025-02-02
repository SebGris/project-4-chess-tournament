from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from models.player import Player
from models.tournament import Tournament
from views.view_player import ViewPlayer


def add_players():
    """Add players to JSON"""
    view = ViewPlayer()
    controller = ControllerPlayer(view)
    controller.add_players_to_json()


def new_tournament():
    """Start new tournament"""
    view = ViewPlayer()
    tournament = Tournament("Championnat de Paris", "Paris",
                            "01/06/2025", "07/06/2025")
    controller = ControllerTournament(view, tournament)
    # Ajouter des joueurs
    # controller.add_players_to_tournament()
    # Afficher les joueurs inscrits
    # controller.display_players()

    # Ajouter des joueurs
    controller.add_player(Player("Dupont", "Jean", "15/08/1990", "AB12345"))
    controller.add_player(Player("Duval", "Alain", "12/11/1985", "CD67890"))
    controller.add_player(Player("Maurel", "Richard", "28/10/1955", "EF54321"))
    controller.add_player(Player("Chevalier", "Marc", "23/06/1912", "GH98765"))

    # Démarrer un tour
    controller.start_next_round()

    # Enregistrer les résultats des matchs
    controller.record_match_results()

    # Afficher les résultats du tournoi
    controller.show_results()


def exit_menu():
    """Exit menu"""
    exit()


MENU_ITEM = {
    1: ("Ajouter un joueur dans la base de donnée", add_players),
    2: ("Nouveau Tournoi", new_tournament),
    3: ("Quitter", exit_menu)
    }


def display_menu():
    """Displays the main menu and manages user choices."""
    while True:
        print("\nMenu :")
        print("\n".join([f"{k}) {v[0]}" for (k, v) in MENU_ITEM.items()]))
        try:
            choice = int(input("Entrer le choix : "))
            if choice in MENU_ITEM:
                action = MENU_ITEM[choice][1]
                action()
            else:
                print("Option non valide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    display_menu()
