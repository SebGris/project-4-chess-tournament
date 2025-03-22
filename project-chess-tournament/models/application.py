from controllers.tournament_controller import TournamentController
from models.application_menu import ApplicationMenu
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository
from repositories.tournament_repository import TournamentRepository
from views.tournament_view import TournamentView


class Application:
    def __init__(self, application_menu: ApplicationMenu):
        self.application_menu = application_menu
        player_repository = PlayerRepository()
        tournament_repository = TournamentRepository()
        round_repository = RoundRepository()
        match_repository = MatchRepository()
        tournament_view = TournamentView()
        self.tournament_controller = TournamentController(
            tournament_repository,
            player_repository,
            round_repository,
            match_repository,
            tournament_view
        )

    def get_refresh_menu(self):
        self.application_menu.clear_menu()
        self.application_menu.add_title("Application tournois d'échecs")
        self._add_general_menu()
        active_tournament = self.tournament_controller.get_active_tournament()
        if active_tournament:
            self._add_tournament_menu(active_tournament.name)
        return self.application_menu

    def _add_tournament_menu(self, name):
        def show_tournament():
            self.tournament_controller.display_active_tournament_details()
            self.tournament_controller.display_player_names()
            self.tournament_controller.display_current_round_info()
            self.tournament_controller.display_player_pairs()
        self.application_menu.add_group(
            "Menu Tournoi : {}".format(name),
            [
                {
                    "label": "Afficher le tournoi",
                    "command": show_tournament,
                },
                {
                    "label": "Afficher les joueurs",
                    "command": self.tournament_controller.display_players,
                },
                {
                    "label": "Modifier la description",
                    "command": self.tournament_controller.update_description,
                },
                {
                    "label": "Modifier le nombre de tours",
                    "command": self.tournament_controller.update_total_of_rounds,
                },
                {
                    "label": "Ajouter des joueurs",
                    "command": self.tournament_controller.add_players,
                },
                {
                    "label": "Démarrer un round",
                    "command": self.tournament_controller.start_round,
                },
                {
                    "label": "Saisir les scores",
                    "command": self.tournament_controller.enter_scores
                },
            ],
        )

    def _add_general_menu(self):
        self.application_menu.add_group(
            "Menu Fichier",
            [
                {
                    "label": "Nouveau tournoi",
                    "command": self.tournament_controller.create_new_tournament,
                },
                {
                    "label": "Sélectionner un tournoi",
                    "command": self.tournament_controller.select_tournament,
                },
                {
                    "label": "Afficher tous les tournois",
                    "command": self.tournament_controller.display_all_tournaments_details,
                },
                {
                    "label": "Quitter",
                    "command": self.quit,
                },
            ],
        )

    def quit(self):
        print("Au revoir !")
        exit()
