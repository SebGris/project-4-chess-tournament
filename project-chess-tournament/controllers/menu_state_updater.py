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


class MenuStateUpdater:
    def __init__(self, menu, tournament_controller):
        self.menu = menu
        self.tournament_controller = tournament_controller

    def refresh_menu(self):
        self.menu.clear_menu()
        self._set_tournament_app_title()
        self._add_general_menu()
        if self.menu.is_tournament_loaded():
            self._add_tournament_menu()

    def _set_tournament_app_title(self):
        self.menu.add_group("Application tournois d'échecs", [])

    def _add_tournament_menu(self):
        show_tournament_composite_command = CompositeCommand()
        show_tournament_composite_command.add_command(
            ShowTournamentDetailsCommand(self.tournament_controller)
        )
        show_tournament_composite_command.add_command(
            ShowPlayerNamesCommand(self.tournament_controller)
        )
        show_tournament_composite_command.add_command(
            ShowCurrentRound(self.tournament_controller)
        )
        show_tournament_composite_command.add_command(
            ShowPlayerPairsCommand(self.tournament_controller)
        )
        update_description_composite_command = CompositeCommand()
        update_description_composite_command.add_command(
            UpdateDescriptionCommand(self.tournament_controller)
        )
        update_rounds_composite_command = CompositeCommand()
        update_rounds_composite_command.add_command(
            UpdateNumberOfRoundsCommand(self.tournament_controller)
        )
        self.menu.add_group(
            "Menu Tournoi",
            [
                {
                    "label": "Afficher le tournoi",
                    "command": show_tournament_composite_command.execute,
                },
                {
                    "label": "Afficher les joueurs",
                    "command": ShowPlayersCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Modifier la description",
                    "command": update_description_composite_command.execute,
                },
                {
                    "label": "Ajouter des joueurs",
                    "command": AddPlayersCommand(self.tournament_controller).execute,
                },
                {
                    "label": "Démarrer un tournoi",
                    "command": StartTournamentCommand(
                        self.tournament_controller
                    ).execute,
                },
                {
                    "label": "Modifier le nombre de tours",
                    "command": update_rounds_composite_command.execute,
                },
                {
                    "label": "Saisir les scores",
                    "command": EnterScoresCommand(self.tournament_controller).execute,
                },
            ],
        )

    def _add_general_menu(self):
        create_tournament_composite_command = CompositeCommand()
        create_tournament_composite_command.add_command(
            CreateTournamentCommand(self.tournament_controller)
        )
        create_tournament_composite_command.add_command(
            SelectTournamentCommand(self.tournament_controller)
        )
        select_tournament_composite_command = CompositeCommand()
        select_tournament_composite_command.add_command(
            ShowAllTournamentsCommand(self.tournament_controller)
        )
        # select_tournament_composite_command.add_command(SelectTournamentCommand(self.tournament_controller))

        self.menu.add_group(
            "Menu Général",
            [
                {
                    "label": "Nouveau tournoi",
                    "command": create_tournament_composite_command.execute,
                },
                {
                    "label": "Sélectionner un tournoi",
                    "command": select_tournament_composite_command.execute,
                },
                {
                    "label": "Afficher tous les tournois",
                    "command": ShowTournamentsDetailsCommand(
                        self.tournament_controller
                    ).execute,
                },
                {"label": "Quitter", "command": QuitCommand().execute},
            ],
        )
