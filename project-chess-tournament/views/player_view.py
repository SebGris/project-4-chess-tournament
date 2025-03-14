import re
from models.player import Player
from typing import List
from views.base_view import BaseView


class PlayerView(BaseView):
    def get_player_data(self):
        while True:
            self.write_line("Entrez l'ID échecs (format: deux lettres suivies de cinq chiffres),")
            id_chess = self.input("ou appuyer sur Entrée pour arrêter l'ajout des joueurs :")
            if not id_chess:
                return None
            if re.match(r'^[A-Z]{2}\d{5}$', id_chess):
                break
            else:
                print("Identifiant invalide. Le format doit être composé de deux lettres suivies de cinq chiffres.")
        last_name = self.input("Entrez le nom de famille :")
        first_name = self.input("Entrez le prénom :")
        birth_date = self.input("Entrez la date de naissance :")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "id_chess": id_chess
        }

    def request_player_addition_confirmation(self):
        return self.get_user_confirmation("Voulez-vous ajouter des joueurs ?")

    def get_user_confirmation(self, prompt):
        while True:
            response = self.input(f"{prompt} (oui/non):").lower()
            if response in ["oui", "non"]:
                return response == "oui"
            else:
                print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

    def display_add_player_message(self, name):
        self.write_line(f"Joueur {name} ajouté.")

    def display_players(self, players: List[Player]):
        """Display a list of players."""
        print("--- Joueurs du tournoi ---")
        if not players:
            print("Aucun joueur enregistré.")
        else:
            for player in players:
                print(f"{player.full_name} | Né(e) le {player.birth_date} | ID échecs {player.id_chess}")

    def display_tournament_players(self, players_names):
        """Display the players of a tournament."""
        print("--- Joueurs du tournoi ---")
        if not players_names:
            print("Aucun joueur enregistré.")
        else:
            print(f"Joueurs : {', '.join(players_names)}")
            print(f"Nombre de joueurs : {len(players_names)}")
