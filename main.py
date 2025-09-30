from src.model.tournament import Tournament


def main():
    players_filepath = "data/player/players.json"

    tournament1 = Tournament("first", "Paris", 19950909)
    tournament1.add_players(players_filepath)
    tournament1.start_tournament()
    tournament1.rounds[0].create_matches()
    print(tournament1.rounds[0].matches)

    print(tournament1.rounds[0].matches[0].finished)
    tournament1.rounds[0].matches[0].end_match("player1")
    print(tournament1.rounds[0].matches[0].finished)
    print(tournament1.rounds[0].matches[0])

    print(tournament1.players)

    


if __name__ == "__main__":
    main()