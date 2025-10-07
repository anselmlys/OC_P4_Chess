from src.constants import PLAYER_DB_FILEPATH
from src.model.player import Player
from src.view.player.register_view import PlayerRegisterView

class PlayerController:
    def __init__(self, view):
        self.view = view

    def get_player_information(self):
        last_name = PlayerRegisterView.prompt_player_last_name(self.view)
        first_name = PlayerRegisterView.prompt_player_first_name(self.view)
        date_of_birth = PlayerRegisterView.prompt_player_date_of_birth(self.view)
        national_chess_id = PlayerRegisterView.prompt_player_national_chess_id(self.view)

        player = Player(last_name, first_name, date_of_birth, national_chess_id)
        try:
            Player.save_new_player_information(player, PLAYER_DB_FILEPATH)
            PlayerRegisterView.confirm_player_registered(self.view, player.last_name,
                                                    player.first_name)
        except:
            print("Une erreur est survenue, le joueur n'a pas été enregistré.")


        

