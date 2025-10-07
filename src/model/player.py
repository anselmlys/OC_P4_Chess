import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path


@dataclass
class Player:
    last_name: str
    first_name: str
    date_of_birth: date
    national_chess_id: str

    def transform_to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
        }

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
                json.dump(data, json_file, indent=4, ensure_ascii=False)


class InGamePlayer:
    def __init__(self, player: Player):
        self.player = player
        self.score = 0
    
    def transform_to_dict(self):
        return {
            "player": self.player.transform_to_dict(),
            "score": self.score,
        }