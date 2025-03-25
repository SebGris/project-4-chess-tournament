from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.application_menu import ApplicationMenu
from repositories.match_repository import MatchRepository
from repositories.player_repository import PlayerRepository
from repositories.round_repository import RoundRepository
from repositories.tournament_repository import TournamentRepository
from views.player_view import PlayerView
from views.tournament_view import TournamentView


class Application:
    def __init__(self, application_menu: ApplicationMenu):
        self.application_menu = application_menu
        self._initialize_controllers()

    def _initialize_controllers(self):
        """Initialise les contrôleurs et les dépendances."""
        player_repository = PlayerRepository()
        tournament_repository = TournamentRepository()
        round_repository = RoundRepository()
        match_repository = MatchRepository()
        tournament_view = TournamentView()
        player_view = PlayerView()
        self.player_controller = PlayerController(
            player_repository, player_view
        )
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
        file_menu = self._get_file_menu_options()
        tournament_count = len(self.tournament_controller.get_tournaments())
        if tournament_count > 0:
            file_menu.extend(self._get_tournament_menu_options())
        file_menu.extend(self._get_quit_menu_option())
        plural_suffix = "s" if tournament_count > 1 else ""
        self.application_menu.add_group(
            f"Menu Fichier ({tournament_count} tournoi{plural_suffix})",
            file_menu
        )
        self.application_menu.add_group(
            "Menu Rapport", self._get_report_menu_options()
        )
        active_tournament = self.tournament_controller.get_active_tournament()
        if active_tournament:
            self.application_menu.add_group(
                f"Menu Tournoi : {active_tournament.name}",
                self._get_tournament_active_menu_options()
            )
            self.application_menu.add_group(
                f"Menu Rapport : {active_tournament.name}",
                self._get_report_tournament_menu_options()
            )
        return self.application_menu

    def _get_tournament_active_menu_options(self):
        return [
            {
                "label": "Afficher le tournoi",
                "command": self._show_tournament
            },
            {
                "label": "Afficher les joueurs",
                "command": self.tournament_controller.display_players,
            },
            {
                "label": "Modifier la description",
                "command": self.tournament_controller.update_description
            },
            {
                "label": "Modifier le nombre de tours",
                "command": self.tournament_controller.update_total_rounds
            },
            {
                "label": "Ajouter des joueurs",
                "command": self.tournament_controller.add_players
            },
            {
                "label": "Démarrer un round",
                "command": self.tournament_controller.start_round
            },
            {
                "label": "Saisir les scores",
                "command": self.tournament_controller.enter_scores
            },
        ]

    def _show_tournament(self):
        """Affiche les détails du tournoi actif."""
        self.tournament_controller.display_active_tournament_details()
        self.tournament_controller.display_player_names()
        self.tournament_controller.display_current_round_info()
        self.tournament_controller.display_player_pairs()

    def _get_report_tournament_menu_options(self):
        return [
            {
                "label": "Nom et dates du tournoi",
                "command": self.tournament_controller.report_name_dates
            },
            {
                "label": "Liste des joueurs du tournoi",
                "command": self.tournament_controller.report_players
            },
            {
                "label": "Liste des tours du tournoi et de leurs matchs",
                "command": self.tournament_controller.report_rounds_matches
            },
        ]

    def _get_file_menu_options(self):
        return [
            {
                "label": "Saisir des joueurs",
                "command": self.player_controller.add_players
            },
            {
                "label": "Nouveau tournoi",
                "command": self.tournament_controller.create_new_tournament
            },
        ]

    def _get_tournament_menu_options(self):
        return [
            {
                "label": "Sélectionner un tournoi",
                "command": self.tournament_controller.select_tournament
            },
            {
                "label": "Afficher tous les tournois",
                "command": self.tournament_controller.
                display_tournaments_details
            },
        ]

    def _get_quit_menu_option(self):
        return [
            {
                "label": "Quitter",
                "command": self._quit
            }
        ]

    def _quit(self):
        """Quitte l'application."""
        print("Au revoir !")
        exit()

    def _get_report_menu_options(self):
        return [
            {
                "label": "Liste de tous les joueurs",
                "command": self.player_controller.report_players
            },
            {
                "label": "Liste de tous les tournois",
                "command": self.tournament_controller.report_tournaments
            },
        ]
