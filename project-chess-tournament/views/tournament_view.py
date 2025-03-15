from models.tournament import Tournament
from typing import List
from views.base_view import BaseView


class TournamentView(BaseView):

    def get_name(self):
        return self.input("Entrez le nom du tournoi :")

    def get_location(self):
        return self.input("Entrez le lieu du tournoi :")

    def get_start_date(self):
        return self.input("Entrez la date de début du tournoi :")

    def get_end_date(self):
        return self.input("Entrez la date de fin du tournoi :")

    def get_tournament_description(self):
        return self.input("Entrez la description du tournoi :")

    def get_number_of_rounds(self):
        while True:
            try:
                rounds = self.input(
                    "Entrez le nombre de tours du tournoi (par défaut 4):"
                )
                if rounds == "":
                    return 4
                rounds = int(rounds)
                if rounds > 0:
                    return rounds
                else:
                    print("Le nombre de tours doit être un chiffre positif.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre.")

    def get_match_result(self):
        """Asks the user to enter the result of a match."""
        while True:
            result = self.input(
                "Entrez 1 si le joueur 1 gagne, 2 si le joueur 2 gagne ou 0 si match nul :"
            )
            if result in {"1", "2", "0"}:
                return result
            else:
                print("Entrée invalide. Veuillez entrer 1, 2 ou 0.")

    def get_tournament_selection(self, tournaments: List[Tournament]) -> int:
        print("Sélectionnez un tournoi :")
        for index, tournament in enumerate(tournaments):
            print(
                f"{index + 1}. {tournament.name} à {tournament.location} du {tournament.start_date} au {tournament.end_date}"
            )
        while True:
            try:
                choice = int(self.input("Entrez le numéro du tournoi :")) - 1
                if 0 <= choice < len(tournaments):
                    return choice
                else:
                    print("Choix invalide, veuillez réessayer.")
            except ValueError:
                print("Entrée invalide, veuillez entrer un numéro.")

    def display_tournament_details(self, tournament: Tournament):
        """Display tournament information."""
        print("--- Informations sur le tournoi ---")
        print(f"Tournoi : {tournament.name} | Lieu : {tournament.location}")
        print(f"Date : du {tournament.start_date} au {tournament.end_date}")
        print(
            f"Description : {tournament.description if tournament.description else 'Aucune'}"
        )
        print(f"Nombre de tours : {tournament.number_of_rounds}")

    def display_tournaments(self, tournaments: List[Tournament]):
        for tournament in tournaments:
            self.display_tournament_details(tournament)

    def display_current_round(self, tournament: Tournament):
        print(
            f"Round actuel : {tournament.current_round}/{tournament.number_of_rounds}"
        )

    def display_match_summary(self, match):
        """Returns a summary of a match."""
        print(f"Match (joueur 1 vs joueur 2) : {' vs '.join(match)}")

    def display_record_results_message(self, round_name):
        self.write_line(f"Enregistrement des résultats du {round_name}:")

    def display_updated_number_rounds_message(self, number):
        self.write_line(f"Le nombre de tours a été mis à jour à {number}.")

    def display_added_round_message(self, round_name):
        self.write_line(f"Nom du round ajouté : {round_name}")

    def display_no_tournament_message(self):
        self.write_line("Aucun tournoi n'est chargé.")

    def display_no_round_message(self):
        self.write_line("Aucun round en cours.")

    def display_for_file_not_found(self, error):
        self.write_line(
            f"=== Information ===\n{error}\nVeuillez créer un nouveau tournoi."
        )

    def display_tournament_created(self, name):
        self.write_line(f"Nouveau tournoi {name} créé.")

    def display_save_success_message(self, filename):
        self.write_line(f"Tournoi sauvegardé avec succès dans le fichier {filename}")

    def display_save_error_message(self, error):
        self.write_line(f"Erreur lors de la sauvegarde du tournoi : {error}")

    def display_start_error_tournament_without_players(self):
        self.write_line("Le tournoi ne peut pas commencer sans joueurs.")

    def display_start_error_tournament_even_players(self):
        self.write_line(
            "Le nombre de joueurs doit être pair pour commencer le tournoi."
        )

    def display_successful_description_message(self):
        self.write_line("Description ajoutée avec succès.")

    def display_tournament_closed_message(self):
        self.write_line("Le tournoi a été fermé avec succès.")

    def display_tournament_selected(self, name):
        self.write_line(f"Tournoi sélectionné : {name}")
