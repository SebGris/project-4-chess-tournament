import sys
from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from models.player import Player
from models.tournament import Tournament
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament


# Tournament creation
view = ViewTournament()
controller = ControllerTournament(view)


def add_players_json():
    """Add players to JSON"""
    view_player = ViewPlayer()
    controller_player = ControllerPlayer(view_player)
    controller_player.add_players_to_json()


def new_tournament():
    """Start new tournament"""
    controller.entering_a_tournament()


def new_tournament_test():
    """Tournament variable for testing"""
    tournament = Tournament("Championnat de Paris", "Paris",
                            "01/06/2025", "07/06/2025")
    controller.entering_a_tournament(tournament)


def add_players():
    """Adding players to the tournament"""
    controller.add_players()


def add_players_test():
    """Ajouter des joueurs pour tester"""
    """Ne marche pas avec nombre impair de joueurs"""
    players = [Player("A", "Jean", "15/08/1990", "AB12345"),
               Player("B", "Alain", "12/11/1985", "CD67890"),
               Player("C", "Richard", "28/10/1955", "EF54321"),
               Player("D", "Marc", "23/06/1942", "GH98765"),
               Player("E", "Antoine", "22/06/1999", "II98765"),
               Player("F", "Christophe", "20/07/1990", "ZZ98765")]
    for player in players:
        controller.add_player(player)


def display_players():
    """Display players in the tournament"""
    controller.display_players()


def start_tournament():
    """Starting a tournament"""
    controller.start_tournament()


def add_description_tournament():
    """Add a description to the tournament"""
    controller.add_description()


def display_tournament():
    """Display the tournament"""
    controller.display_tournament()


def exit_menu():
    """Exit menu"""
    sys.exit(0)


MENU_ITEM = {
    1: ("Ajouter un joueur (JSON)", add_players_json),
    2: ("Nouveau tournoi", new_tournament),
    3: ("Ajouter des joueurs au tournoi", add_players),
    4: ("Afficher les joueurs du tournoi", display_players),
    5: ("Démarrer un tournoi", start_tournament),
    6: ("Ajouter une description au tournoi", add_description_tournament),
    7: ("Afficher le tournoi", display_tournament),
    8: ("Quitter", exit_menu)
    }


TEST = {
    80: ("Test : Nouveau tournoi", new_tournament_test),
    81: ("Test : Ajouter des joueurs au tournoi", add_players_test)
    }


def display_menu():
    """Displays the main menu and manages user choices."""
    while True:
        print("\n---- Menu principal ----")
        print("\n".join([f"{k}) {v[0]}" for (k, v) in MENU_ITEM.items()]))
        print("---- Menu test ----")
        print("\n".join([f"{k}) {v[0]}" for (k, v) in TEST.items()]))
        try:
            choice = int(input("\nChoisir une option : "))
            if choice in MENU_ITEM:
                action = MENU_ITEM[choice][1]
                action()
            elif choice in TEST:
                action = TEST[choice][1]
                action()
            else:
                print("Option non valide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    display_menu()
