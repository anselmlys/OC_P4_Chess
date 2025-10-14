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

2. Move into the project directory, create and activate virtual environment:
```bash
python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS / Linux:
source env/bin/activate
```

3. (Optional) Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```


## Usage
To run the program:
```bash
python chess_app.py
```

To navigate through the menus, just enter one of the listed commands.
All modifications done to the registered players or the tournaments are automatically saved in the JSON files.


## Code review
This code has been checked using flake8 and flake8-html.

To run the analysis again:
```bash
pip install flake8 flake8-html
flake8
```

An HTML report will be generated in the "flake8_rapport" directory.


## Dependencies

- Python 3.10+
- (Optional, for development) flake8, flake8-html


## Notes

This app is designed for educational purposes only.


## Author

Anselmlys
