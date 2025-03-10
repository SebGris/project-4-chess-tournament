from services.json_file_service import JsonFileService, tournaments_file_path, players_file_path, tournaments_file_path_exists, players_file_path_exists

class TournamentLoaderService:
    @staticmethod
    def load_tournaments():
        if not tournaments_file_path_exists():
            raise FileNotFoundError("Fichier de tournois introuvable.")
        return JsonFileService.load_from_file(tournaments_file_path())

    @staticmethod
    def load_players():
        if not players_file_path_exists():
            raise FileNotFoundError("Fichier de joueurs introuvable.")
        return JsonFileService.load_from_file(players_file_path())

    @staticmethod
    def save_players(players_data):
        """Sauvegarder les données des joueurs dans un fichier JSON."""
        JsonFileService.save_to_file(players_data, players_file_path())
