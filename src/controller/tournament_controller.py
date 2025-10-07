from src.constants import PLAYER_DB_FILEPATH
from src.view.tournament.creation_view import TournamentCreationView
from src.view.tournament.selector_view import TournamentSelectorView
from src.view.tournament.running_view import TournamentRunningView
from src.model.tournament import Tournament


class TournamentController:
    def __init__(self, tournament_view):
        self.tournament_view = tournament_view

    def create_tournament(self):
        tournament_name = TournamentCreationView.prompt_tournament_name(self.tournament_view)
        tournament_place = TournamentCreationView.prompt_tournament_place(self.tournament_view)
        tournament_start_date = TournamentCreationView.prompt_tournament_start_date(self.tournament_view)
        tournament_number_of_rounds = TournamentCreationView.prompt_number_of_rounds(self.tournament_view)
        tournament_description = TournamentCreationView.prompt_description(self.tournament_view)

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
            except:
                print("\nUne erreur est survenue, le tournoi n'a pas été enregistré.\n")
        else:
            print(("Attention : le nombre de joueur est impair!\n"
                   "Veuillez ajouter un nouveau joueur avant de continuer.\n"))
            
    def select_tournament(self):
        pass
    
    def run_tournament(self):
        pass