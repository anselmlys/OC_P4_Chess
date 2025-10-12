class PlayerMenuView:
    def prompt_menu_choices(self):
        print(("\nQue souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Ajouter un nouveau joueur : <ajouter>\n"
               "- Voir liste des joueurs : <liste>\n"
               "- Retourner au menu principal : <retour>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        options = ["ajouter", "liste", "retour"]
        choice = input(message_input)
        if choice in options:
            return choice 
        else:
            print(("\nAttention : seules les commandes "
                    "listées sont disponibles !\n"))
            return self.prompt_menu_choices()