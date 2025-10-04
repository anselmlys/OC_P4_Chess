import re

#Filepaths
PLAYER_DB_FILEPATH = "data/player/players.json"
TOURNAMENT_DB_FILEPATH = "data/tournaments/tournaments.json"

#Formats
NAME_FORMAT = re.compile(r"[a-zA-Z]+")
NATIONAL_CHESS_ID_FORMAT = re.compile(r"^[a-zA-Z]{2}[0-9]{5}$")
BIRTHDATE_FORMAT = re.compile(r"^[0-9]{4}-[0-1]{1}[0-9]{1}-[0-9]{2}$")