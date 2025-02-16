import json
import os


def save_to_json(data, filename, folder='data/tournaments'):
    """Save data to a JSON file."""
    data_folder = os.path.join(os.getcwd(), folder)
    os.makedirs(data_folder, exist_ok=True)
    file_path = os.path.join(data_folder, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
