from controllers.controller_tournament import ControllerTournament
from views.view_tournament import ViewTournament
# import pour test
from models.player import Player
from models.tournament import Tournament
from models.pairing_perso import PairingPerso
from controllers.controller_player import ControllerPlayer
from views.view_player import ViewPlayer

# Tournament creation
view = ViewTournament()
controller = ControllerTournament(view)


class MenuController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.actions = {
            "Gestion des tournois": lambda: self.show_menu(
                "tournament", "Gestion des tournois"
            ),
            "Gestion des joueurs": lambda: self.show_menu(
                "player", "Gestion des joueurs"
            ),
            "Menu pour test": lambda: self.show_menu(
                "test", "Menu pour test"
            ),
            "Nouveau tournoi": controller.entering_a_tournament,
            "Ajouter des joueurs": controller.add_players,
            "Afficher les joueurs": controller.display_players,
            "Démarrer un tournoi": controller.start_tournament,
            "Ajouter une description": controller.add_description,
            "Afficher le tournoi": controller.display_tournament,
            "Ajoute un tournoi": self.add_new_tournament_test,
            "Ajouter des joueurs au tournoi": self.add_players_test,
            "Nouveau tournoi + Ajouter des joueurs":
                self.new_tournament_and_add_players_test,
            "Pairing": self.pairing_test,
            "Sauvegarder les joueurs et tournoi en JSON":
                self.save_players_test,
            "Retour au menu principal": self.show_menu
            }

    def show_menu(self, menu_name="main", menu_title="Menu principal"):
        items = self.model.get_menu_items(menu_name)
        self.view.display_menu(menu_title, items)
        while True:
            choice = input(
                "Sélectionnez une option (1-{}) :".format(len(items))
            )
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(items):
                    selected_option = items[choice - 1]
                    if selected_option == "Quitter":
                        exit()
                    else:
                        action = self.actions.get(selected_option)
                        if action:
                            action()
                        else:
                            self.view.display_message(
                                f"Aucune action définie pour "
                                f"{selected_option}."
                            )
                else:
                    self.view.display_message(
                        "Option invalide. Veuillez réessayer."
                    )
            else:
                self.view.display_message(
                    "Entrée invalide. Veuillez entrer un nombre."
                )

    def add_new_tournament_test(self):
        """Tournament variable for testing"""
        controller.entering_a_tournament(
            Tournament(
                "Championnat de Paris", "Paris", "01/06/2025", "07/06/2025"
            )
        )

    def get_players_test(self):
        """Ajouter des joueurs pour tester"""
        players_data = [
            ("A", "Jean", "12/11/1985", "AB12345"),
            ("B", "Alain", "12/11/1985", "CD67890"),
            ("C", "Richard", "28/10/1955", "EF54321"),
            ("D", "Marc", "23/06/1942", "GH98765"),
            ("E", "Antoine", "23/06/1942", "II98765"),
            ("F", "Christophe", "20/07/1990", "ZZ98765")
        ]
        # Unpacking each tuple in players_data into the Player constructor
        return [Player(*data) for data in players_data]

    def add_players_test(self):
        """Ajouter des joueurs pour tester"""
        players = self.get_players_test()
        for player in players:
            controller.add_player(player)

    def pairing_test(self):
        players = self.get_players_test()
        first = [
            (players[0], players[1]),
            (players[2], players[3]),
            (players[4], players[5]),
            (players[0], players[2])
        ]
        pairs = PairingPerso.generate_next_round_pairs(players, first)
        print(first)
        print(pairs)

    def save_players_test(self):
        """Save players to JSON for testing."""
        controller_player = ControllerPlayer(ViewPlayer())
        controller_player.add_players(self.get_players_test())
        controller_player.save_players_to_json()
        self.add_new_tournament_test()
        controller.save_tournament_to_json()

    def new_tournament_and_add_players_test(self):
        self.add_new_tournament_test()
        self.add_players_test()
