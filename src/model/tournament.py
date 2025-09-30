import json
import random
import json
import random
from dataclasses import dataclass, field
from datetime import date

from src.model.round import Round
from src.model.player import InGamePlayer
from src.model.round import Round
from src.model.player import InGamePlayer


@dataclass
class Tournament:
    name: str
    place: str
    start_date: date
    end_date: date | None = None
    players: list[InGamePlayer] = field(default_factory=list)
    players: list[InGamePlayer] = field(default_factory=list)
    number_of_rounds: int = 4
    current_round_number: int = 1
    rounds: list[Round] = field(default_factory=list)
    description: str | None = None

    def add_players(self, players_filepath):
        '''Add the players of a json file to the tournament.'''
        player_number = 1
        with open(players_filepath, "r", encoding='utf-8') as players_file:
            players_data = json.load(players_file)
            for player_data in players_data["players"]:
                in_game_player = InGamePlayer(player_data, player_number)
                self.players.append(in_game_player)
                player_number += 1

    def create_new_round(self, shuffled_players):
        '''Create a new round in the tournament.'''
        round_name = f"Round {self.current_round_number}"
        round = Round(round_name, shuffled_players)
        self.rounds.append(round)

    def create_pairs(self) -> list:
        '''Create the list of pairs for each match'''
        number_of_players = len(self.players)
        pairs = []
        for i in range(0, number_of_players, 2):
            pair = (self.players[i], self.players[i+1])
            pairs.append(pair)
        return pairs

    def start_tournament(self):
        '''Create the first round.'''
        random.shuffle(self.players)
        pair_of_players = self.create_pairs()
        self.create_new_round(pair_of_players)
        
