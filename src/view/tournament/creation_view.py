from src.constants import NO_EMPTY_STRING_FORMAT, DATE_FORMAT, INTEGER_FORMAT

class TournamentCreationView:
    def prompt_tournament_name(self):
        tournament_name = input("\nVeuillez entrer le nom du tournoi : ")
        if not NO_EMPTY_STRING_FORMAT.match(tournament_name):
            print("Attention : Ce champs ne doit pas être vide ! ")
            self.prompt_tournament_name()
        else:
            return tournament_name.lower()
    
    def prompt_tournament_place(self):
        tournament_place = input("Veuillez entrer le lieu du tournoi : ")
        if not NO_EMPTY_STRING_FORMAT.match(tournament_place):
            print("Attention : Ce champs ne doit pas être vide ! ")
            self.prompt_tournament_place()
        else:
            return tournament_place.lower()
        
    def prompt_tournament_start_date(self):
        tournament_start_date = input(("Veuillez entrer la date de début "
                                      "en format AAAA-MM-JJ : "))
        if not DATE_FORMAT.match(tournament_start_date):
            print('Attention : mauvais format de date.')
            self.prompt_tournament_start_date()
        else:
            return tournament_start_date
        
    def prompt_number_of_rounds(self):
        tournament_number_of_rounds = input(("Veuillez entrer le nombre de "
                                            "tours pour ce tournoi : "))
        if not INTEGER_FORMAT.match(tournament_number_of_rounds):
            print("Attention : seuls les nombres supérieurs à zéro sont acceptés.")
            self.prompt_number_of_rounds()
        else:
            return tournament_number_of_rounds
        
    def prompt_description(self):
        description = input("(Optionnel) Veuillez entrer une description : ")
        return description