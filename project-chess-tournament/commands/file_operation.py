from commands.command import Command


class FileOperation:
    def __init__(self, commands: list[Command] | Command):
        if isinstance(commands, list):
            self.commands = commands
        else:
            self.commands = [commands]

    def execute_commands(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results if len(results) > 1 else results[0]
