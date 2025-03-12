import json
import os


class BaseRepository:
    FILE_PATH = ""

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                json.dump([], file)
