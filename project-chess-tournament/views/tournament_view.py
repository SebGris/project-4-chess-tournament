from models.player import Player
from models.round import Round
from models.tournament import Tournament
from reports.report_generator import ReportGenerator
from views.base_player_view import BasePlayerView


class TournamentView(BasePlayerView):

    def get_name(self) -> str:
        return self.input("Entrez le nom du tournoi :")

    def get_location(self) -> str:
        return self.input("Entrez le lieu du tournoi :")

    def get_start_date(self) -> str:
        return self.input_date("Entrez la date de début du tournoi :")

    def get_end_date(self) -> str:
        return self.input_date("Entrez la date de fin du tournoi :")

    def get_tournament_description(self) -> str:
        return self.input("Entrez la description du tournoi :")

    def get_total_of_rounds(self) -> int:
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

    def get_match_result(self) -> str:
        """Asks the user to enter the result of a match."""
        while True:
            result = self.input(
                "Entrez 1 si le joueur 1 gagne, "
                "2 si le joueur 2 gagne ou 0 si match nul "
                "ou entrez 'p' pour passer au match suivant :"
            )
            if result in {"p", "1", "2", "0"}:
                return result
            else:
                print("Entrée invalide. Veuillez entrer p, 1, 2 ou 0.")

    def get_tournament_selection(self, tournaments: list[Tournament]) -> int:
        print("Sélectionnez un tournoi :")
        for index, tournament in enumerate(tournaments):
            print(
                f"{index + 1}. {tournament.name} à {tournament.location} "
                f"du {tournament.start_date} au {tournament.end_date}"
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

    def display_tournaments_details(self, tournaments: list[Tournament]):
        """Display the details of a list of tournaments."""
        for tournament in tournaments:
            self.display_tournament_details(tournament)

    def display_tournament_details(self, tournament: Tournament):
        """Display tournament information."""
        print("--- Informations sur le tournoi ---")
        print(f"Tournoi : {tournament.name} | Lieu : {tournament.location}")
        print(f"Date : du {tournament.start_date} au {tournament.end_date}")
        print(
            f"Description : "
            f"{tournament.description if tournament.description else 'Aucune'}"
        )
        print(f"Nombre de tours : {tournament.total_rounds}")

    def display_match_summary(self, match):
        """Returns a summary of a match."""
        print(f"Match (joueur 1 vs joueur 2) : {' vs '.join(match)}")

    def display_record_results_message(self, round: Round):
        print(f"Enregistrement des résultats du {round.name}:")

    def display_no_round_error(self):
        print("Aucun round en cours. Créer un round pour saisir les scores.")

    def display_round_finished_message(self):
        print("Le round est terminé (scores déjà saisis).")

    def display_updated_number_rounds_message(self, number):
        print(f"Le nombre de tours a été mis à jour à {number}.")

    def display_added_round_message(self, round: Round):
        print(f"Nom du round ajouté : {round.name}")

    def display_tournament_created(self, name):
        print(f"Nouveau tournoi {name} créé.")

    def display_start_error_without_players(self):
        print("Le tournoi ne peut pas commencer sans joueurs.")

    def display_start_error_even_players(self):
        print("Le nombre de joueurs doit être pair pour commencer le tournoi.")

    def display_start_error_unfinished_match(self):
        print(
            "Un nouveau round ne peut pas commencer "
            "tant que tous les matchs du round précédent "
            "ne sont pas terminés."
        )

    def display_invalid_result_message(self):
        print("Score invalide. Veuillez entrer 1, 2 ou 0.")

    def display_successful_description_message(self):
        print("Description ajoutée avec succès.")

    def display_add_player_message(self):
        print("Ajout de joueurs dans le tournoi sélectionné.")

    def display_players_name(self, players: list[Player]):
        """Display the players of a tournament."""
        print("--- Joueurs du tournoi ---")
        if not players:
            print("Aucun joueur enregistré.")
        else:
            players_names = ", ".join(player.full_name for player in players)
            print(f"Joueurs : {players_names}")
            self.display_number_of_players(players)

    def display_players_details(self, players: list[Player]):
        """Display a list of players."""
        print("--- Joueurs du tournoi ---")
        if not players:
            print("Aucun joueur enregistré.")
        else:
            players = sorted(players, key=lambda ply: ply.score, reverse=True)
            total_score = sum(player.score for player in players)
            for player in players:
                print(
                    f"{player.full_name} | Né(e) le {player.birth_date} | "
                    f"ID échecs {player.chess_id} | Score : {player.score}"
                )
            self.display_number_of_players(players)
            print(f"Score total des joueurs : {total_score}")

    def display_number_of_players(self, players: list[Player]):
        """Display the number of players."""
        print(f"Nombre de joueurs : {len(players)}")

    def display_current_round_info(self, tournament: Tournament):
        """Display information active round."""
        if len(tournament.rounds) != 0:
            round = tournament.rounds[-1]
            if round:
                round_name = round.name
                print(f"--- {round_name} ---")
                if round.start_datetime:
                    print(f"Date de début : {round.start_datetime}")
                    end_date = round.end_datetime or "round en cours"
                    print(f"Date de fin : {end_date}")
            print(
                f"Round actuel : {len(tournament.rounds)}/"
                f"{tournament.total_rounds}"
            )
        else:
            print("Aucun round n'a été créé pour ce tournoi.")

    def display_player_pairs(self, round: Round):
        """Display pairs of players for a round."""
        if round:
            print(f"{round.name} avec les paires suivantes :")
            for index, pair in enumerate(round.get_pairs_players(), start=1):
                if len(pair) == 2:
                    print(f"{index}. {pair[0]} vs {pair[1]}")
                else:
                    print(
                        f"{index}. {pair[0]} score {pair[2]} vs "
                        f"{pair[1]} score {pair[3]}"
                    )

    def report_tournaments(self, tournament_dict):
        report_generator = ReportGenerator()
        report_generator.generate_tournaments_report(tournament_dict)

    def report_name_and_dates(self, tournament_dict):
        report_generator = ReportGenerator()
        report_generator.generate_tournament_name_and_dates_report(
            tournament_dict
        )

    def report_players(self, players_dict, tournament: Tournament):
        report_generator = ReportGenerator()
        report_generator.generate_tournament_players_report(
            players_dict, tournament.name
        )

    def report_rounds_matches(self, rounds_dict):
        report_generator = ReportGenerator()
        report_generator.generate_rounds_matches_report(rounds_dict)
