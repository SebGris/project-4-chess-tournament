import json
import os

class JsonFileService:
    @staticmethod
    def load_from_file(file_path) -> dict:
        """Read data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Fichier non trouvé")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage JSON")

    @staticmethod
    def save_to_file(data: dict, file_path):
        """Write data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise ValueError("Erreur d'écriture du fichier")

def get_file_path(filename, folder='data/tournaments'):
    """Get the full file path for the given filename and folder."""
    data_folder = os.path.join(os.getcwd(), folder)
    os.makedirs(data_folder, exist_ok=True)
    return os.path.join(data_folder, filename)

def tournaments_file_path():
    return get_file_path("tournaments.json")

def tournaments_file_path_exists():
    return os.path.exists(tournaments_file_path())

def players_file_path():
    return get_file_path("players.json")

def players_file_path_exists():
    return os.path.exists(players_file_path())
