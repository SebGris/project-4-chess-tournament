import sys
from controllers.controller_tournament import ControllerTournament
from views.view_tournament import ViewTournament
# import pour test
from controllers.controller_player import ControllerPlayer
from models.player import Player
from models.tournament import Tournament
from models.pairing_perso import PairingPerso
from views.view_player import ViewPlayer

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

# début menu test

def new_tournament_test():
    """Tournament variable for testing"""
    tournament = Tournament("Championnat de Paris", "Paris",
                            "01/06/2025", "07/06/2025")
    controller.entering_a_tournament(tournament)

def get_players_test():
    """Ajouter des joueurs pour tester"""
    return [Player("A", "Jean", "12/11/1985", "AB12345"),
               Player("B", "Alain", "12/11/1985", "CD67890"),
               Player("C", "Richard", "28/10/1955", "EF54321"),
               Player("D", "Marc", "23/06/1942", "GH98765"),
               Player("E", "Antoine", "23/06/1942", "II98765"),
               Player("F", "Christophe", "20/07/1990", "ZZ98765")]

def add_players_test():
    """Ajouter des joueurs pour tester"""
    players = get_players_test()
    for player in players:
        controller.add_player(player)

def pairing_test():
    players = get_players_test()
    first = [
        (players[0], players[1]), 
        (players[2], players[3]), 
        (players[4], players[5]), 
        (players[0], players[2])
    ]
    pairs = PairingPerso.generate_next_round_pairs(players, first)
    print(first)
    print(pairs)

def save_players_test():
    """Save players to JSON for testing."""
    controller_player = ControllerPlayer(ViewPlayer())
    controller_player.add_players(get_players_test())
    controller_player.save_players_to_json()
    new_tournament_test()
    controller.save_tournament_to_json()

def new_tournament_and_add_players_test():
    new_tournament_test()
    add_players_test()

TEST = {
    81: ("Nouveau tournoi", new_tournament_test),
    82: ("Ajouter des joueurs au tournoi", add_players_test),
    83: ("Nouveau tournoi + Ajouter des joueurs",
         new_tournament_and_add_players_test),
    84: ("Pairing", pairing_test),
    85: ("Sauvegarder les joueurs et tournoi en JSON", save_players_test)
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
