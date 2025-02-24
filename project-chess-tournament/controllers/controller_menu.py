from commands.command import QuitCommand
from models.tournament import Tournament
from controllers.controller_tournament import ControllerTournament


class ControllerMenu():
    """Manages the logic of the tournament."""

    def __init__(self, menu, view):
        self.menu = menu
        self.view = view
        self.tournament = Tournament()
        self.tournament_controller = ControllerTournament(
            self.tournament, self.menu, self.view
        )

    def run(self):
        while True:
            self.menu.clear_menu()
            if self.menu.is_tournament_loaded():
                self.menu.add_group("Menu Tournoi", [
                    {
                        "label": "Afficher le tournoi",
                        "command": self.tournament_controller
                                    .display_tournament},
                    {
                        "label": "Ajouter une description",
                        "command": self.tournament_controller.add_description
                    },
                    {
                        "label": "Ajouter des joueurs",
                        "command": self.tournament_controller.add_players
                    },
                    {
                        "label": "Démarrer un tournoi",
                        "command": self.tournament_controller.start_tournament
                    },
                    {
                        "label": "Modifier le nombre de tours",
                        "command":
                        self.tournament_controller.update_number_of_rounds
                    },
                    {
                        "label": "Saisir les scores",
                        "command": self.tournament_controller.record_results
                    }
                ])
            else:
                self.menu.add_group("Menu Tournoi", [
                    {
                        "label": "Nouveau tournoi",
                        "command": self.tournament_controller.new_tournament
                    },
                    {
                        "label": "Charger un tournoi",
                        "command": self.tournament_controller.load_tournament
                    }
                ])
            self.menu.add_group("Menu Général", [
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
