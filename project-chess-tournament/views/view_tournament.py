from views.view import View


class ViewTournament(View):
    """View representing the tournament interface."""

    def prompt_for_tournament(self):
        """Requests information from a tournament and returns it."""
        name = self.prompt_input("Entrez le nom du tournoi :")
        location = self.prompt_input("Entrez le lieu du tournoi :")
        start_date = self.prompt_date("Entrez la date de début (JJ/MM/AAAA) :")
        end_date = self.prompt_date("Entrez la date de fin (JJ/MM/AAAA) :")
        description = self.prompt_input("Ajoutez une description :")

        return name, location, start_date, end_date, description

    def display_tournament(self, tournament):
        """Displays the details of a tournament."""
        self.display_message(str(tournament))

    def prompt_for_match_result(self, match):
        """Request the result of a match."""
        self.display_message(f"Match entre {match.player1.first_name} "
                             f"{match.player1.last_name} et "
                             f"{match.player2.first_name} "
                             f"{match.player2.last_name}")
        return self.prompt_input(
            "Entrez le résultat ("
            "1 pour la victoire du 1er joueur, "
            "2 pour la victoire du 2ème joueur, "
            "3 pour match nul) : "
            )

    def display_match_result(self, match):
        """Display the result of a match."""
        self.display_message(f"Résultat du match : {match.result}")
