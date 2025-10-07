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
        choice = MainMenuView.prompt_menu_choices(self.main_menu_view)
        match choice:
            case "joueur":
                self.player_menu_user_choice()
            case "tournoi":
                self.tournament_menu_user_choice()
            case "fermer":
                exit()
            case _:
                print(("\nAttention : seules les commandes "
                      "listées sont disponibles !\n"))
                self.main_menu_user_choice()

    def player_menu_user_choice(self):
        choice = PlayerMenuView.prompt_menu_choices(self.player_menu_view)
        match choice:
            case "ajouter":
                self.player_controller.get_player_information()
                self.player_menu_user_choice()
            case "liste":
                #Ajouter la liste des joueurs
                self.main_menu_user_choice()
            case "retour":
                self.main_menu_user_choice()
            case _:
                print(("\nAttention : seules les commandes "
                      "listées sont disponibles !\n"))
                self.tournament_menu_user_choice()

    def tournament_menu_user_choice(self):
        choice = TournamentMenuView.prompt_menu_choices(self.tournament_menu_view)
        match choice:
            case "creer":
                self.tournament_controller.create_tournament()
                self.tournament_menu_user_choice()
            case "gerer":
                #Ajouter la gestion de tournoi
                self.main_menu_user_choice()
            case "retour":
                self.main_menu_user_choice()
            case _:
                print(("\nAttention : seules les commandes "
                      "listées sont disponibles !\n"))
                self.tournament_menu_user_choice()

