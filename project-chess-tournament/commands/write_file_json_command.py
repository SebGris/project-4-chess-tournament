from commands.command import Command


class WriteFileJsonCommand(Command):
    def __init__(self, json_file_receiver, data):
        self.json_file_receiver = json_file_receiver
        self.data = data

    def execute(self):
        self.json_file_receiver.write(self.data)
