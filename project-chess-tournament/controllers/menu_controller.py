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
            "Nouveau tournoi": self.new_tournament,
            "Ajouter des joueurs": self.add_players,
            "Afficher les joueurs": self.display_players,
            "Démarrer un tournoi": self.start_tournament,
            "Ajouter une description au tournoi": 
                self.add_description_tournament,
            "Afficher le tournoi": self.display_tournament,
            "Test": self.test,
            "Ajoute un nouveau tournoi": self.add_new_tournament_test,
            "Ajouter des joueurs au tournoi": self.add_players_test,
            "Nouveau tournoi + Ajouter des joueurs": 
                self.new_tournament_and_add_players_test,
            "Pairing": self.pairing_test,
            "Sauvegarder les joueurs et tournoi en JSON":
                self.save_players_test,
            "Retour au menu principal": self.show_main_menu
            }

    def show_main_menu(self):
        self.display_menu("Menu principal",self.model.get_main_menu_options())

    def show_test_items(self):
        self.display_menu("Menu test",self.model.get_test_items_menu_options())

    def display_menu(self, title, options):
        while True:
            self.view.display_menu(title, options)
            choice = input(
                "Sélectionnez une option (1-{}) :".format(len(options))
            )
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(options):
                    selected_option = options[choice - 1]
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
    
    def new_tournament(self):
        """Start new tournament"""
        controller.entering_a_tournament()

    def add_players(self):
        """Adding players to the tournament"""
        controller.add_players()

    def display_players(self):
        """Display players in the tournament"""
        controller.display_players()

    def start_tournament(self):
        """Starting a tournament"""
        controller.start_tournament()

    def add_description_tournament(self):
        """Add a description to the tournament"""
        controller.add_description()

    def display_tournament(self):
        """Display the tournament"""
        controller.display_tournament()
    
    def test(self):
        self.show_test_items()

    # début menu test
    def add_new_tournament_test(self):
        """Tournament variable for testing"""
        tournament = Tournament("Championnat de Paris", "Paris",
                                "01/06/2025", "07/06/2025")
        controller.entering_a_tournament(tournament)

    def get_players_test(self):
        """Ajouter des joueurs pour tester"""
        return [Player("A", "Jean", "12/11/1985", "AB12345"),
                Player("B", "Alain", "12/11/1985", "CD67890"),
                Player("C", "Richard", "28/10/1955", "EF54321"),
                Player("D", "Marc", "23/06/1942", "GH98765"),
                Player("E", "Antoine", "23/06/1942", "II98765"),
                Player("F", "Christophe", "20/07/1990", "ZZ98765")]

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
