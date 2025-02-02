import re
from views.view import View


class ViewPlayer(View):
    """View representing the user interface."""

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        self.display_message(f"\nJoueur n° {counter}")
        last_name = self.prompt_input(
            "Entrez le nom du joueur (ou appuyez sur Entrée pour quitter) : "
            )
        if not last_name:
            return None, None, None, None
        first_name = self.prompt_input("Entrez son prénom : ")
        date_of_birth = self.prompt_date(
                "Entrez la date de naissance du joueur (format JJ/MM/AAAA): "
        )
        id_chess = self._prompt_for_id_chess()
        return last_name, first_name, date_of_birth, id_chess

    def _prompt_for_id_chess(self):
        """
        Requests and validates the national chess identifier (format XX#####).
        """
        while True:
            id_chess = self.prompt_input(
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

    def display_one_player(self, player):
        """Displays a player."""
        self.display_message(
            f"Nom : {player.last_name} {player.first_name} | "
            f"Date de naissance : {player.date_of_birth} | "
            f"ID échecs : {player.id_chess}"
        )

    def display_players(self, players):
        """Displays all the players."""
        if not players:
            self.display_message("Aucun joueur à afficher.")
            return
        for player in players:
            self.display_one_player(player)
