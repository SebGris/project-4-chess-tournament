import re
from datetime import datetime


class ViewPlayer:
    """View representing the user interface."""

    def _get_input(self, prompt):
        """Request an entry and eliminate superfluous spaces."""
        return input(prompt).strip()

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        self.show_message(f"\nJoueur n° {counter}")
        last_name = self._get_input(
            "Entrez le nom du joueur (ou appuyez sur Entrée pour quitter) : "
            )
        if not last_name:
            return None, None, None, None
        first_name = self._get_input("Entrez son prénom : ")
        date_of_birth = self._prompt_for_date_of_birth()
        id_chess = self._prompt_for_id_chess()
        return last_name, first_name, date_of_birth, id_chess

    def _prompt_for_date_of_birth(self):
        """
        Requests a date of birth in DD/MM/YYYY format and validates the entry.
        """
        while True:
            date_input = self._get_input(
                "Entrez la date de naissance du joueur (format JJ/MM/AAAA): "
                )
            try:
                # Vérifie et convertit la date
                date_object = datetime.strptime(date_input, "%d/%m/%Y")
                # Retourne la date sous format texte
                return date_object.strftime("%d/%m/%Y")
            except ValueError:
                self.show_message(
                    "Format invalide. "
                    "Veuillez entrer une date au format JJ/MM/AAAA."
                    )

    def _prompt_for_id_chess(self):
        """
        Requests and validates the national chess identifier (format XX#####).
        """
        while True:
            id_chess = self._get_input(
                "Entrez son identifiant national d'échecs (format AB12345) : "
                )
            if re.match(r'^[A-Z]{2}\d{5}$', id_chess):
                return id_chess
            else:
                self.show_message(
                    "Identifiant invalide. "
                    "Le format doit être composé de deux lettres "
                    "suivies de cinq chiffres."
                    )

    def display_one_player(self, player):
        """Displays a player."""
        self.show_message(
            f"Nom : {player.last_name} {player.first_name} | "
            f"Date de naissance : {player.date_of_birth} | "
            f"ID échecs : {player.id_chess}"
        )

    def display_players(self, players):
        """Displays all the players."""
        if not players:
            self.show_message("Aucun joueur à afficher.")
            return
        for player in players:
            self.display_one_player(player)

    def show_saving_success(self):
        """Message for saving success."""
        self.show_message("Sauvegarde des joueurs faite avec succès.")

    def show_message(self, message):
        """Displays a message to the user."""
        print(message)

    def prompt_for_match_result(self, match):
        """Request the result of a match."""
        print(f"Match entre {match.player1.first_name} "
              f"{match.player1.last_name} et "
              f"{match.player2.first_name} "
              f"{match.player2.last_name}")
        result = input(
            "Entrez le résultat ("
            "1 pour la victoire du 1er joueur, "
            "0 pour la victoire du 2ème joueur, "
            "0.5 pour match nul) : "
            )
        match.set_result(result)
        print(f"Résultat du match : {match.result}")
