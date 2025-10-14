# OC Project 4: Chess

This project is carried out as part of the OpenClassrooms training program. 
It can be used to manage chess tournaments (register players, manage rounds and matches, display reports). All player and tournament data is stored in JSON files.


## Features
- Register new players.
- Create new tournaments.
- Manage tournament rounds and matches.
- Display reports:
    - List of registered players (in alphabetical order).
    - List of tournaments.
    - Name and dates of a specific tournament.
    - List of players in a tournament (in alphabetical order).
    - List of all rounds and matches of a tournament.

- Saves player information in a JSON file.
- Saves tournament information in a JSON file named after the tournament.


## Installation
1. Clone this repository:
```bash
git clone https://github.com/anselmlys/OC_P4_Chess.git
```

2. Create and activate virtual environment:
```bash
python -m venv env
. env/Scripts/activate
```

3. Install dependencies:
```bash
pip install flake8
pip install flake8-html
```


## Usage
To run the program:
```bash
python chess_app.py
```

To navigate through the menus, just enter one of the listed commands.
All modifications done to the registered players or the tournaments are automatically saved in the JSON files.


## Dependencies

- Python 3.10+
- flake8
- flake8-html


## Notes

The scraper is designed for educational purposes only.


## Author

Anselmlys
