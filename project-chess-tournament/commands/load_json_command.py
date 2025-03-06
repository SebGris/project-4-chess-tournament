from commands.command import Command
from commands.json_file_receiver import JsonFileReceiver


class LoadJSONCommand(Command):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self):
        receiver = JsonFileReceiver(self.file_path)
        return receiver.read()
