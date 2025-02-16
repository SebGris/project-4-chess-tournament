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
