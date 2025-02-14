class MenuView:
    def display_menu(self, title, menu_items):
        header = f"\n=== {title} ==="
        print(header)
        for index, item in enumerate(menu_items):
            print(f"{index + 1}. {item}")
        print("=" * len(header))
        

    def display_message(self, message):
        print(message)