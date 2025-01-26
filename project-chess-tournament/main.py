from views.viewplayer import ViewPlayer
from views.view import View
from controllers.controllerplayer import ControllerPlayer
from controllers.controller import Controller


def add_players():
    screen = ViewPlayer()
    controller = ControllerPlayer(screen)
    controller.add_players()


def new_tournament():
    view = View()
    game = Controller(view)
    game.run()


def exit_menu():
    exit()


MENU_ITEM = {
    1: ("Ajouter un joueur", add_players),
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
