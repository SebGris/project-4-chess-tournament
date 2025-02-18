from views.view import View


class MenuView(View):
    def display_menu(self, title, menu_items):
        """Display a menu with a title and items."""
        self.clear_console()
        header = f"=== {title} ==="
        print(header)
        for index, item in enumerate(menu_items):
            print(f"{index + 1}. {item}")
        print("=" * len(header))

    def get_user_choice(self, menu_item_count):
        return input("Choisissez une option (1-{}) :".format(menu_item_count))

    def display_invalid_option_message_try_again(self):
        self.display_message("Choix invalide, veuillez réessayer.")

    def display_invalid_input_message_enter_a_number(self):
        self.display_message("Entrée invalide, veuillez entrer un nombre.")
