from datetime import datetime

from src.model.match import Match


class Round:
    def __init__(self, name: str, pair_of_players: list):
        self.name: str = name
        self.pair_of_players: list = pair_of_players
        self.start_datetime = datetime.now().strftime("%Y-%m-%d %H:%m")
        self.end_datetime: datetime | None = None
        self.matches: list = []
        
    @property
    def finished(self) -> bool:
        return all(match.finished for match in self.matches)

    def __repr__(self):
        return self.name
    
    def finish_round(self):
        if not self.finished:
            self.finished = True
            self.end_datetime = datetime.now().strftime("%Y-%m-%d %H:%m")

    def create_matches(self):
        '''Create the matches inside this round.'''
        for pair in self.pair_of_players:
            match = Match(pair)
            self.matches.append(match)



            

            

