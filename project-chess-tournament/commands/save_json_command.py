from commands.command import Command
from commands.json_file_receiver import JsonFileReceiver


class SaveJSONCommand(Command):
    def __init__(self, file_path, data):
        self.file_path = file_path
        self.data = data

    def execute(self):
        receiver = JsonFileReceiver(self.file_path)
        receiver.write(self.data)
