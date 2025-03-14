from controllers.tournament_controller import TournamentController
from commands.composite_command import CompositeCommand
from menu_commands.add_players_command import AddPlayersCommand
from menu_commands.create_tournament_command import CreateTournamentCommand
from menu_commands.enter_scores_command import EnterScoresCommand
from menu_commands.quit_command import QuitCommand
from menu_commands.select_tournament_command import SelectTournamentCommand
from menu_commands.show_all_tournaments_command import ShowAllTournamentsCommand
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


class MenuStateUpdater:
    def __init__(self, menu: TournamentMenu, controller: TournamentController):
        self.menu = menu
        self.controller = controller

    def refresh_menu(self):
        self.menu.clear_menu()
        self._set_tournament_app_title()
        self._add_general_menu()
        if self.menu.is_tournament_loaded():
            self._add_tournament_menu()

    def _set_tournament_app_title(self):
        self.menu.add_group("Application tournois d'échecs", [])

    def _add_tournament_menu(self):
        show_tournament_composite_com = CompositeCommand()
        show_tournament_composite_com.add_command(
            ShowTournamentDetailsCommand(self.controller)
        )
        show_tournament_composite_com.add_command(
            ShowPlayerNamesCommand(self.controller)
        )
        show_tournament_composite_com.add_command(ShowCurrentRound(self.controller))
        show_tournament_composite_com.add_command(
            ShowPlayerPairsCommand(self.controller)
        )
        update_description_composite_com = CompositeCommand()
        update_description_composite_com.add_command(
            UpdateDescriptionCommand(self.controller)
        )
        update_rounds_composite_command = CompositeCommand()
        update_rounds_composite_command.add_command(
            UpdateNumberOfRoundsCommand(self.controller)
        )
        self.menu.add_group(
            "Menu Tournoi",
            [
                {
                    "label": "Afficher le tournoi",
                    "command": show_tournament_composite_com.execute,
                },
                {
                    "label": "Afficher les joueurs",
                    "command": ShowPlayersCommand(self.controller).execute,
                },
                {
                    "label": "Modifier la description",
                    "command": update_description_composite_com.execute,
                },
                {
                    "label": "Ajouter des joueurs",
                    "command": AddPlayersCommand(self.controller).execute,
                },
                {
                    "label": "Démarrer un tournoi",
                    "command": StartTournamentCommand(self.controller).execute,
                },
                {
                    "label": "Modifier le nombre de tours",
                    "command": update_rounds_composite_command.execute,
                },
                {
                    "label": "Saisir les scores",
                    "command": EnterScoresCommand(self.controller).execute,
                },
            ],
        )

    def _add_general_menu(self):
        create_tournament_composite_com = CompositeCommand()
        create_tournament_composite_com.add_command(
            CreateTournamentCommand(self.controller)
        )
        create_tournament_composite_com.add_command(
            SelectTournamentCommand(self.controller)
        )
        select_tournament_composite_com = CompositeCommand()
        select_tournament_composite_com.add_command(
            ShowAllTournamentsCommand(self.controller)
        )
        # select_tournament_composite_command.add_command(SelectTournamentCommand(self.tournament_controller))

        self.menu.add_group(
            "Menu Général",
            [
                {
                    "label": "Nouveau tournoi",
                    "command": create_tournament_composite_com.execute,
                },
                {
                    "label": "Sélectionner un tournoi",
                    "command": select_tournament_composite_com.execute,
                },
                {
                    "label": "Afficher tous les tournois",
                    "command": ShowTournamentsDetailsCommand(self.controller).execute,
                },
                {"label": "Quitter", "command": QuitCommand().execute},
            ],
        )
