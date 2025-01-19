class Screen:
    def prompt_for_add_new_player(self):
        print("1 : Ajouter un joueur")

    def prompt_for_player(self):
        """Prompt for a name."""
        name = input("tapez le nom du joueur : ")
        if not name:
            return None
        return name
    
    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True