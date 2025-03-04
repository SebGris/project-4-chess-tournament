import re


class InputHandler:
    def input(self, prompt):
        return input(prompt)

    def get_tournament_file_path(self):
        return self.input("Entrez le chemin du fichier JSON du tournoi:")

    def get_players_file_path(self):
        return self.input("Entrez le chemin du fichier JSON des joueurs:")

    def get_tournament_name(self):
        return self.input("Entrez le nom du tournoi :")

    def get_tournament_location(self):
        return self.input("Entrez le lieu du tournoi :")

    def get_tournament_start_date(self):
        return self.input("Entrez la date de début du tournoi :")

    def get_tournament_end_date(self):
        return self.input("Entrez la date de fin du tournoi :")

    def get_tournament_description(self):
        return self.input("Entrez la description du tournoi :")

    def get_tournament_number_of_rounds(self):
        return int(
            self.input(
                "Entrez le nombre de tours du tournoi (par défaut 4):"
            ) or 4
        )

    def request_player_addition_confirmation(self):
        return self.get_user_confirmation("Voulez-vous ajouter des joueurs ?")

    def get_user_confirmation(self, prompt):
        while True:
            response = self.input(f"{prompt} (oui/non):").lower()
            if response in ["oui", "non"]:
                return response == "oui"
            else:
                print(
                    "Réponse invalide. Veuillez répondre par 'oui' ou 'non'."
                )

    def get_player_data(self):
        while True:
            id_chess = self.input(
                "Entrez l'ID échecs "
                "(format: deux lettres suivies de cinq chiffres) :"
            )
            if not id_chess:
                return None
            if re.match(r'^[A-Z]{2}\d{5}$', id_chess):
                break
            else:
                print(
                    "Identifiant invalide. "
                    "Le format doit être composé de deux lettres "
                    "suivies de cinq chiffres."
                )
        last_name = self.input("Entrez le nom de famille :")
        first_name = self.input("Entrez le prénom :")
        birth_date = self.input("Entrez la date de naissance :")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "id_chess": id_chess
        }

    def get_match_result(self):
        """Asks the user to enter the result of a match."""
        while True:
            result = self.input(
                "Entrez "
                "1 si le joueur 1 gagne, "
                "2 si le joueur 2 gagne ou "
                "0 si match nul :"
            )
            if result in {"1", "2", "0"}:
                return result
            else:
                print("Entrée invalide. Veuillez entrer 1, 2 ou 0.")
