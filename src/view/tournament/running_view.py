from src.constants import INTEGER_FORMAT


class TournamentRunningView:
    def tournament_start(self):
        print((f"\nCe tournoi n'a pas encore commencé.\n"
               f"\nSouhaitez vous le <commencer> ou <revenir> au "
               f"menu principal ?"))
        options = ["commencer", "revenir"]
        choice = input("Veuillez entrez une commande: ")
        if choice in options:
            return choice
        else:
            print("\nAttention : commande inconnue.\n")
            return self.tournament_start()

    def ongoing_tournament(self):
        print((f"\n- Cloturer un match : <match>\n"
               f"- Créer le prochain tour : <tour>\n"
               f"- Revenir au menu principal : <retour>\n"))
        options = ["match", "tour", "retour"]
        choice = input("Veuillez entrez une commande: ")
        if choice in options:
            return choice
        else:
            print("\nAttention : commande inconnue.\n")
            return self.ongoing_tournament()
    
    def prompt_match_selection(self, number_of_matches):
        match_number = input("Veuillez entrer le numéro du match à modifier : ")
        if (not INTEGER_FORMAT.match(match_number) or
            int(match_number) > number_of_matches):
            print("Attention : Veuillez entrer le numéro d'un match ! ")
            return self.prompt_match_selection(number_of_matches)
        else:
            return match_number

    def tournament_over(self):
        print("\nLe tournoi est terminé !\n")

    def current_status(self, tournament, round_index):
        print((f"\nTournoi : {tournament.name.title()}\n"
               f"Nombre de tour : {tournament.number_of_rounds}\n"
               f"Tour actuel : {tournament.current_round_number}\n"
               f"\nVoici les matchs de ce tour : "))
        match_number = 1
        for match in tournament.rounds[round_index].matches:
            print((f"\n- Match {match_number} :\n"
                   f"joueur 1 : {match.player1} - "
                   f"joueur 2 : {match.player2}\n"
                   f"Terminé : {match.finished}\n"
                   f"Gagnant : {match.winner}"))
            match_number +=1

    def prompt_match_winner(self, tournament, round_index, match_index):
        match = tournament.rounds[round_index].matches[match_index]
        print((f"\nJoueur 1 : {match.player1}\n"
               f"Joueur 2 : {match.player2}\n"))
        potential_winner = ["1", "2", "match nul"]
        winner = input("Qui a gagné ? <1> / <2> / <match nul>")
        if not winner in potential_winner:
            print("\nAttention : Veuillez entrer une commande valide !\n")
            return self.prompt_match_winner(tournament, round_index, match_index)
        else:
            return winner
        