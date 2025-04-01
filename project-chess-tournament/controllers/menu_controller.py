from models.application import Application
from views.menu_view import MenuView


class MenuController:
    """Controller for managing the menu in the chess tournament application."""
    def __init__(self, application: Application, menu_view: MenuView):
        """Initializes the MenuController with the application and menu view."""
        self.application = application
        self.menu_view = menu_view

    def show_menu(self):
        """Displays the menu and handles user input."""
        while True:
            menu = self.application.get_refresh_menu()
            self.menu_view.display_menu(menu)
            choice = self.menu_view.get_user_choice()
            command = self._get_command_from_choice(menu, choice)
            if command:
                command()
                input("Appuyez sur une touche pour afficher le menu...")

    def _get_command_from_choice(self, menu, choice):
        """Returns the command associated with the user's choice."""
        try:
            choice_index = int(choice) - 1
            flat_menu = [
                item
                for group in menu.get_groups()
                for item in group["items"]
            ]
            if 0 <= choice_index < len(flat_menu):
                return flat_menu[choice_index]["command"]
            else:
                raise ValueError("Invalid choice")
        except (IndexError, ValueError):
            self.menu_view.display_invalid_option_message()
            return None
