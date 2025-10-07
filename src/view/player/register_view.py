from src.constants import DATE_FORMAT, NATIONAL_CHESS_ID_FORMAT, NAME_FORMAT


class PlayerRegisterView:
    def prompt_player_last_name(self):
        last_name = input("\nEntrez le nom de famille du joueur : ")
        if not NAME_FORMAT.match(last_name):
            print("Attention : seuls les lettres sont acceptées.")
            self.prompt_player_last_name()
        else:
            return last_name.lower()
    
    def prompt_player_first_name(self):
        first_name = input("Entrez le prénom du joueur : ")
        if not NAME_FORMAT.match(first_name):
            print("Attention : seuls les lettres sont acceptées.")
            self.prompt_player_first_name()
        else:
            return first_name.lower()
    
    def prompt_player_date_of_birth(self):
        date_of_birth = input("Entrez la date de naissance du joueur en format AAAA-MM-JJ : ")
        if not DATE_FORMAT.match(date_of_birth):
            print('Attention : mauvais format de date.')
            self.prompt_player_date_of_birth()
        else:
            return date_of_birth
    
    def prompt_player_national_chess_id(self):
        national_chess_id = input("Entrez l'identifiant national du joueur : ")
        if not NATIONAL_CHESS_ID_FORMAT.match(national_chess_id):
            print('L\'ID doit être composé de 2 chiffres puis 5 lettres.')
            self.prompt_player_national_chess_id()
        else:
            return national_chess_id
    
    def confirm_player_registered(self,last_name, first_name):
        print(f"{first_name.title()} {last_name.title()} a bien été enregistré !\n")