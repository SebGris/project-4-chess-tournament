import os


def get_file_path(filename, folder='data/tournaments'):
    """Get the full file path for the given filename and folder."""
    data_folder = os.path.join(os.getcwd(), folder)
    os.makedirs(data_folder, exist_ok=True)
    return os.path.join(data_folder, filename)


def tournaments_file_path():
    return get_file_path("tournaments.json")


def players_file_path():
    return get_file_path("players.json")
