from src.model.player import InGamePlayer


class Match:
    def __init__(self, player1: InGamePlayer, player2: InGamePlayer):
        self.player1 = player1
        self.player2 = player2
        self.finished: bool = False
        self.winner: str | None = None

    def __repr__(self):
        return (f"([{self.player1}, {self.player1.score}]," 
                f"[{self.player2}, {self.player2.score}])")
    
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
