import re

# Filepaths
PLAYER_DB_FILEPATH = "data/player/players.json"
TOURNAMENT_DB_FOLDER = "data/tournaments"

# Formats
NO_EMPTY_STRING_FORMAT = re.compile(r"^\S.+$")
TOURNAMENT_NAME_FORMAT = re.compile(r"^[a-zA-Z0-9]*[\sa-zA-Z0-9]+$")
INTEGER_FORMAT = re.compile(r"^[1-9]{1}[0-9]*$")
NAME_FORMAT = re.compile(r"[a-zA-Z]+")
NATIONAL_CHESS_ID_FORMAT = re.compile(r"^[a-zA-Z]{2}[0-9]{5}$")
DATE_FORMAT = re.compile(r"^[0-9]{4}-[0-1]{1}[0-9]{1}-[0-9]{2}$")
