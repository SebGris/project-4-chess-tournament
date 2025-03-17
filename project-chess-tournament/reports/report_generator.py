from models.tournament import Tournament
from reports.tournament_report_generator import TournamentReportGenerator
from repositories.tournament_repository import TournamentRepository
from repositories.player_repository import PlayerRepository
from repositories.match_repository import MatchRepository
from repositories.round_repository import RoundRepository


class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self):
        # Lire les données des fichiers JSON
        tournament_repository = TournamentRepository()
        player_repository = PlayerRepository()
        match_repository = MatchRepository()
        round_repository = RoundRepository()

        tournaments_dto = tournament_repository.get_tournaments()
        # players_dto = player_repository.get_players()
        # matches_dto = match_repository.get_matches()
        # rounds_dto = round_repository.get_rounds()

        tournaments = [
            Tournament.from_dto(
                tournament_dto, player_repository, round_repository, match_repository
            ) for tournament_dto in tournaments_dto
        ]
        # Mettre à jour les scores des joueurs
        for tournament in tournaments:
            tournament.update_scores()
        tournaments_with_scores = [tournament for tournament in tournaments]
        # Construire la tournament_list
        tournament_list = []
        for tournament in tournaments_with_scores:
            tournament_dict = tournament.to_dto().to_dict()
            tournament_dict["players"] = [
                player.to_dict() for player in tournament.players
            ]
            # tournament_dict["rounds"] = [
            #     round.to_dto().to_dict() for round in tournament.rounds
            # ]
            # for round in tournament_dict["rounds"]:
            #     round["matches"] = [
            #         match.to_dict() for match in matches_dto if match.id in round["match_ids"]
            #     ]
            print(tournament_dict)
            tournament_list.append(tournament_dict)

        report_generator = TournamentReportGenerator(tournament_list)
        report_generator.generate_report()
        report_generator.serve_report()
