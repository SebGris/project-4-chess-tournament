class MenuView:
    def display_menu(self, menu_items, title):
        header = f"=== {title} ==="
        print(header)
        for index, item in enumerate(menu_items):
            print(f"{index + 1}. {item}")
        print("=" * len(header))
        

    def display_message(self, message):
        print(message)