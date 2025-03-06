from commands.command import Command


class ReadFileJsonCommand(Command):
    def __init__(self, json_file_receiver):
        self.json_file_receiver = json_file_receiver

    def execute(self):
        return self.json_file_receiver.read()
