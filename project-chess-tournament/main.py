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


MENU_ITEM = {1: (add_players, "Ajouter un joueur"),
             2: (new_tournament, "Nouveau Tournoi"),
             3: (exit_menu, "Quitter")}


def display_menu():
    while True:
        print("\n".join([f"{k}) {v[1]}" for (k, v) in MENU_ITEM.items()]))
        try:
            choice = int(input("Entrer le choix : "))
            if choice in MENU_ITEM:
                MENU_ITEM[choice][0]()
            else:
                print("Option non valide. Veuillez réessayer.")
        except ValueError:
            print("Oups ! Ce n'était pas un numéro valide. Réessayez...")


if __name__ == "__main__":
    display_menu()
