from controllers.menu_controller import MenuController
from controllers.menu_state_updater import MenuStateUpdater
from controllers.tournament_controller import TournamentController
from models.menu import Menu
from views.menu_view import MenuView
from views.tournament_view import TournamentView

if __name__ == "__main__":
    menu = Menu()
    menu_view = MenuView()
    tournament_view = TournamentView(menu)
    tournament_controller = TournamentController(tournament_view)
    menu_state_updater = MenuStateUpdater(menu, tournament_controller)
    controller = MenuController(menu, menu_view, tournament_controller, menu_state_updater)
    controller.run()
