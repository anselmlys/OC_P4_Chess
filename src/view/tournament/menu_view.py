class TournamentMenuView:
    def prompt_menu_choices(self):
        print(("\nQue souhaitez-vous faire ? (les commandes disponibles "
               "sont représentées entre <>) : \n"
               "- Créer un nouveau tournoi : <creer>\n"
               "- Lancer/Continuer un tournoi : <continuer>\n"
               "- Retourner au menu principal : <retour>\n"))
               
        message_input = ("Veuillez entrez une commande: ")
        choice = input(message_input)
        return choice 