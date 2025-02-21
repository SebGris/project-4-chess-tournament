import json


class JsonFileManager:
    @staticmethod
    def read(file_path):
        """Read data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Fichier non trouvé")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON")

    @staticmethod
    def write(file_path, data):
        """Write data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise ValueError("Erreur d'écriture du fichier")
