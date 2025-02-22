class Menu:
    def __init__(self):
        self.groups = []
        self.tournament_loaded = False

    def add_group(self, title, items):
        self.groups.append({"title": title, "items": items})

    def get_groups(self):
        return self.groups

    def clear_menu(self):
        self.groups = []

    def is_tournament_loaded(self):
        return self.tournament_loaded

    def set_tournament_loaded(self, loaded):
        self.tournament_loaded = loaded
