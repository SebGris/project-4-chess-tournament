from reports.report_generator import ReportGenerator
from views.base_player_view import BasePlayerView


class PlayerView(BasePlayerView):

    def request_player_addition_confirmation(self):
        return self.get_user_confirmation("Voulez-vous ajouter des joueurs ?")

    def get_user_confirmation(self, prompt):
        while True:
            response = self.input(f"{prompt} (oui/non):").lower()
            if response in ["oui", "non"]:
                return response == "oui"
            else:
                print("Réponse invalide.")
                print("Veuillez répondre par 'oui' ou 'non'.")

    def report_players(self, list_of_players):
        report_generator = ReportGenerator()
        report_generator.generate_players_report(list_of_players)
