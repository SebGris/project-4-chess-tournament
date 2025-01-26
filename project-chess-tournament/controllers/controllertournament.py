from models.player import Player


class ControllerTournament:
    """Controller for adding players,
    running the tournament and managing results."""
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament

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
            self.view.prompt_for_match_result(match)

    def show_results(self):
        """Affiche les résultats du tournoi."""
        self.view.show_message("Résultats du tournoi :")
        self.tournament.show_results()

    def display_players(self):
        """Displays the list of players registered for the tournament."""
        self.view.display_players(self.tournament.players)
