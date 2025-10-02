from itertools import combinations

from src.model.tournament import Tournament
from src.model.tournament import Tournament


def main():
    players_filepath = "data/player/players.json"

    tournament1 = Tournament("first", "Paris", 19950909, number_of_rounds=6)
    tournament1.add_players(players_filepath)


    #Round 1

    tournament1.start_tournament()
    tournament1.rounds[0].create_matches()

    print(f"Round 1: {tournament1.rounds[0].pair_of_players}")
    
    
    tournament1.rounds[0].matches[0].end_match("player1")
    tournament1.rounds[0].matches[1].end_match("player2")
    tournament1.rounds[0].matches[2].end_match("draw")

    print(tournament1.rounds[0].end_datetime)

    
    '''#Round 2

    tournament1.continue_tournament()
    tournament1.rounds[1].create_matches()

    print(f"Round 2: {tournament1.rounds[1].pair_of_players}")
    
    
    tournament1.rounds[1].matches[0].end_match("player1")
    tournament1.rounds[1].matches[1].end_match("player2")
    tournament1.rounds[1].matches[2].end_match("draw")


    #Round 3

    tournament1.continue_tournament()
    tournament1.rounds[2].create_matches()

    print(f"Round 3: {tournament1.rounds[2].pair_of_players}")
    
    tournament1.rounds[2].matches[0].end_match("player1")
    tournament1.rounds[2].matches[1].end_match("player2")
    tournament1.rounds[2].matches[2].end_match("draw")

    #Round 4

    tournament1.continue_tournament()
    tournament1.rounds[3].create_matches()

    print(f"Round 4: {tournament1.rounds[3].pair_of_players}")

    tournament1.rounds[3].matches[0].end_match("player1")
    tournament1.rounds[3].matches[1].end_match("player2")
    tournament1.rounds[3].matches[2].end_match("draw")

    #Round 5

    tournament1.continue_tournament()
    tournament1.rounds[4].create_matches()

    print(f"Round 5: {tournament1.rounds[4].pair_of_players}")

    tournament1.rounds[4].matches[0].end_match("player1")
    tournament1.rounds[4].matches[1].end_match("player2")
    tournament1.rounds[4].matches[2].end_match("draw")

    #Round 6
    
    tournament1.continue_tournament()
    tournament1.rounds[5].create_matches()

    print(f"Round 6: {tournament1.rounds[5].pair_of_players}")

    tournament1.rounds[5].matches[0].end_match("player1")
    tournament1.rounds[5].matches[1].end_match("player2")
    tournament1.rounds[5].matches[2].end_match("draw")'''


if __name__ == "__main__":
    main()