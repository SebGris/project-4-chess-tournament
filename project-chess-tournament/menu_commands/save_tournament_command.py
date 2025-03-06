from commands.write_file_json_command import WriteFileJsonCommand
from commands.file_operation import FileOperation
from commands.json_file_receiver import JsonFileReceiver


class SaveTournamentCommand:
    def __init__(self, tournoi):
        self.tournoi = tournoi

    def execute(self):
        json_receiver = JsonFileReceiver("tournoi.json")
        write_command = WriteFileJsonCommand(json_receiver, self.tournoi.to_dict())
        file_operation = FileOperation(write_command)
        file_operation.execute_commands()
