from commands.read_file_json_command import ReadFileJsonCommand
from commands.file_operation import FileOperation
from commands.json_file_receiver import JsonFileReceiver


class LoadTournamentCommand:
    def execute(self):
        json_receiver = JsonFileReceiver("tournoi.json")
        read_command = ReadFileJsonCommand(json_receiver)
        file_operation = FileOperation(read_command)
        return file_operation.execute_commands()
