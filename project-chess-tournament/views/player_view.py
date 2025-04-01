from reports.report_generator import ReportGenerator
from views.base_player_view import BasePlayerView


class PlayerView(BasePlayerView):
    """Class to manage the player view in the chess tournament application."""

    def display_add_player_message(self):
        """Display a message indicating that players are being added directly to the JSON file."""
        print("Ajout de joueurs directement dans le fichier JSON.")

    def report_players(self, list_of_players):
        """Generate a report of players using the ReportGenerator class."""
        report_generator = ReportGenerator()
        report_generator.generate_players_report(list_of_players)
