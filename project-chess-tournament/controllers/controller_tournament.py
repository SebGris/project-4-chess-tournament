from models.player import Player
from models.round import Round
from models.match import Match


class ControllerTournament:
    """Controller for running the tournament and managing results."""
    def __init__(self, view, tournament, current_round=1):
        self.view = view
        self.tournament = tournament
        self.current_round = current_round
        self.rounds = []  # Liste des tours
        self.players = []  # Liste des joueurs enregistrés

    def add_player(self, player):
        """Add a player to the tournament."""
        self.tournament.add_player(player)

    def add_players_to_tournament(self):
        """Adds a player to the tournament
         by retrieving information from the view."""
        while True:
            counter = len(self.tournament.players) + 1
            player_info = self.view.prompt_for_player(counter)
            if player_info:
                last_name, first_name, date_of_birth, id_chess = player_info
                if not last_name:
                    return
                try:
                    # Crée un nouvel objet Player avec les informations
                    player = Player(last_name, first_name,
                                    date_of_birth, id_chess)
                    # Ajoute le joueur au tournoi
                    self.tournament.add_player(player)
                    self.view.show_message("Joueur ajouté avec succès.")
                except ValueError as e:
                    self.view.show_message(f"Erreur: {e}")
            else:
                self.view.show_message("Aucun joueur ajouté.")

    def start_round(self):
        """Commence un nouveau tour avec les matchs."""
        if self.current_round > self.number_of_rounds:
            print("Le tournoi est terminé.")
            return
        round_ = Round(self.current_round)
        self.rounds.append(round_)
        # Générer les matchs pour ce tour (matchs pairs de joueurs)
        for i in range(0, len(self.players), 2):
            if i + 1 < len(self.players):  # Assurer qu'il y a deux joueurs
                match = Match(self.players[i], self.players[i+1])
                round_.add_match(match)
        self.current_round += 1

    def start_next_round(self):
        """Starts the next round of the tournament."""
        self.tournament.start_round()

    def record_match_results(self):
        """Enregistre les résultats des matchs pour le tour courant."""
        if self.tournament.current_round > self.tournament.number_of_rounds:
            self.view.show_message("Le tournoi est terminé.")
            return
        current_round = self.tournament.rounds[self.tournament.current_round - 2]  # Le tour courant
        for match in current_round.matches:
            match.set_result(self.view.prompt_for_match_result(match))

    def set_result(self, result):
        """Assigns a result to the match."""
        # '1' pour la victoire du premier joueur,
        # '2' pour la victoire du deuxième joueur,
        # '3' pour un match nul.
        if result not in ['1', '2', '3']:
            raise ValueError("Le résultat doit être '1', '2' ou '3'.")

    def show_results(self):
        """Affiche les résultats du tournoi."""
        self.view.show_message("Résultats du tournoi :")
        self.tournament.show_results()

    def display_players(self):
        """Displays the list of players registered for the tournament."""
        self.view.display_players(self.tournament.players)
