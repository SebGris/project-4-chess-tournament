from commands.command import Command


class ShowAllTournamentsCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.get_all_tournaments()
