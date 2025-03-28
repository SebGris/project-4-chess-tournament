import re
from models.player import Player
from views.base_view import BaseView


class BasePlayerView(BaseView):
    def get_player_data(self):
        while True:
            print("Entrez l'ID échecs "
                  "(format: deux lettres suivies de cinq chiffres),")
            chess_id = self.input(
                "ou appuyer sur Entrée pour arrêter l'ajout des joueurs :"
            )
            if not chess_id:
                return None
            if re.match(r'^[A-Z]{2}\d{5}$', chess_id):
                break
            else:
                print("Identifiant invalide. "
                      "Le format doit être composé de "
                      "deux lettres suivies de cinq chiffres.")
        last_name = self.input("Entrez le nom de famille :")
        first_name = self.input("Entrez le prénom :")
        birth_date = self.input_date("Entrez la date de naissance :")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "chess_id": chess_id
        }

    def display_player_success_message(self, player: Player):
        print(f"Joueur {player.full_name} ajouté.")
