class TournamentRunningView:
    def tournament_status(self, tournament):
        print((f"\nSituation du tournoi:\n"
               f"- Tour actuel : Tour {tournament.current_round_number}\n"
               f"- Tour terminé : {tournament.rounds[tournament.current_round_number].finished}\n"
               f"- Nombre de tour prévu : {tournament.number_of_rounds}\n"
               f"\nSouhaitez vous <continuer> ce tournoi ou <revenir> "
               f"en arrière ?\n"))
        choice = input("Veuillez entrez une commande: ")
