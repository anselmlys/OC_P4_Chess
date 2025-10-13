# Controllers
from src.controller.menu_controller import MenuController
from src.controller.player_controller import PlayerController
from src.controller.tournament_controller import TournamentController

# Views
from src.view.main_menu_view import MainMenuView
from src.view.player.menu_view import PlayerMenuView
from src.view.player.register_view import PlayerRegisterView
from src.view.player.list_view import PlayerListView
from src.view.tournament.menu_view import TournamentMenuView
from src.view.tournament.creation_view import TournamentCreationView
from src.view.tournament.selector_view import TournamentSelectorView
from src.view.tournament.managing_view import TournamentManagingView
from src.view.tournament.report_view import TournamentReportView


class AppController:
    def launch_app(self):
        # Instantiate views
        main_menu_view = MainMenuView()
        player_menu_view = PlayerMenuView()
        player_register_view = PlayerRegisterView()
        player_list_view = PlayerListView()
        tournament_menu_view = TournamentMenuView()
        tournament_creation_view = TournamentCreationView()
        tournament_selector_view = TournamentSelectorView()
        tournament_managing_view = TournamentManagingView()
        tournament_report_view = TournamentReportView()

        # Instantiate controllers
        player_controller = PlayerController(player_register_view,
                                             player_list_view)
        tournament_controller = TournamentController(tournament_creation_view,
                                                     tournament_selector_view,
                                                     tournament_managing_view,
                                                     tournament_report_view)
        menu_controller = MenuController(main_menu_view, player_menu_view,
                                         tournament_menu_view, player_controller,
                                         tournament_controller)

        menu_controller.main_menu_user_choice()
