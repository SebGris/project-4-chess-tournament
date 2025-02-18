from commands.command import (
    ChangeMenuCommand, QuitCommand
)


class MenuController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.commands = {
            "Gestion des tournois": ChangeMenuCommand(
                self, "tournament", "Gestion des tournois"
            ),
            "Gestion des joueurs": ChangeMenuCommand(
                self, "player", "Gestion des joueurs"
            ),
            "Menu pour test": ChangeMenuCommand(
                self, "test", "Menu pour test"
            ),
            "Retour au menu principal": ChangeMenuCommand(
                self, "main", "Menu principal"
            ),
            "Quitter": QuitCommand()
            }

    def start_menu_navigation(self, menu_name="main",
                              menu_title="Menu principal"):
        while True:
            options = self.model.get_menu_items(menu_name)
            self.view.display_menu(menu_title, options)
            try:
                choice = int(self.view.get_user_choice(len(options)))
                if 1 <= choice <= len(options):
                    self.execute_command(options[choice - 1])
                else:
                    self.view.display_invalid_option_message_try_again()
            except ValueError:
                self.view.display_invalid_input_message_enter_a_number()

    def execute_command(self, selected_option):
        command = self.commands.get(selected_option)
        if command:
            command.execute()
        else:
            self.view.display_invalid_option_message_try_again()
