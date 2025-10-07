from src.controller.menu_controller import MenuController
from src.controller.player_controller import PlayerController
from src.controller.tournament_controller import TournamentController
from src.view.main_menu_view import MainMenuView
from src.view.player.menu_view import PlayerMenuView
from src.view.player.register_view import PlayerRegisterView
from src.view.tournament.menu_view import TournamentMenuView


def main():
    main_menu_view = MainMenuView()
    player_menu_view = PlayerMenuView()
    player_register_view = PlayerRegisterView()
    tournament_menu_view = TournamentMenuView()

    player_controller = PlayerController(player_register_view)
    tournament_controller = TournamentController(tournament_menu_view)
    menu_controller = MenuController(main_menu_view=main_menu_view,
                                     player_menu_view=player_menu_view,
                                     tournament_menu_view=tournament_menu_view,
                                     player_controller=player_controller,
                                     tournament_controller=tournament_controller)

    menu_controller.main_menu_user_choice()


if __name__ == "__main__":
    main()