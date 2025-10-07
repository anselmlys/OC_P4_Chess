class PlayerMenuView:
    def prompt_menu_choices(self):
        print(("Que souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Ajouter un nouveau joueur : <ajouter>\n"
               "- Voir liste des joueurs : <liste>\n"
               "- Retourner au menu principal : <retour>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        choice = input(message_input)
        return choice 