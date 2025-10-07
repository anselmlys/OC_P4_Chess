from src.controller.menu_controller import MenuController
from src.controller.player_controller import PlayerController
from src.controller.tournament_controller import TournamentController

from src.view.main_menu_view import MainMenuView

from src.view.player.menu_view import PlayerMenuView
from src.view.player.register_view import PlayerRegisterView

from src.view.tournament.menu_view import TournamentMenuView
from src.view.tournament.creation_view import TournamentCreationView
from src.view.tournament.selector_view import TournamentSelectorView


from src.model.tournament import Tournament
from src.constants import PLAYER_DB_FILEPATH


def main():
    '''main_menu_view = MainMenuView()
    player_menu_view = PlayerMenuView()
    player_register_view = PlayerRegisterView()
    tournament_menu_view = TournamentMenuView()
    tournament_creation_view = TournamentCreationView()
    tournament_selector_view = TournamentSelectorView()

    player_controller = PlayerController(player_register_view)
    tournament_controller = TournamentController(tournament_creation_view,
                                                 tournament_selector_view)
    menu_controller = MenuController(main_menu_view=main_menu_view,
                                     player_menu_view=player_menu_view,
                                     tournament_menu_view=tournament_menu_view,
                                     player_controller=player_controller,
                                     tournament_controller=tournament_controller)

    menu_controller.main_menu_user_choice()
'''
    tournament = Tournament("encore un test", "lieu", "2025-10-07")
    tournament.add_players(PLAYER_DB_FILEPATH)
    tournament.get_unique_pairs()
    pair_of_players = tournament.create_random_pairs()
    tournament.create_new_round(pair_of_players)
    tournament.rounds[0].create_matches()
    tournament.rounds[0].matches[0].end_match("player1")
    tournament.rounds[0].matches[1].end_match("player1")
    tournament.rounds[0].matches[2].end_match("player1")
    tournament.create_json_file()
    tournament.save_tournament_bis()

    

if __name__ == "__main__":
    main()