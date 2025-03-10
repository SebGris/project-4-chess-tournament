from views.base_view import BaseView


class MenuView(BaseView):
    def get_user_choice(self):
        return self.input("Choisissez une option :")

    def display_invalid_option_message(self):
        print("Option invalide, veuillez réessayer.")

    def display_menu(self, menu):
        """Display a menu with a title and items."""
        index = 1
        for group in menu.get_groups():
            menu_group_header = f"=== {group['title']} ==="
            if group['items'] == []:
                print("=" * len(menu_group_header))
            print(menu_group_header)
            for item in group['items']:
                print(f"{index}. {item['label']}")
                index += 1
            print("=" * len(menu_group_header))
