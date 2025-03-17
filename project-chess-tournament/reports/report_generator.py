from reports.tournament_report_generator import TournamentReportGenerator


class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self):
        # Exemple d'utilisation
        tournaments = [
            {
                "tournament_id": 1,
                "name": "Tournoi de Printemps",
                "players": [
                    {"player_id": 101, "name": "John Doe", "score": 50},
                    {"player_id": 102, "name": "Jane Smith", "score": 60},
                ]
            },
            {
                "tournament_id": 2,
                "name": "Tournoi d'Été",
                "players": [
                    {"player_id": 103, "name": "Alice Johnson", "score": 70},
                    {"player_id": 104, "name": "Bob Brown", "score": 80},
                ]
            }
        ]

        report_generator = TournamentReportGenerator(tournaments)
        report_generator.generate_report()
        report_generator.serve_report()
