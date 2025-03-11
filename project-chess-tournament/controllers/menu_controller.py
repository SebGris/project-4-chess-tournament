class MenuController():
    """Contrôleur principal de l'application"""

    def __init__(self, menu, menu_view, menu_state_updater):
        self.menu = menu
        self.menu_view = menu_view
        self.menu_state_updater = menu_state_updater

    def run(self):
        while True:
            self.menu_state_updater.refresh_menu()
            self.menu_view.display_menu(self.menu)
            choice = self.menu_view.get_user_choice()

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
                self.menu_view.display_invalid_option_message()
            else:
                command()
