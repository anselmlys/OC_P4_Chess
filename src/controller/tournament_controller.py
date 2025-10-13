from os import listdir
from pathlib import Path

from src.constants import PLAYER_DB_FILEPATH, TOURNAMENT_DB_FOLDER
from src.view.tournament.creation_view import TournamentCreationView
from src.view.tournament.selector_view import TournamentSelectorView
from src.view.tournament.managing_view import TournamentManagingView
from src.view.tournament.report_view import TournamentReportView
from src.model.tournament import Tournament


class TournamentController:
    def __init__(self, creation_view: TournamentCreationView,
                 selector_view: TournamentSelectorView,
                 managing_view: TournamentManagingView,
                 report_view: TournamentReportView):
        self.creation_view = creation_view
        self.selector_view = selector_view
        self.managing_view = managing_view
        self.report_view = report_view

    def create_tournament(self):
        tournament_name = self.creation_view.prompt_tournament_name()
        tournament_place = self.creation_view.prompt_tournament_place()
        tournament_start_date = self.creation_view.prompt_tournament_start_date()
        tournament_number_of_rounds = self.creation_view.prompt_number_of_rounds()
        tournament_description = self.creation_view.prompt_description()

        tournament = Tournament(name=tournament_name,
                                place=tournament_place,
                                start_date=tournament_start_date,
                                number_of_rounds=tournament_number_of_rounds,
                                description=tournament_description)

        tournament.add_players(PLAYER_DB_FILEPATH)
        number_of_player = len(tournament.players)
        if (number_of_player % 2) == 0:
            try:
                tournament.create_json_file()
                tournament.save_tournament_information()
                print("\nLe tournoi a bien été créé !\n")
                input("\nPress Enter to continue...\n")
            except PermissionError:
                print(("Accès refusé : "
                       "le tournoi n'a pas été enregistré.\n"))
                input("\nPress Enter to continue...\n")
            except Exception as e:
                print(f"\nUne erreur est survenue : {e}")
                input("\nPress Enter to continue...\n")
        else:
            print(("Attention : le nombre de joueur est impair!\n"
                   "Veuillez ajouter un nouveau joueur avant de continuer.\n"))
            input("\nPress Enter to continue...\n")

    def select_tournament(self):
        tournament_files = [f.removesuffix('.json') for f in listdir(TOURNAMENT_DB_FOLDER)]
        choice = self.selector_view.prompt_tournament_to_select(tournament_files)
        filename = ''.join(e for e in choice if e.isalnum())
        filepath = f"{TOURNAMENT_DB_FOLDER}/{filename}.json"
        tournament_file = Path(filepath)
        if not tournament_file.is_file():
            print("\nAttention : nom de tournoi non valide.\n")
            input("\nPress Enter to continue...\n")
            return self.select_tournament()
        else:
            try:
                tournament = Tournament.get_tournament_information(filepath)
                return tournament
            except FileNotFoundError:
                print(f"\nErreur : le fichier {filename}.json est introuvable.\n")
                input("\nPress Enter to continue...\n")
            except PermissionError:
                print(f"\nErreur : accès au fichier {filename}.json refusé.")
                input("\nPress Enter to continue...\n")
            except Exception as e:
                print(f"\nUne erreur est survenue : {e}")
                input("\nPress Enter to continue...\n")

    def list_tournaments(self):
        tournaments = []
        tournament_files = [f for f in listdir(TOURNAMENT_DB_FOLDER)]
        try:
            for file in tournament_files:
                filepath = f"{TOURNAMENT_DB_FOLDER}/{file}"
                tournament = Tournament.get_tournament_information(filepath)
                tournaments.append(tournament)
            self.report_view.list_of_tournaments(tournaments)
        except FileNotFoundError:
            print(f"\nErreur : le fichier {file} est introuvable.\n")
            input("\nPress Enter to continue...\n")
        except PermissionError:
            print(f"\nErreur : accès au fichier {file} refusé.")
            input("\nPress Enter to continue...\n")
        except Exception as e:
            print(f"\nUne erreur est survenue : {e}")
            input("\nPress Enter to continue...\n")

    def start_tournament(self, tournament: Tournament):
        choice = self.managing_view.tournament_start()
        match choice:
            case "commencer":
                tournament.get_unique_pairs()
                pair_of_players = tournament.create_random_pairs()
                tournament.create_new_round(pair_of_players)
                round_index = tournament.current_round_number - 1
                tournament.rounds[round_index].create_matches()
                try:
                    tournament.save_tournament_information()
                    self.manage_tournament(tournament)
                except PermissionError:
                    print(f"\nErreur : accès au fichier {tournament.db_filepath} refusé.")
                    input("\nPress Enter to continue...\n")
                except Exception as e:
                    print(f"\nUne erreur est survenue : {e}")
                    input("\nPress Enter to continue...\n")

            case "revenir":
                return

    def end_match(self, tournament: Tournament, round_index: int):
        number_of_matches = len(tournament.rounds[round_index].matches)
        match_number = int(self.managing_view.prompt_match_selection(number_of_matches))
        match_index = match_number - 1
        winner = self.managing_view.prompt_match_winner(tournament,
                                                        round_index,
                                                        match_index)
        tournament.rounds[round_index].matches[match_index].end_match(winner)
        try:
            tournament.save_tournament_information()
            self.manage_tournament(tournament)
        except PermissionError:
            print(f"\nErreur : accès au fichier {tournament.db_filepath} refusé.")
            input("\nPress Enter to continue...\n")
        except Exception as e:
            print(f"\nUne erreur est survenue : {e}")
            input("\nPress Enter to continue...\n")

    def create_new_round(self, tournament: Tournament, round_index: int):
        # Check that the current round is over
        if tournament.rounds[round_index].finished:
            # Remove pairs who played together from unique pairs list
            for previous_pair in tournament.previous_pairs:
                if previous_pair in tournament.unique_pairs_left:
                    tournament.unique_pairs_left.remove(previous_pair)

            # Check if there are still unique pairs available or not
            if tournament.unique_pairs_left:
                pair_of_players = tournament.create_unique_pairs()
            else:
                pair_of_players = tournament.create_random_pairs()

            tournament.create_new_round(pair_of_players)
            round_index = tournament.current_round_number - 1
            tournament.rounds[round_index].create_matches()
            try:
                tournament.save_tournament_information()
                self.manage_tournament(tournament)
            except PermissionError:
                print(f"\nErreur : accès au fichier {tournament.db_filepath} refusé.")
                input("\nPress Enter to continue...\n")
            except Exception as e:
                print(f"\nUne erreur est survenue : {e}")
                input("\nPress Enter to continue...\n")
        else:
            print("\nLe tour actuel n'est pas terminé ! \n")
            self.manage_tournament(tournament)

    def manage_tournament(self, tournament: Tournament):
        round_index = tournament.current_round_number - 1
        # Check if tournament is already over or not
        if (int(tournament.number_of_rounds) == int(tournament.current_round_number) and
                tournament.rounds[round_index].finished):
            tournament.end_tournament()
            choice = self.managing_view.tournament_over(tournament)
        else:
            self.managing_view.current_status(tournament, round_index)
            choice = self.managing_view.ongoing_tournament()
        match choice:
            case "match":
                self.end_match(tournament, round_index)
            case "tour":
                self.create_new_round(tournament, round_index)
            case "joueur":
                players = sorted(tournament.players,
                                 key=lambda player: player.player.last_name)
                self.report_view.list_of_players(players)
                self.manage_tournament(tournament)
            case "info":
                self.report_view.tournament_info(tournament)
                self.manage_tournament(tournament)
            case "retour":
                pass
