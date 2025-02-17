
class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class AddPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players()


class LoadPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.load_players_from_json()


class DisplayPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_players()


class ShowMenuCommand(Command):
    def __init__(self, controller, menu_name, menu_title):
        self.controller = controller
        self.menu_name = menu_name
        self.menu_title = menu_title

    def execute(self):
        self.controller.show_menu(self.menu_name, self.menu_title)

# ...other command classes for each menu action...
