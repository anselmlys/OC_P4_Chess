from src.model.player import InGamePlayer


class Match:
    def __init__(self, pair_of_players):
        self.player1 = pair_of_players[0]
        self.player2 = pair_of_players[1]
        self.finished: bool = False
        self.winner: str | None = None
        self._listeners: list = []

    def __repr__(self):
        return (f"([{self.player1}, {self.player1.score}]," 
                f"[{self.player2}, {self.player2.score}])")
    
    def add_listener(self, callback):
        '''Allow observers (here "Round") to listen to changes'''
        self._listeners.append(callback)

    def _notify(self):
        '''Will launch callback functions in listeners when match is done'''
        for callback in self._listeners:
            callback(self)
    
    def end_match(self, winner):
        '''Add the points to the score of the winner and set the match to finished'''
        match winner:
            case "player1":
                self.player1.score += 1
                self.winner = self.player1
            case "player2":
                self.player2.score += 1
                self.winner = self.player2
            case "draw":
                self.player1.score += 0.5
                self.player2.score += 0.5
                self.winner = "draw"
        self.finished = True
        self._notify()

        return (f"([{self.player1}, {self.player1.score}]," 
                f"[{self.player2}, {self.player2.score}])")
    
