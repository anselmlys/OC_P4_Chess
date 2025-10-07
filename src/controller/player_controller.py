from src.constants import PLAYER_DB_FILEPATH
from src.model.player import Player
from src.view.player.register_view import PlayerRegisterView

class PlayerController:
    def __init__(self, register_view: PlayerRegisterView):
        self.register_view = register_view

    def get_player_information(self):
        last_name = self.register_view.prompt_player_last_name()
        first_name = self.register_view.prompt_player_first_name()
        date_of_birth = self.register_view.prompt_player_date_of_birth()
        national_chess_id = self.register_view.prompt_player_national_chess_id()

        player = Player(last_name, first_name, date_of_birth, national_chess_id)
        try:
            player.save_new_player_information(PLAYER_DB_FILEPATH)
            self.register_view.confirm_player_registered(player.last_name,
                                                    player.first_name)
        except:
            print("Une erreur est survenue, le joueur n'a pas été enregistré.")


        

