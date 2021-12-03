from dataclasses import dataclass


@dataclass
class Game:
    id: int
    date: str
    week: int
    season: int
    stadium: int
    broadcast: str
    attendance: int
    drives: []
    site: str = "team"

