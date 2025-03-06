from commands.command import Command


class TournamentCommand(Command):
    def __init__(self, tournament, view=None, menu=None):
        self.tournament = tournament
        self.view = view
        self.menu = menu


class LoadTournamentCommand(TournamentCommand):
    def __init__(self, tournament, menu):
        super().__init__(tournament, menu=menu)

    def execute(self):
        self.menu.set_tournament_loaded(True)
        return f"Tournoi {self.tournament.name} chargé."


class NewTournamentCommand(TournamentCommand):
    def execute(self):
        name = self.view.get_tournament_name()
        location = self.view.get_tournament_location()
        start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()
        number_of_rounds = 4
        self.tournament.set_tournament(
            name, location, start_date, end_date, number_of_rounds,
            [], None, [],
        )
        self.menu.set_tournament_loaded(True)
        save_message = self.save_tournament()
        return f"Nouveau tournoi {name} créé et {save_message}"


class AddDescriptionCommand(TournamentCommand):
    def execute(self):
        description = self.view.get_tournament_description()
        self.tournament.set_description(description)
        save_message = self.save_tournament()
        return f"Description ajoutée: {description} et {save_message}"


class AddPlayersCommand(TournamentCommand):
    def __init__(self, tournament, players):
        super().__init__(tournament)
        self.players = players

    def execute(self):
        for player in self.players:
            self.tournament.add_player(player)
        save_message = self.save_tournament()
        existing_players = self.file_manager.load_all_players()
        updated_players = existing_players + [
            player.to_dict() for player in self.players
        ]
        self.file_manager.save_players(updated_players)
        return f"Joueurs ajoutés et {save_message}"


class RecordResultsCommand(TournamentCommand):
    def execute(self):
        round_instance = self.tournament.get_current_round()
        self.view.display_record_results_message(round_instance.name)
        for match in round_instance.matches:
            if match.is_finished():
                continue
            self.view.display_match_summary(match.get_player_names())
            result = self.view.get_match_result()
            if result == "1":
                match.set_score(1, 0)
            elif result == "2":
                match.set_score(0, 1)
            elif result == "0":
                match.set_score(0.5, 0.5)
            save_message = self.save_tournament()
        round_instance.end_round()
        save_message = self.save_tournament()
        return f"Résultats enregistrés et {save_message}"


class UpdateNumberOfRoundsCommand(TournamentCommand):
    def execute(self):
        number_of_rounds = self.view.get_tournament_number_of_rounds()
        self.tournament.set_number_of_rounds(number_of_rounds)
        save_message = self.save_tournament()
        return (
            f"Nombre de tours mis à jour à {number_of_rounds} "
            f"et {save_message}"
        )


class DisplayCommand(Command):
    def __init__(self, tournament, view):
        self.tournament = tournament
        self.view = view


class DisplayCurrentRoundNoCommand(DisplayCommand):
    def execute(self):
        round_no = {
            "current_round": self.tournament.current_round,
            "number_of_rounds": self.tournament.number_of_rounds
            }
        self.view.display_current_round_no(round_no)


class DisplayPlayerPairsCommand(DisplayCommand):
    def execute(self):
        round_name, pairs = self.tournament.get_current_pairs_players()
        self.view.display_player_pairs(round_name, pairs)


class DisplayPlayersCommand(DisplayCommand):
    def execute(self):
        players_data = [
            {
                "full_name": player.full_name,
                "birth_date": player.formatted_birth_date(),
                "id_chess": player.id_chess
            }
            for player in self.tournament.players
        ]
        self.view.display_players(players_data)


class DisplayTournamentPlayersCommand(DisplayCommand):
    def execute(self):
        players_names = [
            player.full_name for player in self.tournament.players
        ]
        self.view.display_tournament_players(players_names)


class DisplayCurrentRound(DisplayCommand):
    def execute(self):
        current_round = self.tournament.get_current_round()
        if current_round:
            round = {
                "name": current_round.name,
                "start_date": current_round.start_datetime,
                "end_date": current_round.end_datetime
            }
            self.view.display_round_info(round)
        else:
            self.view.display_no_round()


class DisplayTournamentDetailsCommand(DisplayCommand):
    def execute(self):
        tournament = {
            "name": self.tournament.name,
            "location": self.tournament.location,
            "start_date": self.tournament.start_date,
            "end_date": self.tournament.end_date,
            "description": self.tournament.description,
            "number_of_rounds": self.tournament.number_of_rounds
        }
        self.view.display_tournament_details(tournament)
