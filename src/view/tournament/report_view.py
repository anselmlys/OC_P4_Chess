class TournamentReportView:
    def list_of_tournaments(self, tournaments: list):
        print("\nVoici la liste des tournois : ")
        for tournament in tournaments:
            print(tournament)