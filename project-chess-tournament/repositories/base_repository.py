import json
import os


class BaseRepository:
    FILE_PATH = ""

    def __init__(self):
        if not os.path.exists(self.get_file_path()):
            with open(self.get_file_path(), "w") as file:
                json.dump([], file)

    def get_file_path(self, folder="data/tournaments"):
        data_folder = os.path.join(os.getcwd(), folder)
        os.makedirs(data_folder, exist_ok=True)
        return os.path.join(data_folder, self.FILE_PATH)
