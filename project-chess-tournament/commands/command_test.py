from .command import Command


class AddTournamentCommandTest(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_new_tournament_test()


class AddPlayersToTournamentCommandTest(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.add_players_test()


class NewTournamentCommandTest(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.new_tournament_and_add_players_test()


class PairingCommandTest(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.pairing_test()


class SavePlayersCommandTest(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.save_players_test()
