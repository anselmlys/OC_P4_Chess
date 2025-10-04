from src.controller.menu_controller import MenuController
from src.controller.player_controller import PlayerController
from src.view.main_menu_view import MainMenuView
from src.view.player_view import PlayerView


def main():
    main_menu_view = MainMenuView()
    player_view = PlayerView()
    player_controller = PlayerController(player_view)
    menu_controller = MenuController(main_menu_view, player_controller)
    menu_controller.main_menu_user_choice()



if __name__ == "__main__":
    main()