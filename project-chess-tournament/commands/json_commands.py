from commands.command import Command

class ReadFileJsonCommand(Command):
    def __init__(self, json_file_receiver):
        self.json_file_receiver = json_file_receiver

    def execute(self):
        return self.json_file_receiver.read()

class WriteFileJsonCommand(Command):
    def __init__(self, json_file_receiver, data):
        self.json_file_receiver = json_file_receiver
        self.data = data

    def execute(self):
        self.json_file_receiver.write(self.data)

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