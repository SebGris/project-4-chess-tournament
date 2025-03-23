from reports.report_generator import ReportGenerator
from views.base_player_view import BasePlayerView


class PlayerView(BasePlayerView):

    def report_players(self, list_of_players):
        report_generator = ReportGenerator()
        report_generator.generate_players_report(list_of_players)
