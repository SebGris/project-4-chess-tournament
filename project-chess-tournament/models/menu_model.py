class MenuModel:
    def __init__(self):
        self.menu_navigation = {
            "main": [
                "Gestion des tournois",
                "Gestion des joueurs",
                "Menu pour test",
                "Quitter"
            ],
            "player": [
                "Ajouter des joueurs",
                "Charger les joueurs",
                "Afficher les joueurs",
                "Retour au menu principal",
                "Quitter"
            ],
            "tournament": [
                "Nouveau tournoi",
                "Ajouter des joueurs au tournoi",
                "Charger un tournoi",
                "Démarrer un tournoi",
                "Ajouter une description",
                "Afficher la description",
                "Afficher les joueurs du tournoi",
                "Afficher le résultat du tournoi",
                "Retour au menu principal",
                "Quitter"
            ],
            "test": [
                "Ajoute un tournoi",
                "Ajouter des joueurs au tournoi (score 0)",
                "Nouveau tournoi + Ajouter des joueurs",
                "Pairing",
                "Sauvegarder les joueurs et tournoi en JSON",
                "Retour au menu principal",
                "Quitter"
            ]
        }

    def get_menu_navigation(self, menu_name):
        return self.menu_navigation.get(menu_name, [])
