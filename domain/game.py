from dataclasses import dataclass


@dataclass
class Game:
    id: int
    date: str
    season: int
    week: int
    stadium: int
    broadcast: str
    attendance: int
    drives: []
    site: str = "team"

