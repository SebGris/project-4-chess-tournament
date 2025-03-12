import json
from models.tournament import Tournament
from models.base_repository import BaseRepository


class TournamentRepository(BaseRepository):
    FILE_PATH = "tournaments.json"

    def get_all_tournaments(self):
        with open(self.FILE_PATH, "r") as file:
            tournaments_dict = json.load(file)
        return [Tournament.from_dict(tournament) for tournament in tournaments_dict]

    def find_tournament_by_id(self, tournament_id):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                return tournament
        return None

    def create_tournament(self, tournament):
        tournaments = self.get_all_tournaments()
        tournaments.append(tournament)
        with open(self.FILE_PATH, "w") as file:
            json.dump(
                [tournament.to_dict() for tournament in tournaments], file, indent=4
            )
        return tournament

    def update_tournament(self, tournament_id, updated_data):
        tournaments = self.get_all_tournaments()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                tournament.name = updated_data["name"]
                tournament.date = updated_data["date"]
                with open(self.FILE_PATH, "w") as file:
                    json.dump(
                        [tournament.to_dict() for tournament in tournaments],
                        file,
                        indent=4,
                    )
                return tournament
        return None
