from controllers.controller_tournament import ControllerTournament
from controllers.menu_state_manager import MenuStateManager
from models.tournament import Tournament
from views.view import View


class ControllerMenu():
    """Contrôleur principal de l'application"""

    def __init__(self, menu, menuview):
        self.menu = menu
        self.menuview = menuview
        self.view = View()
        self.tournament = Tournament()
        self.tournament_controller = ControllerTournament(
            self.tournament, self.menu, self.view
        )
        self.menu_state_manager = MenuStateManager(
            self.menu, self.tournament_controller
        )

    def run(self):
        while True:
            self.menu_state_manager.update_menu()
            self.menuview.display_menu(self.menu)
            choice = self.menuview.get_user_choice()

            try:
                choice_index = int(choice) - 1
                flat_menu = [
                    item for group in self.menu.get_groups()
                    for item in group['items']
                ]
                if 0 <= choice_index < len(flat_menu):
                    command = flat_menu[choice_index]["command"]
                else:
                    raise ValueError("Invalid choice")
            except (IndexError, ValueError):
                self.menuview.display_invalid_option_message()
            else:
                command()
