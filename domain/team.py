from dataclasses import dataclass


@dataclass
class Team:
    id: int
    name: str
    abbreviation: str
    nickname: str