class ApplicationMenu:
    """A class to represent an application menu."""
    def __init__(self):
        """Initializes the application menu."""
        self.groups = []

    def add_title(self, title):
        """Adds a title to the menu."""
        self.add_group(title, [])

    def add_group(self, title, items):
        """Adds a group of items to the menu."""
        self.groups.append({"title": title, "items": items})

    def get_groups(self):
        """Returns the groups in the menu."""
        return self.groups

    def clear_menu(self):
        """Clears the menu."""
        self.groups.clear()
