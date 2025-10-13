from src.constants import PLAYER_DB_FILEPATH
from src.model.player import Player
from src.view.player.register_view import PlayerRegisterView
from src.view.player.list_view import PlayerListView

class PlayerController:
    def __init__(self, register_view: PlayerRegisterView,
                 list_view: PlayerListView):
        self.register_view = register_view
        self.list_view = list_view

    def get_player_information(self):
        last_name = self.register_view.prompt_player_last_name().lower()
        first_name = self.register_view.prompt_player_first_name().lower()
        date_of_birth = self.register_view.prompt_player_date_of_birth()
        national_chess_id = self.register_view.prompt_player_national_chess_id()

        player = Player(last_name, first_name, date_of_birth, national_chess_id)
        try:
            player.save_new_player_information(PLAYER_DB_FILEPATH)
            self.register_view.confirm_player_registered(player.last_name,
                                                    player.first_name)
        except PermissionError:
            print(f"\nErreur : accès au fichier {PLAYER_DB_FILEPATH} refusé.")
            input("\nPress Enter to continue...\n")
        except Exception as e:
            print(f"\nUne erreur est survenue : {e}")
            input("\nPress Enter to continue...\n")

    def show_players_list(self):
        players = Player.get_players_data(PLAYER_DB_FILEPATH)
        players = sorted(players, key=lambda player: player.last_name)
        self.list_view.show_list(players)