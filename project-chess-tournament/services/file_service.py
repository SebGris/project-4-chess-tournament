import json
import os


class FileService:
    FOLDER = "app_chess_tournament/data/tournaments"

    def __init__(self, file_path):
        """
        Creates the storage file if it doesn't already exist.
        """
        self.data_folder = os.path.join(os.getcwd(), self.FOLDER)
        os.makedirs(self.data_folder, exist_ok=True)
        self.file_path = os.path.join(self.data_folder, file_path)
        if not os.path.exists(self.file_path):
            # Create an empty file if it doesn't exist
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def read_from_file(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Fichier non trouvé")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON")

    def write_to_file(self, data):
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise ValueError("Erreur d'écriture du fichier")
