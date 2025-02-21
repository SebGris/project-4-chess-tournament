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
        return input("Choisissez une option :")

    def display_invalid_option_message_try_again(self):
        self.display_message("Choix invalide, veuillez réessayer.")

    def display_invalid_input_message_enter_a_number(self):
        self.display_message("Entrée invalide, veuillez entrer un nombre.")
