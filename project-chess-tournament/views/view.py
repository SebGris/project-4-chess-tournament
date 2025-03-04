from views.base_view import BaseView


class View(BaseView):
    # Méthodes d'affichage
    def display_message(self, message):
        """Displays a generic message."""
        print(message)

    def display_tournament_start_error(self):
        print("Le tournoi ne peut pas commencer sans joueurs.")

    def display_even_players_message(self):
        print("Le nombre de joueurs doit être pair pour commencer le tournoi.")

    def display_add_player_message(self, name):
        print(f"Joueur {name} ajouté.")

    def display_current_round_no(self, round_no):
        print(f"N° tour actuel : {round_no['current_round']}/"
              f"{round_no['number_of_rounds']}")

    def display_match_summary(self, match):
        """Returns a summary of a match."""
        print(f"Match (joueur 1 vs joueur 2) : {' vs '.join(match)}")

    def display_player_pairs(self, round_name, pairs):
        """Display pairs of players for a round."""
        print(f"{round_name} avec les paires suivantes :")
        for index, pair in enumerate(pairs, start=1):
            if len(pair) == 2:
                print(f"{index}. {pair[0]} vs {pair[1]}")
            else:
                print(f"{index}. {pair[0]} score {pair[2]} vs "
                      f"{pair[1]} score {pair[3]}")

    def display_players(self, players):
        """Display a list of players."""
        print("--- Liste des joueurs ---")
        if not players:
            print("Aucun joueur enregistré.")
        else:
            for player in players:
                print(f"{player['full_name']} | "
                      f"Né(e) le {player['birth_date']} | "
                      f"ID échecs {player['id_chess']}")

    def display_tournament_players(self, players_names):
        """Display the players of a tournament."""
        print("--- Joueurs du tournoi ---")
        print(f"Joueurs : {', '.join(players_names)}")
        print(f"Nombre de joueurs : {len(players_names)}")

    def display_record_results_message(self, round_name):
        print(f"Enregistrement des résultats du {round_name}:")

    def display_no_round(self):
        print("Aucun tour en cours.")

    def display_round_info(self, round):
        """Display information about a round."""
        round_name = round['name']
        if round_name == "Round 1":
            print("--- Liste des rounds ---")
        print(f"--- {round_name} ---")
        if round['start_date']:
            print(f"Date de début : {round['start_date']}")
        print(f"Date de fin : {round['end_date'] or 'tour en cours'}")

    def display_tournament_details(self, tournament):
        """Display tournament information."""
        print("--- Informations sur le tournoi ---")
        print(f"Tournoi : {tournament['name']} | "
              f"Lieu : {tournament['location']}")
        print(f"Date : du {tournament['start_date']} "
              f"au {tournament['end_date']}")
        print(f"Description : {tournament['description']}")
        print(f"Nombre de tours : {tournament['number_of_rounds']}")
