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
from repositories.player_repository import PlayerRepository
from repositories.tournament_repository import TournamentRepository
from views.tournament_view import TournamentView


class Application:
    def __init__(self, application_menu):
        self.application_menu = application_menu
        player_repository = PlayerRepository()
        tournament_repository = TournamentRepository()
        tournament_view = TournamentView()
        self.tournament_controller = TournamentController(
            tournament_repository, player_repository, tournament_view
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
        self.application_menu.add_group(
            "Menu Tournoi : {}".format(name),
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
        self.application_menu.add_group(
            "Menu Général",
            [
                {
                    "label": "Nouveau tournoi",
                    "command": NewTournamentCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Sélectionner un tournoi",
                    "command": SelectTournamentCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Afficher tous les tournois",
                    "command": ShowTournamentsDetailsCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Quitter",
                    "command": QuitCommand().execute
                },
            ],
        )
