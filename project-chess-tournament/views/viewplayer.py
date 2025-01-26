import re
from datetime import datetime


class ViewPlayer:

    def _get_input(self, prompt):
        """Request an entry and eliminate superfluous spaces."""
        return input(prompt).strip()

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        print(f"\nJoueur n° {counter}")
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
                print(
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
                print(
                    "Identifiant invalide. "
                    "Le format doit être composé de deux lettres "
                    "suivies de cinq chiffres."
                    )

    def display_one_player(self, player):
        print(
            f"Nom : {player.last_name} {player.first_name} | "
            f"Date de naissance : {player.date_of_birth} | "
            f"ID échecs : {player.id_chess}"
        )

    def display_players(self, players):
        """Displays all the players on the list."""
        if not players:
            print("Aucun joueur à afficher.")
            return
        for player in players:
            self.display_one_player(player)

    def show_saving_success(self):
        """Message for saving success."""
        print("Sauvegarde des joueurs faite avec succès.")
