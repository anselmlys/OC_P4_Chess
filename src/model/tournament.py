import json
import random
from functools import cached_property
from itertools import groupby, combinations
from dataclasses import dataclass, field
from datetime import date

from src.model.round import Round
from src.model.player import InGamePlayer


@dataclass
class Tournament:
    name: str
    place: str
    start_date: date
    end_date: date | None = None
    players: list[InGamePlayer] = field(default_factory=list)
    number_of_rounds: int = 4
    current_round_number: int = 1
    rounds: list[Round] = field(default_factory=list)
    description: str | None = None

    @cached_property
    def unique_pairs(self) -> list:
        '''Get all possible unique pairs of players'''
        self.unique_pairs = []
        unique_pairs_in_tuple = combinations(self.players, 2)
        for a, b in unique_pairs_in_tuple:
            self.unique_pairs.append(set([a, b]))
        return self.unique_pairs
    
    @property
    def previous_pairs(self) -> list:
        '''Get the pair of players that already played against eachother
        during previous rounds'''
        previous_pairs = []
        for round in self.rounds:
            for a, b in round.pair_of_players:
                previous_pairs.append(set([a, b]))
        return previous_pairs

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

    def create_random_pairs(self):
        pair_of_players = []
        players_list = self.players.copy()
        random.shuffle(players_list)
        while players_list:
            pair = (players_list.pop(0), players_list.pop(0))
            pair_of_players.append(pair)
            
        return pair_of_players
    
    def create_unique_pairs(self, previous_pairs):
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
                while pair in previous_pairs:
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
    
    def start_tournament(self):
        '''Create the first round of the tournament'''
        number_of_players = len(self.players)
        if (number_of_players % 2) == 0:
            pair_of_players = self.create_random_pairs()
            self.create_new_round(pair_of_players)
        else:
            print("Nombre de joueur est impair!")
        
    def continue_tournament(self):
        #Check if there are remaining rounds to play or not
        if self.current_round_number < self.number_of_rounds:
            #Check if all matches are done in current round
            if all(round.finished for round in self.rounds):
                #Change current round number
                self.current_round_number += 1

                #Remove pairs who played together from unique pairs list
                for previous_pair in self.previous_pairs:
                    if previous_pair in self.unique_pairs:
                        self.unique_pairs.remove(previous_pair)

                #Check if there are still unique pairs available or not
                if self.unique_pairs:
                    pair_of_players = self.create_unique_pairs(self.previous_pairs)
                else:
                    pair_of_players = self.create_random_pairs()

                self.create_new_round(pair_of_players)
            else:
                #A déplacer dans "view"
                print("Le tour précédent n'est pas terminé!")
        else:
            #A déplacer dans "view"
            print("Le tournoi est terminé !")
