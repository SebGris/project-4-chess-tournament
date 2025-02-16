class MenuModel:
    def __init__(self):
        self.menus = {
            "main": [
                "Gestion des tournois",
                "Gestion des joueurs",
                "Menu Test",
                "Quitter"
            ],
            "player": [
                "Ajouter des joueurs",
                "Afficher les joueurs",
                "Retour au menu principal",
                "Quitter"
            ],
            "tournament": [
                "Nouveau tournoi",
                "Démarrer un tournoi",
                "Ajouter une description",
                "Afficher le tournoi",
                "Retour au menu principal",
                "Quitter"
            ],
            "test": [
                "Ajoute un tournoi",
                "Ajouter des joueurs au tournoi",
                "Nouveau tournoi + Ajouter des joueurs",
                "Pairing",
                "Sauvegarder les joueurs et tournoi en JSON",
                "Retour au menu principal",
                "Quitter"
            ]
        }

    def get_menu_items(self, menu_name):
        return self.menus.get(menu_name, [])
