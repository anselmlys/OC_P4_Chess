from src.controller.player_controller import PlayerController
from src.controller.tournament_controller import TournamentController
from src.view.main_menu_view import MainMenuView
from src.view.player.menu_view import PlayerMenuView
from src.view.tournament.menu_view import TournamentMenuView

class MenuController:
    def __init__(self, main_menu_view: MainMenuView,
                 player_menu_view: PlayerMenuView,
                 tournament_menu_view: TournamentMenuView, 
                 player_controller: PlayerController,
                 tournament_controller: TournamentController):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller
        self.main_menu_view = main_menu_view
        self.player_menu_view = player_menu_view
        self.tournament_menu_view = tournament_menu_view

    def main_menu_user_choice(self):
        choice = self.main_menu_view.prompt_menu_choices()
        match choice:
            case "joueur":
                self.player_menu_user_choice()
            case "tournoi":
                self.tournament_menu_user_choice()
            case "fermer":
                exit()

    def player_menu_user_choice(self):
        choice = self.player_menu_view.prompt_menu_choices()
        match choice:
            case "ajouter":
                self.player_controller.get_player_information()
                self.player_menu_user_choice()
            case "liste":
                #Ajouter la liste des joueurs
                pass
            case "retour":
                self.main_menu_user_choice()

    def tournament_menu_user_choice(self):
        choice = self.tournament_menu_view.prompt_menu_choices()
        match choice:
            case "creer":
                self.tournament_controller.create_tournament()
                self.tournament_menu_user_choice()
            case "continuer":
                tournament = self.tournament_controller.select_tournament()
                #Check if tournament has already started or not
                if tournament.current_round_number == 0:
                    self.tournament_controller.start_tournament(tournament)
                else:
                    self.tournament_controller.run_tournament(tournament)
            case "retour":
                pass
        self.main_menu_user_choice()

