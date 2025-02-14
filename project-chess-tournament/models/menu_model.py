class MenuModel:
    def __init__(self):
        self.main_menu = [
            "Nouveau tournoi",
            "Ajouter des joueurs",
            "Afficher les joueurs",
            "Démarrer un tournoi",
            "Ajouter une description au tournoi",
            "Afficher le tournoi",
            "Test",
            "Quitter"
            ]
        self.test_items_menu = [
            "Ajoute un nouveau tournoi",
            "Ajouter des joueurs au tournoi",
            "Nouveau tournoi + Ajouter des joueurs",
            "Pairing",
            "Sauvegarder les joueurs et tournoi en JSON",
            "Retour au menu principal"
            ]

    def get_main_menu_options(self):
        return self.main_menu
    
    def get_test_items_menu_options(self):
        return self.test_items_menu
