class TournamentMenuView:
    def prompt_menu_choices(self):
        print(("\nQue souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Créer un nouveau tournoi : <creer>\n"
               "- Gérer un tournoi : <gerer>\n"                
               "- Voir liste des tournois : <liste>\n"
               "- Retourner au menu principal : <retour>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        options = ["creer", "gerer", "liste", "retour"]
        choice = input(message_input)
        if choice in options:
            return choice
        else:
            print(("\nAttention : seules les commandes "
                   "listées sont disponibles !\n"))
            return self.prompt_menu_choices()