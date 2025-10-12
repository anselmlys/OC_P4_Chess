class TournamentSelectorView:
    def prompt_tournament_to_select(self, tournament_files):
        print(("\nVoici la liste des tournois:"))
        for file in tournament_files:
            print(f"- {file}")
        choice = input("\nEntrez le nom du tournoi que vous souhaitez continuer : ")
        return choice
