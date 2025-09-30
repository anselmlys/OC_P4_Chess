import re
import re
import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path


national_chess_id_format = re.compile(r"^[a-zA-Z]{2}[0-9]{5}$")

national_chess_id_format = re.compile(r"^[a-zA-Z]{2}[0-9]{5}$")

@dataclass
class Player:
    last_name: str
    first_name: str
    date_of_birth: date
    national_chess_id: str

    def __post_init__(self):
        if not national_chess_id_format.match(self.national_chess_id):
            raise ValueError("Format attendu : deux lettres puis cinq chiffres")

    def save_new_player_information(self, filepath):
        '''Save the player data in the json file storing player information'''
    def __post_init__(self):
        if not national_chess_id_format.match(self.national_chess_id):
            raise ValueError("Format attendu : deux lettres puis cinq chiffres")

    def save_new_player_information(self, filepath):
        '''Save the player data in the json file storing player information'''
        players_file = Path(filepath)
        if players_file.is_file():
            with open(filepath) as json_file:
                players_data = json.load(json_file)
                players_data["players"].append(asdict(self))

            with open(filepath, "w", encoding='utf-8') as json_file:
                json.dump(players_data, json_file, indent=4)
        else:
            with open(filepath, 'w', encoding='utf-8') as json_file:
                data = {"players": []}
                data["players"].append(asdict(self))
                json.dump(data, json_file, indent=4)


class InGamePlayer:
    def __init__(self, player: Player, number: int):
        self.player = player
        self.number = number
        self.score = 0

    def __repr__(self):
        return (f"{self.number}- "
                f"{self.player['last_name']} {self.player['first_name']}"
                f" - {self.score}")