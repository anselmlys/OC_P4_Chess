class MainMenuView:
    def prompt_menu_choices(self):
        print(("Que souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Ajouter un joueur : <joueur>\n"
               "- Créer un nouveau tournoi : <tournoi>\n"
               "- Fermer le programme : <fermer>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        choice = input(message_input)
        return choice 
        