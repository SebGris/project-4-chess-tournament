from commands.command import QuitCommand
from models.menu import Menu
from models.tournament import Tournament
from controllers.base_controller import BaseController
from views.view import View
from controllers.controller_tournament import ControllerTournament


class Controller(BaseController):
    """Manages the logic of the tournament."""

    def __init__(self,):
        self.tournament = Tournament()
        self.view = View()
        self.menu = Menu()
        self.tournament_controller = ControllerTournament(
            self.tournament)

    def run(self):
        while True:
            self.menu = Menu()  # Reset menu for each iteration
            if self.tournament.is_loaded:
                self.menu.add_group("Tournoi", [
                    {
                        "label": "Afficher le tournoi",
                        "command": self.tournament_controller
                                    .display_tournament},
                    {
                        "label": "Sauvegarder le tournoi",
                        "command": self.tournament_controller.save_tournament
                    }
                ])
                self.menu.add_group("Général", [
                    {"label": "Quitter", "command": QuitCommand().execute}
                ])
            else:
                self.menu.add_group("Tournoi", [
                    {
                        "label": "Charger un tournoi",
                        "command": self.tournament_controller.load_tournament
                    }
                ])
                self.menu.add_group("Général", [
                    {"label": "Quitter", "command": QuitCommand().execute}
                ])

            self.view.display_menu(self.menu)
            choice = self.view.get_user_choice()

            try:
                choice_index = int(choice) - 1
                flat_menu = [
                    item for group in self.menu.get_groups()
                    for item in group['items']
                ]
                if 0 <= choice_index < len(flat_menu):
                    command = flat_menu[choice_index]["command"]
                    command()
                else:
                    raise ValueError("Invalid choice")
            except (IndexError, ValueError):
                self.view.display_message(
                    "Option invalide, veuillez réessayer."
                )
