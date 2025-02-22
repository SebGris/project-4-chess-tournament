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
        return input("Entrez le chemin du fichier JSON du tournoi : ")

    def get_tournament_name(self):
        return input("Entrez le nom du tournoi : ")

    def get_tournament_location(self):
        return input("Entrez le lieu du tournoi : ")

    def get_tournament_start_date(self):
        return input("Entrez la date de début du tournoi : ")

    def get_tournament_end_date(self):
        return input("Entrez la date de fin du tournoi : ")

    def get_tournament_players(self):
        players = input(
            "Entrez les joueurs du tournoi (séparés par des virgules) : "
        )
        return [player.strip() for player in players.split(',')]

    def get_tournament_description(self):
        return input("Entrez la description du tournoi : ")
