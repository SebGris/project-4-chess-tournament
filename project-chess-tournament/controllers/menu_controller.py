import random
from controllers.controller_tournament import ControllerTournament
from views.view_tournament import ViewTournament
# import pour test
from models.player import Player
from models.tournament import Tournament
from models.pairing import Pairing
from controllers.controller_player import ControllerPlayer
from views.view_player import ViewPlayer

# Tournament creation
tournament_view = ViewTournament()
tournament_controller = ControllerTournament(tournament_view)
player_view = ViewPlayer()
player_controller = ControllerPlayer(player_view)


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
            "Ajouter des joueurs": player_controller.add_players,
            "Charger les joueurs": player_controller.load_players_from_json,
            "Afficher les joueurs": player_controller.display_players,
            "Nouveau tournoi": tournament_controller.entering_a_tournament,
            "Charger un tournoi":
                tournament_controller.load_tournament_from_json,
            "Démarrer un tournoi": tournament_controller.start_tournament,
            "Ajouter une description": tournament_controller.add_description,
            "Afficher le tournoi": tournament_controller.display_tournament,
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
                    self.view.display_invalid_option_message_try_again()
            else:
                self.view.display_invalid_input_message_enter_a_number()

    def add_new_tournament_test(self, players=None):
        """Tournament variable for testing"""
        players = players or []
        tournament = Tournament(
            "Championnat de Paris", "Paris", "01/06/2025", "07/06/2025",
            players=players
        )
        tournament_controller.entering_a_tournament(tournament)

    def get_random_players(self, number=6):
        """Generate players for testing"""
        if number > 0:
            last_names = ["Jean", "Alain", "Richard", "Marc", "Antoine"]
            first_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
            players_data = []
            for _ in range(number):
                last_name = random.choice(last_names)
                first_name = random.choice(first_names)
                birth_date = "{:02d}/{:02d}/{}".format(
                    random.randint(1, 28),
                    random.randint(1, 12),
                    random.randint(1950, 2000)
                )
                random_letters = "".join(
                    random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2)
                )
                random_digits = "".join(random.choices("0123456789", k=5))
                id_chess = random_letters + random_digits
                score = round(random.uniform(0, 10), 1)
                players_data.append(
                    (
                        first_name, last_name, birth_date,
                        id_chess, number, score
                    )
                )
        else:
            players_data = [
                ("A", "Jean", "12/11/1985", "AB12345", 1, 5),
                ("B", "Alain", "12/11/1985", "CD67890", 2, 6),
                ("C", "Richard", "28/10/1955", "EF54321", 3, 7),
                ("D", "Marc", "23/06/1942", "GH98765", 4, 4),
                ("E", "Antoine", "23/06/1942", "II98765", 5, 3),
                ("F", "Christophe", "20/07/1990", "ZZ98765", 6, 8)
            ]
        # Unpacking each tuple in players_data into the Player constructor
        players = [Player(*data) for data in players_data]
        print("Joueurs générés pour test :")
        print(players)
        return players

    def add_players_test(self):
        """Ajouter des joueurs pour tester"""
        players = self.get_random_players()
        for player in players:
            tournament_controller.add_player(player)

    def pairing_test(self):
        try:
            total_players = int(input("Nombre de joueurs à tester : "))
        except ValueError:
            self.view.display_invalid_input_message_enter_a_number()
            return
        players = self.get_random_players(total_players)
        first = Pairing.generate_first_round_pairs(players)
        print("Premier tour (aléatoirement):")
        print(first)
        pairs = Pairing.generate_next_round_pairs(players, first)
        print("Deuxième tour (en fonction des scores):")
        print(pairs)

    def save_players_test(self):
        """Save players to JSON for testing."""
        controller_player = ControllerPlayer(ViewPlayer())
        controller_player.add_players(self.get_random_players())
        self.add_new_tournament_test(controller_player.players)
        tournament_controller.save_tournament_to_json(True)

    def new_tournament_and_add_players_test(self):
        self.add_new_tournament_test()
        self.add_players_test()
