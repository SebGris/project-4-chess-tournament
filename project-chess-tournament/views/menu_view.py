from views.base_view import BaseView


class MenuView(BaseView):
    def __init__(self):
        super().__init__()
        # affiche une ligne vide
        print()

    def get_user_choice(self):
        return self.input("Choisissez une option :")

    def display_invalid_option_message(self):
        print("Option invalide, veuillez réessayer.")

    def display_menu(self, menu):
        """Affiche un menu encadré par une fenêtre de signes '='."""
        # Calcul de la largeur de la fenêtre
        max_title_length = max(
            len(group['title'])
            for group in menu.get_groups()
        ) if menu.get_groups() else 0
        max_item_label_length = max(
            len(f"{index}. {item['label']}")
            for group in menu.get_groups()
            for index, item in enumerate(group['items'], start=1)
        ) if menu.get_groups() else 0
        max_length = max(max_item_label_length, max_title_length)
        # Largeur minimale de 20 caractères
        window_width = max(max_length + 4, 20)

        # Ligne horizontale supérieure
        print("=" * window_width)

        # Affichage des groupes et des items
        index = 1
        for group in menu.get_groups():
            # Affichage du titre du groupe
            print(f"| {group['title'].center(window_width - 4)} |")
            if group['items'] != []:
                print("=" * window_width)

            # Affichage des items du groupe
            for item in group['items']:
                item_text = f"{index}. {item['label']}"
                print(f"| {item_text.ljust(window_width - 4)} |")
                index += 1

            # Ligne de séparation entre les groupes
            print("=" * window_width)
