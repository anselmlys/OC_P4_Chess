import json
import random
from functools import cached_property
from itertools import groupby, combinations
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from src.constants import TOURNAMENT_DB_FOLDER
from src.model.round import Round
from src.model.player import InGamePlayer, Player


@dataclass
class Tournament:
    name: str
    place: str
    start_date: date
    end_date: date | None = None
    players: list[InGamePlayer] = field(default_factory=list)
    number_of_rounds: int = 4
    current_round_number: int = 0
    rounds: list[Round] = field(default_factory=list)
    description: str | None = None
    unique_pairs_left: list = field(default_factory=list)
    db_filepath: str | None = None

    @property
    def previous_pairs(self) -> list:
        '''Get the pair of players that already played against eachother
        during previous rounds'''
        previous_pairs = []
        for round in self.rounds:
            for a, b in round.pair_of_players:
                previous_pairs.append(set([a, b]))
        return previous_pairs

    def transform_to_dict(self):
        unique_pairs_left = [
            [a.transform_to_dict(), b.transform_to_dict()] for a, b in self.unique_pairs_left
        ]

        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": [player.transform_to_dict() for player in self.players],
            "number_of_rounds": self.number_of_rounds,
            "current_round_number": self.current_round_number,
            "rounds": [round.transform_to_dict() for round in self.rounds],
            "description": self.description,
            "unique_pairs_left": unique_pairs_left,
            "db_filepath": self.db_filepath,
        }
    
    @classmethod
    def transform_from_dict(cls, json_data):
        players = [
            InGamePlayer.transform_from_dict(player) for player in json_data["players"]
        ]
        rounds = [
            Round.transform_from_dict(round) for round in json_data["rounds"]
        ]
        unique_pairs_left = [
            (InGamePlayer.transform_from_dict(a),
             InGamePlayer.transform_from_dict(b)) 
             for a, b in json_data["unique_pairs_left"]
        ]

        return cls(
            name=json_data["name"],
            place=json_data["place"],
            start_date=json_data["start_date"],
            end_date=json_data["end_date"],
            players=players,
            number_of_rounds=json_data["number_of_rounds"],
            current_round_number=json_data["current_round_number"],
            rounds=rounds,
            description=json_data["description"],
            unique_pairs_left=unique_pairs_left,
            db_filepath=json_data["db_filepath"],
        )

    def add_players(self, players_filepath):
        '''Add the players of a json file to the tournament.'''
        with open(players_filepath, "r", encoding='utf-8') as players_file:
            players_data = json.load(players_file)
            for player_data in players_data["players"]:
                player = Player(last_name=player_data["last_name"],
                                first_name=player_data["first_name"],
                                date_of_birth=player_data["date_of_birth"],
                                national_chess_id=player_data["national_chess_id"])
                in_game_player = InGamePlayer(player)
                self.players.append(in_game_player)

    def get_unique_pairs(self) -> list:
        '''Get all possible unique pairs of players'''
        unique_pairs_in_tuple = combinations(self.players, 2)
        for a, b in unique_pairs_in_tuple:
            self.unique_pairs_left.append(set([a, b]))
    
    def create_new_round(self, pair_of_players):
        '''Create a new round in the tournament.'''
        self.current_round_number += 1
        round_name = f"Round {self.current_round_number}"
        round = Round(round_name, pair_of_players)
        self.rounds.append(round)

    def create_random_pairs(self):
        pair_of_players = []
        players_list = self.players.copy()
        random.shuffle(players_list)
        while players_list:
            pair = (players_list.pop(0), players_list.pop(0))
            pair_of_players.append(pair)
            
        return pair_of_players
    
    def create_unique_pairs(self):
        '''Pair together players who have not played against eachother'''
        #Sort all players based on their scores
        sorted_players = self.players.copy()
        sorted_players.sort(key=lambda x: x.score, reverse=True)

        #Shuffle between players who have the same score
        shuffled_players = []
        for _, group in groupby(sorted_players, key=lambda x: x.score):
            g = list(group)
            random.shuffle(g)
            shuffled_players.extend(g)

        #Pair together the two first players in the shuffled_players list
        pair_of_players = []
        while len(shuffled_players) > 0:
            n = 0
            player_to_pair = shuffled_players.pop(n)
            player_to_pair_with = shuffled_players[n]
            pair = set({player_to_pair, player_to_pair_with})

            #Change second player if the pair already played together
            try:
                while pair in self.previous_pairs:
                    n += 1
                    player_to_pair_with = shuffled_players[n]
                    pair = set({player_to_pair, player_to_pair_with})

            #Keep original pair if no unique pairs were found
            except:
                n = 0

            #Create the tuple for the pair and add it to the list of pairs
            finally:
                player_to_pair_with = shuffled_players.pop(n)
                pair = (player_to_pair, player_to_pair_with)
                pair_of_players.append(pair)

        return pair_of_players
        
    def continue_tournament(self):
        #Check if there are remaining rounds to play or not
        if self.current_round_number < self.number_of_rounds:
            #Check if all matches are done in current round
            if all(round.finished for round in self.rounds):
                #Change current round number
                self.current_round_number += 1

                #Remove pairs who played together from unique pairs list
                for previous_pair in self.previous_pairs:
                    if previous_pair in self.unique_pairs_left:
                        self.unique_pairs_left.remove(previous_pair)

                #Check if there are still unique pairs available or not
                if self.unique_pairs_left:
                    pair_of_players = self.create_unique_pairs()
                else:
                    pair_of_players = self.create_random_pairs()

                self.create_new_round(pair_of_players)
            else:
                #A déplacer dans "view"
                print("Le tour précédent n'est pas terminé!")
        else:
            #A déplacer dans "view"
            print("Le tournoi est terminé !")

    def create_json_file(self) -> str:
        '''Create the file that will store the tournament data'''
        filename = ''.join(e for e in self.name if e.isalnum())
        filepath = f"{TOURNAMENT_DB_FOLDER}/{filename}.json"
        tournament_file = Path(filepath)
        n = 2
        while tournament_file.is_file():
            filepath = f"{TOURNAMENT_DB_FOLDER}/{filename}{n}.json"
            tournament_file = Path(filepath)
            n += 1
        with open(filepath, 'w', encoding='utf-8') as json_file:
            data = {}
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        self.db_filepath = filepath

    def save_tournament_information(self):
        with open(self.db_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(self.transform_to_dict(), json_file, indent=4, ensure_ascii=False)

    def get_tournament_information(json_file):
        with open(json_file, "r", encoding="utf-8") as tournament_file:
            tournament_data = json.load(tournament_file)
            tournament = Tournament.transform_from_dict(tournament_data)
        return tournament