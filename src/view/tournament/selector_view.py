class TournamentSelectorView:
    def prompt_tournament_to_select(self):
        print(("Si vous avez un doute sur le nom du tournoi, vous pouvez "
               "retrouver la liste des tournois en entrant <liste>.\n"))
        choice = input("Veuillez entrer le nom du tournoi : ")
        return choice
