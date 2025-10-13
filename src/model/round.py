from datetime import datetime
from dataclasses import dataclass, field

from src.model.match import Match
from src.model.player import InGamePlayer


@dataclass
class Round:
    name: str
    pair_of_players: list
    start_datetime: datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    end_datetime: datetime | None = None
    matches: list = field(default_factory=list)

    def __post_init__(self):
        if self.matches:
            for match in self.matches:
                match.add_listener(self._on_match_finished)

    @property
    def finished(self) -> bool:
        return all(match.finished for match in self.matches)

    def __repr__(self):
        return self.name

    def transform_to_dict(self):
        return {
            "name": self.name,
            "pair_of_players": [
                [a.transform_to_dict(), b.transform_to_dict()]
                for a, b in self.pair_of_players
            ],
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": [match.transform_to_dict() for match in self.matches],
        }

    @classmethod
    def transform_from_dict(cls, json_data):
        pair_of_players = [
                (InGamePlayer.transform_from_dict(a),
                 InGamePlayer.transform_from_dict(b))
                for a, b in json_data["pair_of_players"]
            ]
        matches = [Match.transform_from_dict(match) for match in json_data["matches"]]

        return cls(
            name=json_data["name"],
            pair_of_players=pair_of_players,
            start_datetime=json_data["start_datetime"],
            end_datetime=json_data["end_datetime"],
            matches=matches,
        )

    def create_matches(self):
        '''Create the matches inside this round.'''
        for pair in self.pair_of_players:
            match = Match(pair)
            self.matches.append(match)

        # Link observer to the objects (matches) it wants to listen to
        for match in self.matches:
            match.add_listener(self._on_match_finished)

    def _on_match_finished(self, match):
        '''Contains the function that will be called when matches are done'''
        if self.end_datetime is None and self.finished:
            self.end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
