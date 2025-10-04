from src.controller.player_controller import PlayerController
from src.view.main_menu_view import MainMenuView

class MenuController:
    def __init__(self, main_menu_view: MainMenuView, 
                 player_controller: PlayerController):
        self.player_controller = player_controller
        self.main_menu_view = main_menu_view

    def main_menu_user_choice(self):
        choice = MainMenuView.prompt_menu_choices(self.main_menu_view)
        match choice:
            case "joueur":
                self.player_controller.get_player_information()
                self.main_menu_user_choice()
            case "fermer":
                exit()
            case _:
                print(("\nAttention : seules les commandes "
                      "listées sont disponibles !\n"))
                self.main_menu_user_choice()

