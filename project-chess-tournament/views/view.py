import re
from views.base_view import BaseView


class View(BaseView):
    # Méthodes d'accès
    def get_user_choice(self):
        return input("Choisissez une option : ")

    def get_tournament_file_path(self):
        return input("Entrez le chemin du fichier JSON du tournoi: ")

    def get_players_file_path(self):
        return input("Entrez le chemin du fichier JSON des joueurs: ")

    def get_tournament_name(self):
        return input("Entrez le nom du tournoi : ")

    def get_tournament_location(self):
        return input("Entrez le lieu du tournoi : ")

    def get_tournament_start_date(self):
        return input("Entrez la date de début du tournoi : ")

    def get_tournament_end_date(self):
        return input("Entrez la date de fin du tournoi : ")

    def get_tournament_description(self):
        return input("Entrez la description du tournoi : ")

    def get_tournament_number_of_rounds(self):
        return int(
            input("Entrez le nombre de tours du tournoi (par défaut 4): ") or 4
        )

    def get_user_confirmation(self, prompt):
        while True:
            response = input(f"{prompt} (oui/non): ").strip().lower()
            if response in ["oui", "non"]:
                return response == "oui"
            else:
                self.display_message(
                    "Réponse invalide. Veuillez répondre par 'oui' ou 'non'."
                )

    def get_player_data(self):
        while True:
            id_chess = input(
                "Entrez l'ID échecs "
                "(format: deux lettres suivies de cinq chiffres) : "
            ).strip()
            if not id_chess:
                return None
            if re.match(r'^[A-Z]{2}\d{5}$', id_chess):
                break
            else:
                self.display_message(
                    "Identifiant invalide. "
                    "Le format doit être composé de deux lettres "
                    "suivies de cinq chiffres."
                )
        last_name = input("Entrez le nom de famille : ").strip()
        first_name = input("Entrez le prénom : ").strip()
        birth_date = input("Entrez la date de naissance : ").strip()
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "id_chess": id_chess
        }

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

    # Méthodes d'affichage
    def display_menu(self, menu):
        """Display a menu with a title and items."""
        index = 1
        for group in menu.get_groups():
            menu_group_header = f"=== {group['title']} ==="
            print(menu_group_header)
            for item in group['items']:
                print(f"{index}. {item['label']}")
                index += 1
            print("=" * len(menu_group_header))

    def display_players(self, players):
        """Display a list of players."""
        print("--- Liste des joueurs ---")
        if not players:
            print("Aucun joueur enregistré.")
        else:
            for player in players:
                print(f"{player['full_name']} | "
                      f"Né(e) le {player['birth_date']} | "
                      f"ID échecs {player['id_chess']}")
