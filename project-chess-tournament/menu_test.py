from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from models.player import Player
from models.tournament import Tournament
from models.pairing_perso import PairingPerso
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament


# Tournament creation
view = ViewTournament()
controller = ControllerTournament(view)

def add_players_json():
    """Add players to JSON"""
    view_player = ViewPlayer()
    controller_player = ControllerPlayer(view_player)
    controller_player.add_players_to_json()

def new_tournament_test():
    """Tournament variable for testing"""
    tournament = Tournament("Championnat de Paris", "Paris",
                            "01/06/2025", "07/06/2025")
    controller.entering_a_tournament(tournament)

def get_players_test():
    """Ajouter des joueurs pour tester"""
    return [Player("A", "Jean", "12/11/1985", "AB12345"),
               Player("B", "Alain", "12/11/1985", "CD67890"),
               Player("C", "Richard", "28/10/1955", "EF54321"),
               Player("D", "Marc", "23/06/1942", "GH98765"),
               Player("E", "Antoine", "23/06/1942", "II98765"),
               Player("F", "Christophe", "20/07/1990", "ZZ98765")]

def add_players_test():
    """Ajouter des joueurs pour tester"""
    players = get_players_test()
    for player in players:
        controller.add_player(player)

def pairing_test():
    players = get_players_test()
    first = [
        (players[0], players[1]), 
        (players[2], players[3]), 
        (players[4], players[5]), 
        (players[0], players[2])
    ]
    pairs = PairingPerso.generate_next_round_pairs(players, first)
    print(first)
    print(pairs)

def save_players_test():
    """Save players to JSON for testing."""
    players = get_players_test()
    controller_player = ControllerPlayer(ViewPlayer())
    controller_player.save_players_to_json(players)

def new_tournament_and_add_players_test():
    new_tournament_test()
    add_players_test()

TEST = {
    80: ("Ajouter un joueur (JSON)", add_players_json),
    81: ("Nouveau tournoi", new_tournament_test),
    82: ("Ajouter des joueurs au tournoi", add_players_test),
    83: ("Nouveau tournoi + Ajouter des joueurs",
         new_tournament_and_add_players_test),
    84: ("Pairing", pairing_test),
    85: ("Sauvegarder les joueurs en JSON", save_players_test)
    }