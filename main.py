from src.model.player import Player


def main():
    filepath = "data/player/players.json"

    player1 = Player('Smith', 'John', '09091999', 'HG63735')
    player1.save_new_player(filepath)

    player2 = Player('Doe', 'Jane', '05051995', 'JG83954')
    player2.save_new_player(filepath)


if __name__ == "__main__":
    main()