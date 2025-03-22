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
        """Display a menu with a title and items."""
        def create_separator_line(header):
            print("=" * len(header))
        index = 1
        for group in menu.get_groups():
            menu_group_header = f"=== {group['title']} ==="
            if group['items'] == []:
                create_separator_line(menu_group_header)
            print(menu_group_header)
            for item in group['items']:
                print(f"{index}. {item['label']}")
                index += 1
            create_separator_line(menu_group_header)
