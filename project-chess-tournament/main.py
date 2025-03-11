from controllers.menu_controller import MenuController
from controllers.menu_state_updater import MenuStateUpdater
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.menu import Menu
from models.player_repository import PlayerRepository
from models.tournament_repository import TournamentRepository
from views.menu_view import MenuView
from views.player_view import PlayerView
from views.tournament_view import TournamentView

if __name__ == "__main__":
    player_repository = PlayerRepository()
    player_view = PlayerView()
    player_controller = PlayerController(player_repository, player_view)

    tournament_repository = TournamentRepository()
    tournament_view = TournamentView()
    tournament_controller = TournamentController(tournament_repository, tournament_view)

    menu = Menu()
    menu_view = MenuView()
    menu_state_updater = MenuStateUpdater(menu, tournament_controller)
    menu_controller = MenuController(menu, menu_view, menu_state_updater)
    menu_controller.run()
