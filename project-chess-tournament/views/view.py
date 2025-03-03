import re
from views.base_view import BaseView


class View(BaseView):
    # Méthodes d'accès
    def get_user_choice(self):
        return self.input("Choisissez une option :")

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

    # Méthodes d'affichage
    def display_message(self, message):
        """Displays a generic message."""
        print(message)

    def display_invalid_option_message(self):
        print("Option invalide, veuillez réessayer.")

    def display_tournament_start_error(self):
        print("Le tournoi ne peut pas commencer sans joueurs.")

    def display_even_players_message(self):
        print("Le nombre de joueurs doit être pair pour commencer le tournoi.")

    def display_add_player_message(self, name):
        print(f"Joueur {name} ajouté.")

    def display_current_round_no(self, round_no):
        print(f"N° tour actuel : {round_no['current_round']}/"
              f"{round_no['number_of_rounds']}")

    def display_match_summary(self, match):
        """Returns a summary of a match."""
        print(f"Match (joueur 1 vs joueur 2) : {' vs '.join(match)}")

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

    def display_player_pairs(self, round_name, pairs):
        """Display pairs of players for a round."""
        print(f"{round_name} avec les paires suivantes :")
        for index, pair in enumerate(pairs, start=1):
            if len(pair) == 2:
                print(f"{index}. {pair[0]} vs {pair[1]}")
            else:
                print(f"{index}. {pair[0]} score {pair[2]} vs "
                      f"{pair[1]} score {pair[3]}")

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

    def display_players_full_names(self, players_names):
        """Display players' full names."""
        print(f"Joueurs : {', '.join(players_names)}")
        print(f"Nombre de joueurs : {len(players_names)}")

    def display_record_results_message(self, round_name):
        print(f"Enregistrement des résultats du {round_name}:")

    def display_no_round(self):
        print("Aucun tour en cours.")

    def display_round_info(self, round):
        """Display information about a round."""
        print(f"--- {round['name']} ---")
        if round['start_date']:
            print(f"Date de début : {round['start_date']}")
        print(f"Date de fin : {round['end_date'] or 'tour en cours'}")

    def display_tournament(self, tournament):
        """Display tournament information."""
        print("--- Informations sur le tournoi ---")
        print(f"Tournoi : {tournament['name']} | "
              f"Lieu : {tournament['location']}")
        print(f"Date : du {tournament['start_date']} "
              f"au {tournament['end_date']}")
        print(f"Description : {tournament['description']}")
        print(f"Nombre de tours : {tournament['number_of_rounds']}")
