
class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class ChangeMenuCommand:
    def __init__(self, menu_controller, menu_name, menu_title):
        self.menu_controller = menu_controller
        self.menu_name = menu_name
        self.menu_title = menu_title

    def execute(self):
        self.menu_controller.start_menu_navigation(self.menu_name, self.menu_title)


class AddPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players() # TODO Ajoute un seul joueur ?

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


class NewTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.new_tournament()


class AddPlayersToTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players()


class LoadTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.load_tournament_from_json()


class StartTournamentCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.start_tournament()


class DisplayTournamentsCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_tournaments() # TODO Affiche les tournois


class AddDescriptionCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_description()


class DisplayTournamentPlayersCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.display_tournament_players()
class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
