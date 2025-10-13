class TournamentReportView:
    def list_of_tournaments(self, tournaments: list):
        print("\nVoici la liste des tournois : ")
        for tournament in tournaments:
            print(tournament)

    def list_of_players(self, players: list):
        print("\nVoici la liste des joueurs du tournoi : ")
        for player in players:
            print((f"- {player.player.national_chess_id}- "
                   f"{player.player.last_name} {player.player.first_name} - "
                   f"Score : {player.score}"))

    def tournament_info(self, tournament):
        pass