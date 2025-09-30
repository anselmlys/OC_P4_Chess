from datetime import datetime

from src.model.match import Match


class Round:
    def __init__(self, name: str, players: list):
        self.name: str = name
        self.players: list = players
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
        #Separate the players in two lists to create player1 or player2 lists
        total_number_of_players = len(self.players)
        
        list_player1 = []
        list_player2 = []
        
        for n in range(total_number_of_players):
            if (n % 2) == 0:
                list_player1.append(self.players[n])
            else:
                list_player2.append(self.players[n])

        #Create the matches using the lists player1 and player2
        players_per_match = 2
        number_of_matches = int(total_number_of_players/players_per_match)

        for n in range(number_of_matches):
            player1 = list_player1[n]
            player2 = list_player2[n]
            match = Match(player1, player2)
            self.matches.append(match)



            

            

