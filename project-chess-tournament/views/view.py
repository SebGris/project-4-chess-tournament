from views.base_view import BaseView


class View(BaseView):
    def display_menu(self, menu):
        """Display a menu with a title and items."""
        # self.clear_console()
        index = 1
        for group in menu.get_groups():
            menu_group_header = f"=== {group['title']} ==="
            print(menu_group_header)
            for item in group['items']:
                print(f"{index}. {item['label']}")
                index += 1
            print("=" * len(menu_group_header))

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
                self.display_message("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

    def get_player_data(self):
        player_data = input(
            "Entrez les données du joueur "
            "(nom de famille, prénom, date de naissance, "
            "id échecs) ou appuyez sur Entrée pour arrêter: "
        )
        if player_data:
            last_name, first_name, birth_date, id_chess = \
                player_data.strip().split(',')
            return {
                "last_name": last_name,
                "first_name": first_name,
                "birth_date": birth_date,
                "id_chess": id_chess
            }
        return None
