from commands.command import QuitCommand

class MenuStateManager:
    def __init__(self, menu, tournament_controller):
        self.menu = menu
        self.tournament_controller = tournament_controller

    def update_menu(self):
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
        self.menu.add_group("Menu Général", [{"label": "Quitter", "command": QuitCommand().execute}])