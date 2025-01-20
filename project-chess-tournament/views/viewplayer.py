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

    def save_players(self):
        """Save player(s)."""
        print("Souhaitez vous enregistrer les joueurs dans la base ?")
        while True:
            choice = input("O/n: ")
            if choice == "O":
                return True
            elif choice == "n":
                return False

    def display_one_player(self, tuple):
        last_name, first_name, date_of_birth = tuple
        return f"Nom : {last_name} {first_name} né(e) le {date_of_birth}"

    def display_players(self, players):
        [print(self.display_one_player(player)) for player in players]

    def show_saving_success(self):
        """Message for saving success."""
        print("Sauvegarde des joueurs faite avec succès.")
