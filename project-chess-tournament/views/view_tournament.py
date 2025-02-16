import re
from views.view import View


class ViewTournament(View):
    """View to display tournament information."""

    def prompt_for_tournament(self):
        """Requests information from a tournament and returns it."""
        # self.clear_console()
        self.display_message("Nouveau tournoi.")
        name = self.get_input("Entrez le nom du tournoi :")
        location = self.get_input("Entrez le lieu du tournoi :")
        start_date = self.get_input_date(
            "Entrez la date de début (JJ/MM/AAAA) :"
        )
        end_date = self.get_input_date("Entrez la date de fin (JJ/MM/AAAA) :")
        return name, location, start_date, end_date

    def prompt_for_description(self):
        """Request a description for the tournament."""
        return self.get_input("Ajoutez une description :")

    def prompt_for_add_player(self):
        """Request to add a player to the tournament."""
        return self.get_input("Ajouter un joueur ? (o/n) :").lower()

    def prompt_for_player(self):
        """Prompt for player details"""
        first_name = self.get_input("Entrez le prénom du joueur :")
        last_name = self.get_input("Entrez son nom :")
        birth_date = self.get_input_date(
            "Entrez sa date de naissance (format JJ/MM/AAAA):"
        )
        id_chess = self._prompt_for_id_chess()
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "id_chess": id_chess
        }

    def _prompt_for_id_chess(self):
        """
        Requests and validates the national chess identifier (format XX#####).
        """
        while True:
            id_chess = self.get_input(
                "Entrez son identifiant national d'échecs (format AB12345) : "
                )
            if re.match(r'^[A-Z]{2}\d{5}$', id_chess):
                return id_chess
            else:
                self.display_message(
                    "Identifiant invalide. "
                    "Le format doit être composé de deux lettres "
                    "suivies de cinq chiffres."
                    )

    def display_players(self, players):
        """Displays a list of players."""
        if not players:
            self.display_message("Aucun joueur dans le tournoi.")
        else:
            self.display_message("Liste des joueurs :")
            for player in players:
                self.display_message(player)

    def display_tournament(self, tournament):
        """Displays the details of a tournament."""
        self.display_message(str(tournament))

    def get_match_result(self):
        """Asks the user to enter the result of a match."""
        while True:
            result = self.get_input(
                "Résultat (1: Joueur 1 gagne, 2: Joueur 2 gagne, 0: Nul) : "
            )
            if result in {"1", "2", "0"}:
                return result
            else:
                print("Entrée invalide. Veuillez entrer 1, 2 ou 0.")

    def display_result(self, players):
        """Display the result of a tournament."""
        self.display_message("Tournoi terminé !")
        self.display_players(players)

    def display_tournament_players(self, tournament):
        """Displays the list of players in the tournament."""
        players = tournament.players
        if not players:
            self.display_message("Aucun joueur dans le tournoi.")
        else:
            self.display_message("Liste des joueurs du tournoi :")
            for player in players:
                self.display_message(
                    f"Nom : {player.last_name} {player.first_name} | "
                    f"Date de naissance : {player.birth_date} | "
                    f"ID échecs : {player.id_chess}"
                )
