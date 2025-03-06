from commands.command import Command


class QuitCommand(Command):
    def execute(self):
        print("Au revoir !")
        exit()
