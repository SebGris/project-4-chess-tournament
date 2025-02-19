from commands.command import (
    ChangeMenuCommand, 
    AddPlayersCommand, LoadPlayersCommand, DisplayPlayersCommand,
    NewTournamentCommand, AddPlayersToTournamentCommand, LoadTournamentCommand, StartTournamentCommand,
    DisplayTournamentsCommand, AddDescriptionCommand, DisplayTournamentPlayersCommand,
    QuitCommand
)
from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament


tournament_view = ViewTournament()
tournament_controller = ControllerTournament(tournament_view)
player_view = ViewPlayer()
player_controller = ControllerPlayer(player_view)

class MenuController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.commands = {
            "Gestion des tournois": ChangeMenuCommand(
                self, "tournament", "Gestion des tournois"
            ),
            "Gestion des joueurs": ChangeMenuCommand(
                self, "player", "Gestion des joueurs"
            ),
            "Menu pour test": ChangeMenuCommand(
                self, "test", "Menu pour test"
            ),
            "Retour au menu principal": ChangeMenuCommand(
                self, "main", "Menu principal"
            ),
            "Ajouter des joueurs": AddPlayersCommand(player_controller),
            "Charger les joueurs": LoadPlayersCommand(player_controller),
            "Afficher les joueurs": DisplayPlayersCommand(player_controller),
            "Nouveau tournoi": NewTournamentCommand(tournament_controller),
            "Ajouter des joueurs au tournoi": AddPlayersToTournamentCommand(tournament_controller),
            "Charger un tournoi": LoadTournamentCommand(tournament_controller),
            "Démarrer un tournoi": StartTournamentCommand(tournament_controller),
            "Afficher les tournois": DisplayTournamentsCommand(tournament_controller),
            "Ajouter une description": AddDescriptionCommand(tournament_controller),
            "Afficher les joueurs du tournoi": DisplayTournamentPlayersCommand(tournament_controller),
            # "Afficher le résultat du tournoi": tournament_controller.show_results,
            # "Ajoute un tournoi": self.add_new_tournament_test,
            # "Ajouter des joueurs au tournoi (score 0)": self.add_players_test,
            # "Nouveau tournoi + Ajouter des joueurs":
            #     self.new_tournament_and_add_players_test,
            # "Pairing": self.pairing_test,
            # "Sauvegarder les joueurs et tournoi en JSON":
            #     self.save_players_test,
            "Quitter": QuitCommand()
            }

    def start_menu_navigation(self, menu_name="main",
                              menu_title="Menu principal"):
        while True:
            options = self.model.get_menu_navigation(menu_name)
            self.view.display_menu(menu_title, options)
            try:
                choice = int(self.view.get_user_choice(len(options)))
                if 1 <= choice <= len(options):
                    self.execute_command(options[choice - 1])
                else:
                    self.view.display_invalid_option_message_try_again()
            except ValueError:
                self.view.display_invalid_input_message_enter_a_number()

    def execute_command(self, selected_option):
        command = self.commands.get(selected_option)
        if command:
            command.execute()
        else:
            self.view.display_invalid_option_message_try_again()
