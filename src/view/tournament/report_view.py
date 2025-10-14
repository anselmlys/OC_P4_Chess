class TournamentReportView:
    def list_of_tournaments(self, tournaments: list):
        print("\nVoici la liste des tournois : ")
        for tournament in tournaments:
            print(tournament)
        input("\nPress Enter to continue...\n")

    def list_of_players(self, players: list):
        print("\nVoici la liste des joueurs du tournoi : ")
        for player in players:
            print((f"- {player.player.national_chess_id}- "
                   f"{player.player.last_name.title()} "
                   f"{player.player.first_name.title()} - "
                   f"Score : {player.score}"))
        input("\nPress Enter to continue...\n")

    def tournament_info(self, tournament):
        print((f"\nNom : {tournament.name.title()}\n"
               f"Lieu : {tournament.place.title()}\n"
               f"Date de début : {tournament.start_date}\n"
               f"Date de fin : {tournament.end_date}\n"))
        print("Voici l'ensemble des tours et de leurs matchs :")
        for round in tournament.rounds:
            print((f"\nNom : {round.name}\n"
                   f"Date de début : {round.start_datetime}\n"
                   f"Date de fin : {round.end_datetime}"))
            match_number = 1
            for match in round.matches:
                print(f"Match {match_number} : {match}")
                match_number += 1
        input("\nPress Enter to continue...\n")
