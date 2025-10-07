import json

from src.constants import PLAYER_DB_FILEPATH, TOURNAMENT_DB_FOLDER
from src.view.tournament.creation_view import TournamentCreationView
from src.view.tournament.selector_view import TournamentSelectorView
from src.view.tournament.running_view import TournamentRunningView
from src.model.tournament import Tournament


class TournamentController:
    def __init__(self, creation_view: TournamentCreationView,
                 selector_view: TournamentSelectorView):
        self.creation_view = creation_view
        self.selector_view = selector_view

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
            except:
                print("\nUne erreur est survenue, le tournoi n'a pas été enregistré.\n")
        else:
            print(("Attention : le nombre de joueur est impair!\n"
                   "Veuillez ajouter un nouveau joueur avant de continuer.\n"))
            
    def select_tournament(self, choice):
        #choice = self.selector_view.prompt_tournament_to_select()
        filename = ''.join(e for e in choice if e.isalnum())
        filepath = f"{TOURNAMENT_DB_FOLDER}/{filename}.json"
        with open(filepath, "r", encoding='utf-8') as tournament_file:
            tournament_data = json.load(tournament_file)
            tournament = Tournament(tournament_data)
        return tournament
            
    
    def run_tournament(self, tournament):
        pass