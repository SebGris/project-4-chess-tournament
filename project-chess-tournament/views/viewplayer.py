from datetime import datetime


class ViewPlayer:

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        print(f"\nJoueur n° {counter}")
        last_name = input(
            "Entrez le nom du joueur (ou appuyez sur Entrée pour quitter) : "
            ).strip()
        if not last_name:
            return None, None, None, None
        first_name = input("Entrez son prénom : ").strip()
        date_of_birth = self._prompt_for_date_of_birth()
        id_chess = input("Entrez son identifiant national d'échecs : ").strip()
        return last_name, first_name, date_of_birth, id_chess

    def _prompt_for_date_of_birth(self):
        """
        Requests a date of birth in DD/MM/YYYY format and validates the entry.
        """
        while True:
            date_input = input(
                "Entrez la date de naissance du joueur (format JJ/MM/AAAA): "
                ).strip()
            try:
                # Vérifie et convertit la date
                date_object = datetime.strptime(date_input, "%d/%m/%Y")
                return date_object.strftime("%d/%m/%Y")  # Retourne en texte
            except ValueError:
                print(
                    "Format invalide. "
                    "Veuillez entrer une date au format JJ/MM/AAAA."
                    )

    def display_one_player(self, player):
        print(
            f"Nom : {player.last_name} {player.first_name} | "
            f"Date de naissance : {player.date_of_birth}"
            )

    def display_players(self, players):
        for player in players:
            self.display_one_player(player)

    def show_saving_success(self):
        """Message for saving success."""
        print("Sauvegarde des joueurs faite avec succès.")
