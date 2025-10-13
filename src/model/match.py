from src.model.player import InGamePlayer


class Match:
    def __init__(self, pair_of_players):
        self.player1 = pair_of_players[0]
        self.player2 = pair_of_players[1]
        self.finished: bool = False
        self.winner: str | None = None
        self._listeners: list = []

    def __repr__(self):
        return (([{self.player1}, {self.player1.score}], 
                [{self.player2}, {self.player2.score}]))
    
    def __str__(self):
        if self.winner == "1":
            return ((f"{self.player1} - {self.player1.score} (gagnant) // "
                    f"{self.player2} - {self.player2.score}"))
        elif self.winner == "2":
            return ((f"{self.player1} - {self.player1.score} // "
                    f"{self.player2} - {self.player2.score} (gagnant)"))
        elif self.winner == "match nul":
            return ((f"(Match nul) {self.player1} - {self.player1.score} // "
                    f"{self.player2} - {self.player2.score}"))
        else:
            return ((f"(En cours) {self.player1} - {self.player1.score} // "
                    f"{self.player2} - {self.player2.score}"))
    
    def transform_to_dict(self):
        return {
            "player1": self.player1.transform_to_dict(),
            "player2": self.player2.transform_to_dict(),
            "finished": self.finished,
            "winner": self.winner,
        }
    
    @classmethod
    def transform_from_dict(cls, json_data):
        player1 = InGamePlayer.transform_from_dict(json_data["player1"])
        player2 = InGamePlayer.transform_from_dict(json_data["player2"])
        pair_of_players = [player1, player2]
        match = cls(pair_of_players=pair_of_players)
        match.finished = json_data["finished"]
        match.winner = json_data["winner"]
        
        return match
    
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
            case "1":
                self.player1.score += 1
                self.winner = winner
            case "2":
                self.player2.score += 1
                self.winner = winner
            case "match nul":
                self.player1.score += 0.5
                self.player2.score += 0.5
                self.winner = winner
        self.finished = True
        self._notify()

        return (f"([{self.player1}, {self.player1.score}]," 
                f"[{self.player2}, {self.player2.score}])")
    
