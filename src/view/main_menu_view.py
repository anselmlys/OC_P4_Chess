class MainMenuView:
    def prompt_menu_choices(self):
        print(("Que souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Gérer les joueurs : <joueur>\n"
               "- Gérer les tournois : <tournoi>\n"
               "- Fermer le programme : <fermer>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        options = ["joueur", "tournoi", "fermer"]
        choice = input(message_input)
        if choice in options:
            return choice 
        else:
            print(("\nAttention : seules les commandes "
                   "listées sont disponibles !\n"))
            return self.prompt_menu_choices()