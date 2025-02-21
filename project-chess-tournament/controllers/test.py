import random
from controllers.controller_tournament import ControllerTournament
from views.view_tournament import View
# import pour test
from models.player import Player
from models.pairing import Pairing
from controllers.controller_player import ControllerPlayer
from views.view_player import ViewPlayer

# Tournament creation
tournament_view = View()
tournament_controller = ControllerTournament(tournament_view)
player_view = ViewPlayer()
player_controller = ControllerPlayer(player_view)


def get_random_players(number=6):
    """Generate players for testing"""
    players_data = []
    if number > 0:
        last_names = ["Jean", "Alain", "Richard", "Marc", "Antoine"]
        first_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for id in range(number):
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
            players_data.append(
                (
                    first_name, last_name, birth_date,
                    id_chess, id+1
                )
            )
    else:
        players_data = [
            ("A", "Jean", "12/11/1985", "AB12345", 1),
            ("B", "Alain", "12/11/1985", "CD67890", 2),
            ("C", "Richard", "28/10/1955", "EF54321", 3),
            ("D", "Marc", "23/06/1942", "GH98765", 4),
            ("E", "Antoine", "23/06/1942", "II98765", 5),
            ("F", "Christophe", "20/07/1990", "ZZ98765", 6)
        ]
    # Unpacking each tuple in players_data into the Player constructor
    players = [Player(*data) for data in players_data]
    for player in players:
        player.update_score(round(random.uniform(0, 10), 1))
    print("Joueurs générés pour test :")
    print(players)
    return players


def add_players_test(self, score_0=True):
    """Ajouter des joueurs pour tester"""
    players = self.get_random_players()
    if score_0:
        for player in players:
            player.reset_score()
    tournament_controller.add_players(players)
    tournament_controller.display_tournament_players()


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
    tournament_controller.save_tournament(save_with_players=True)


def new_tournament_and_add_players_test(self):
    self.add_new_tournament_test()
    self.add_players_test(False)
