from reports.report_generator import ReportGenerator
from views.base_player_view import BasePlayerView


class PlayerView(BasePlayerView):

    def display_add_player_message(self):
        print("Ajout de joueurs directement dans le fichier JSON.")

    def report_players(self, list_of_players):
        report_generator = ReportGenerator()
        report_generator.generate_players_report(list_of_players)
