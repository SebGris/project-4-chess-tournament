from views.screenplayer import ScreenPlayer
from views.view import View
from controllers.controllerplayer import ControllerPlayer
from controllers.controller import Controller

menu_item = ["1) Ajouter un joueur", "2) Nouveau Tournoi", "3) Quitter"]

def display_menu():
    while True:
        print("\n".join(menu_item))
        choice = input("Entrer le choix : ")
        choice = choice.strip()
        if (choice == "1"):
            add_players()
        elif (choice == "2"):
            new_tournament()
        elif (choice == "3"):
            break
        elif (choice == ""):
            break
        else:
            print("Option non valide. Veuillez réessayer.")

def add_players():
    screen = ScreenPlayer()
    controller = ControllerPlayer(screen)
    controller.add_players()

def new_tournament():
    view = View()
    game = Controller(view)
    game.run()


if __name__ == "__main__":
    display_menu()