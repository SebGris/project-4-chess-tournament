class TournamentMenu:
    def __init__(self):
        self.groups = []

    def add_group(self, title, items):
        self.groups.append({"title": title, "items": items})

    def get_groups(self):
        return self.groups

    def clear_menu(self):
        self.groups = []
