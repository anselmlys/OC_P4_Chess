from src.model.tournament import Tournament


def main():
    players_filepath = "data/player/players.json"

    tournament1 = Tournament("first", "Paris", 19950909)
    tournament1.add_players(players_filepath)
    tournament1.start_tournament()
    tournament1.rounds[0].create_matches()
    

    tournament1.rounds[0].matches[0].end_match("player1")
    tournament1.rounds[0].matches[1].end_match("player2")
    tournament1.rounds[0].matches[2].end_match("draw")
    print(tournament1.rounds[0].finished)
    print(tournament1.rounds[0].matches)

    tournament1.players.sort(key=lambda x: x.score, reverse=True)
    print(tournament1.players)



if __name__ == "__main__":
    main()