from controllers.tournament_controller import TournamentController
from commands.composite_command import CompositeCommand
from menu_commands.add_players_command import AddPlayersCommand
from menu_commands.new_tournament_command import NewTournamentCommand
from menu_commands.enter_scores_command import EnterScoresCommand
from menu_commands.quit_command import QuitCommand
from menu_commands.select_tournament_command import SelectTournamentCommand
from menu_commands.show_current_round import ShowCurrentRound
from menu_commands.show_player_names_command import ShowPlayerNamesCommand
from menu_commands.show_player_pairs_command import ShowPlayerPairsCommand
from menu_commands.show_players_command import ShowPlayersCommand
from menu_commands.show_tournament_details_command import ShowTournamentDetailsCommand
from menu_commands.show_tournaments_details_command import ShowTournamentsDetailsCommand
from menu_commands.start_tournament_command import StartTournamentCommand
from menu_commands.update_description_command import UpdateDescriptionCommand
from menu_commands.update_number_of_rounds_command import UpdateNumberOfRoundsCommand
from models.tournament_menu import TournamentMenu
from models.player_repository import PlayerRepository
from models.tournament_manager import TournamentManager
from models.tournament_repository import TournamentRepository
from views.tournament_view import TournamentView


class Application:
    def __init__(self):
        player_repository = PlayerRepository()
        tournament_repository = TournamentRepository(player_repository)
        self.tournament_manager = TournamentManager(tournament_repository)
        self.tournament_view = TournamentView()
        self.tournament_controller = TournamentController(
            self.tournament_manager, self.tournament_view
        )
        self.menu = TournamentMenu()

    def get_refresh_menu(self):
        self.menu.clear_menu()
        self._set_tournament_app_title()
        self._add_general_menu()
        active_tournament = self.tournament_manager.get_active_tournament()
        if active_tournament:
            self._add_tournament_menu(active_tournament.name)
        return self.menu

    def _set_tournament_app_title(self):
        self.menu.add_group("Application tournois d'échecs", [])

    def _add_tournament_menu(self, name):
        show_tournament_composite_com = CompositeCommand()
        show_tournament_composite_com.add_command(
            ShowTournamentDetailsCommand(self.tournament_controller)
        )
        show_tournament_composite_com.add_command(
            ShowPlayerNamesCommand(self.tournament_controller)
        )
        show_tournament_composite_com.add_command(
            ShowCurrentRound(self.tournament_controller)
        )
        show_tournament_composite_com.add_command(
            ShowPlayerPairsCommand(self.tournament_controller)
        )
        self.menu.add_group(
            "Tournoi : {}".format(name),
            [
                {
                    "label": "Afficher le tournoi",
                    "command": show_tournament_composite_com.execute,
                },
                {
                    "label": "Afficher les joueurs",
                    "command": ShowPlayersCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Modifier la description",
                    "command": UpdateDescriptionCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Ajouter des joueurs",
                    "command": AddPlayersCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Démarrer un tournoi",
                    "command": StartTournamentCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Modifier le nombre de tours",
                    "command": UpdateNumberOfRoundsCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Saisir les scores",
                    "command": EnterScoresCommand(self.tournament_controller).execute,
                },
            ],
        )

    def _add_general_menu(self):
        new_tournament_composite_command = CompositeCommand()
        new_tournament_composite_command.add_command(
            NewTournamentCommand(self.tournament_controller)
        )
        new_tournament_composite_command.add_command(
            SelectTournamentCommand(self.tournament_controller)
        )
        self.menu.add_group(
            "Menu Général",
            [
                {
                    "label": "Nouveau tournoi",
                    "command": new_tournament_composite_command.execute,
                },
                {
                    "label": "Sélectionner un tournoi",
                    "command": SelectTournamentCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Afficher tous les tournois",
                    "command": ShowTournamentsDetailsCommand(self.tournament_controller).execute,
                },
                {"label": "Quitter", "command": QuitCommand().execute},
            ],
        )
