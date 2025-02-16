import json
import os


def get_file_path(filename, folder='data/tournaments'):
    """Get the full file path for the given filename and folder."""
    data_folder = os.path.join(os.getcwd(), folder)
    os.makedirs(data_folder, exist_ok=True)
    return os.path.join(data_folder, filename)


def save_to_json(data, filename):
    """Save data to a JSON file."""
    file_path = get_file_path(filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def load_from_json(filename):
    """Load data from a JSON file."""
    file_path = get_file_path(filename)
    with open(file_path, 'r') as file:
        return json.load(file)
