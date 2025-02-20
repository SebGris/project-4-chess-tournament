import re
from views.base_view import View


class ViewPlayer(View):
    """View representing the user interface."""

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        self.display_message(f"\nJoueur n° {counter}")
        first_name = self.get_input("Entrez le prénom du joueur :")
        last_name = self.get_input("Entrez son nom :")
        birth_date = self.get_input_date(
            "Entrez sa date de naissance (format JJ/MM/AAAA):"
        )
        id_chess = self._prompt_for_id_chess()
        return last_name, first_name, birth_date, id_chess

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

    def display_one_player(self, player):
        """Displays a player."""
        self.display_message(
            f"Nom : {player.last_name} {player.first_name} | "
            f"Date de naissance : {player.birth_date} | "
            f"ID échecs : {player.id_chess}"
        )

    def display_players(self, players):
        """Displays all the players."""
        if not players:
            self.display_message("Aucun joueur à afficher.")
            return
        for player in players:
            self.display_one_player(player)

    def show_saving_success(self):
        """Displays a message confirming the saving of the players."""
        self.display_message("Les joueurs ont bien été enregistrés.")
