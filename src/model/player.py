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

    def __str__(self):
        return (f"{self.national_chess_id} - "
                f"{self.last_name.title()} {self.first_name.title()} "
                f"({self.date_of_birth})")

    def transform_to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
        }
    
    @classmethod
    def transform_from_dict(cls, json_data):
        return cls(
            last_name=json_data["last_name"],
            first_name=json_data["first_name"],
            date_of_birth=json_data["date_of_birth"],
            national_chess_id=json_data["national_chess_id"],
        )

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

    def get_players_data(json_file: str) -> list:
        with open(json_file, "r", encoding="utf-8") as players_file:
            players = []
            players_data = json.load(players_file)
            for player_data in players_data["players"]:
                player = Player.transform_from_dict(player_data)
                players.append(player)
            return players


class InGamePlayer:
    def __init__(self, player: Player, score: int = 0):
        self.player = player
        self.score = score

    def __str__(self):
        return (f"{self.player.national_chess_id}-"
                f"{self.player.last_name} "
                f"{self.player.first_name}")
    
    def transform_to_dict(self):
        return {
            "player": self.player.transform_to_dict(),
            "score": self.score,
        }
    
    @classmethod
    def transform_from_dict(cls, json_data):
        return cls(
            player=Player.transform_from_dict(json_data["player"]),
            score=json_data["score"],
        )