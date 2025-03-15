import json


class FileService:
    def __init__(self, file_path):
        self.file_path = file_path

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
