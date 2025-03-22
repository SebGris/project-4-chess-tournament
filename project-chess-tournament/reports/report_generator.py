from reports.player_report_generator import PlayerReportGenerator


class ReportGenerator:
    def __init__(self):
        pass

    def generate_players_report(self, players):

        report_generator = PlayerReportGenerator(players)
        report_generator.generate_report()
        report_generator.serve_report()
