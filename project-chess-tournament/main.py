import sys
from controllers.controller_tournament import ControllerTournament
from views.view_tournament import ViewTournament
from menu_test import *

# Tournament creation
view = ViewTournament()
controller = ControllerTournament(view)


def new_tournament():
    """Start new tournament"""
    controller.entering_a_tournament()


def add_players():
    """Adding players to the tournament"""
    controller.add_players()


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
    1: ("Nouveau tournoi", new_tournament),
    2: ("Ajouter des joueurs au tournoi", add_players),
    3: ("Afficher les joueurs du tournoi", display_players),
    4: ("Démarrer un tournoi", start_tournament),
    5: ("Ajouter une description au tournoi", add_description_tournament),
    6: ("Afficher le tournoi", display_tournament),
    7: ("Quitter", exit_menu)
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
