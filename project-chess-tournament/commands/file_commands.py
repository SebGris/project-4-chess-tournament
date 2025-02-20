import json
from commands.base_command import Command


class ReadJsonFileCommand(Command):
    """Read data from a JSON file."""
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)


class WriteJsonFileCommand(Command):
    """Write data to a JSON file."""
    def __init__(self, file_path, data):
        self.file_path = file_path
        self.data = data

    def execute(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)
