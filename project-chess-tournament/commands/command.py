
class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class ChangeMenuCommand:
    def __init__(self, menu_controller, menu_name, menu_title):
        self.menu_controller = menu_controller
        self.menu_name = menu_name
        self.menu_title = menu_title

    def execute(self):
        self.menu_controller.run(self.menu_name, self.menu_title)


class AddPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players()


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
