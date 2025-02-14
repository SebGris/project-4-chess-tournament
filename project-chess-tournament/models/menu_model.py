class MenuModel:
    def __init__(self):
        self.menu_items = [
            "Nouveau tournoi",
            "Ajouter des joueurs au tournoi",
            "Afficher les joueurs du tournoi",
            "Démarrer un tournoi",
            "Ajouter une description au tournoi",
            "Afficher le tournoi",
            "Quitter",
            "Test - Nouveau tournoi",
            "Test - Ajouter des joueurs au tournoi",
            "Test - Nouveau tournoi + Ajouter des joueurs",
            "Test - Pairing",
            "Test - Sauvegarder les joueurs et tournoi en JSON"
            ]

    def get_menu_items(self):
        return self.menu_items
