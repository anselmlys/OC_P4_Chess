from datetime import datetime, timezone


class Round:
    def __init__(self, name: str):
        self.name = name
        self.start_datetime = datetime.now(timezone.utc)
        self.end_datetime = None
        self.matchs = []