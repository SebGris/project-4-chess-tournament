class ViewPlayer:

    def prompt_for_player(self, counter):
        """Prompt for last name, first name and date of birth."""
        print(f"\nJoueur n° {counter}")
        last_name = input("Entrez le nom du joueur (Entrée pour quitter) : ")
        if not last_name:
            return (None, None, None)
        first_name = input("Entrez le prénom du joueur : ")
        date_of_birth = input("Entrez la date de naissance du joueur : ")

        return (last_name, first_name, date_of_birth)

    def display_one_player(self, player):
        print(f"Nom : {player.last_name} {player.first_name} né(e) le {player.date_of_birth}")

    def display_players(self, players):
        for player in players:
            self.display_one_player(player)

    def show_saving_success(self):
        """Message for saving success."""
        print("Sauvegarde des joueurs faite avec succès.")
