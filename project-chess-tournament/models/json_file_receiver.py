import json


class JsonFileReceiver:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Read data from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Fichier non trouvé")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON")

    def write(self, data):
        """Write data to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise ValueError("Erreur d'écriture du fichier")
