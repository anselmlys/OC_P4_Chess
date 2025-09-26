from player import Player

class Match:
    def __init__(self, id_player1: Player, id_player2: Player, 
                 player1_score: int = 0, player2_score: int = 0):
        self.id_player1 = id_player1
        self.id_player2 = id_player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def __repr__(self):
        return ([{self.id_player1}, {self.player1_score}],
                [{self.id_player2}, {self.player2_score}])
