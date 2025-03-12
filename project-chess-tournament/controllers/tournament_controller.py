from controllers.pairing import Pairing
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from menu_commands.save_tournament_command import SaveTournamentCommand


class TournamentController():

    def __init__(self, repository, view):
        self.repository = repository
        self.view = view
        self.tournaments = []
        self.active_tournament = None
        self.all_players = self.load_all_players()
        self.load_tournaments()

    def get_all_tournaments(self):
        tournaments = self.repository.get_all_tournaments()
        self.view.display_all_tournaments(tournaments)

    def get_tournament_by_id(self, tournament_id):
        tournament = self.repository.find_tournament_by_id(tournament_id)
        self.view.display_tournament(tournament)

    def create_tournament(self, name, location, start_date, end_date, number_of_rounds, description=None, player_ids=None, rounds_list=None):
        players_list = [self.all_players[player_id] for player_id in player_ids] if player_ids else []
        rounds_list = [Round(**round) for round in rounds_list] if rounds_list else []
        tournament = Tournament(name, location, start_date, end_date, number_of_rounds, description, players_list, rounds_list)
        self.active_tournament = tournament
        self.tournaments.append(tournament)
        created_tournament = self.repository.create_tournament(tournament)
        self.view.display_tournament_created(created_tournament)

    def update_tournament(self, tournament_id, name, date):
        updated_data = {"name": name, "date": date}
        tournament = self.repository.update_tournament(tournament_id, updated_data)
        self.view.display_tournament_updated(tournament)
    
    def select_tournament(self, tournament_index):
        self.active_tournament = self.tournaments[tournament_index]
        self.view.menu.set_tournament_loaded(True)

    def load_tournaments(self):
        """Charger les tournois depuis un fichier JSON."""
        try:
            tournaments_data = TournamentLoaderService.load_tournaments()
            for tournament_data in tournaments_data:
                if isinstance(tournament_data, dict):
                    self.create_tournament(**tournament_data)
                else:
                    print(f"Invalid data format: {tournament_data}")
        except FileNotFoundError as e:
            self.view.display_for_file_not_found(str(e))

    def load_players_data(self):
        return TournamentLoaderService.load_players()

    def load_all_players(self):
        try:
            all_players = {
                player_data['id']: Player(**player_data)
                for player_data in self.load_players_data()
            }
            return all_players
        except FileNotFoundError as e:
            self.view.display_for_file_not_found(str(e))

    def add_player(self, player_data):
        player = Player(**player_data)
        self.active_tournament.players.append(player)
        return str(player.id)
    
    def get_players(self):
        return [
            {
                **player.to_dict(),
                "full_name": player.full_name
            }
            for player in self.active_tournament.players
        ]

    def start_tournament(self):
        for index in range(1,self.active_tournament.number_of_rounds):
            self.active_tournament.update_scores(round.matches)
            print(self.active_tournament.players)
            # if self.active_tournament.number_of_rounds > len(self.active_tournament.rounds):
            current_round = self.active_tournament.get_current_round()
            if (current_round is None):
                self.add_round()
            elif current_round.is_finished():
                self.add_round()
    
    def add_round(self):
        round_name = f"Round {len(self.active_tournament.rounds) + 1}"
        new_round = Round(round_name)
        previous_matches = {
            (match.player1.id, match.player2.id)
            for round in self.active_tournament.rounds
            for match in round.matches
        }
        if len(self.active_tournament.rounds) == 0:
            print("First round")
            pairs = Pairing.generate_first_round_pairs(self.active_tournament.players)
        else:
            print("Next round")
            pairs = Pairing.generate_next_round_pairs(
                self.active_tournament.players, previous_matches)
            print(pairs)
        for player1, player2 in pairs:
            new_round.add_match(player1, player2)
        self.active_tournament.rounds.append(new_round)
        self.view.display_added_round_message(round_name)
    
    def update_number_of_rounds(self, new_number_of_rounds):
        self.active_tournament.set_number_of_rounds(new_number_of_rounds)

    def update_description(self, description):
        self.active_tournament.set_description(description)

    def enter_scores(self):
        round_instance = self.active_tournament.get_current_round()
        self.view.display_record_results_message(round_instance.name)
        for match in round_instance.matches:
            if round_instance.is_finished():
                continue
            self.view.display_match_summary(match.get_player_names())
            result = self.view.get_match_result()
            if result == "1":
                match.set_score(1, 0)
            elif result == "2":
                match.set_score(0, 1)
            elif result == "0":
                match.set_score(0.5, 0.5)
            SaveTournamentCommand(self).execute()
        round_instance.end_round()
        SaveTournamentCommand(self).execute()

    def save_players_data(self, players_data):
        """Sauvegarder les données des joueurs dans un fichier JSON."""
        TournamentLoaderService.save_players(players_data)
