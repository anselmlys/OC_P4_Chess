from dataclasses import dataclass, field
from datetime import date

from round import Round
from player import Player


@dataclass
class Tournament:
    name: str
    place: str
    start_date: date
    end_date: date | None = None
    number_of_rounds: int = 4
    current_round_number: int = 1
    rounds: list[Round] = field(default_factory=list)
    players: list[Player] = field(default_factory=list)
    description: str | None = None

        