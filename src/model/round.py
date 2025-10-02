from datetime import datetime

from src.model.match import Match


class Round:
    def __init__(self, name: str, pair_of_players: list):
        self.name: str = name
        self.pair_of_players: list = pair_of_players
        self.start_datetime = datetime.now().strftime("%Y-%m-%d %H:%m")
        self.end_datetime: datetime | None = None
        self.matches: list = []

    def __post_init__(self):
        #Link observer to the objects it wants to listen to
        for match in self.matches:
            match.add_listener(self._on_match_finished)
        
    @property
    def finished(self) -> bool:
        return all(match.finished for match in self.matches)

    def __repr__(self):
        return self.name

    def create_matches(self):
        '''Create the matches inside this round.'''
        for pair in self.pair_of_players:
            match = Match(pair)
            self.matches.append(match)

        for match in self.matches:
            match.add_listener(self._on_match_finished)

    def _on_match_finished(self, match):
        '''Contains the function that will be called when matches are done'''
        if self.end_datetime is None and self.finished:
            self.end_datetime = datetime.now().strftime("%Y-%m-%d %H:%m")



            

            

