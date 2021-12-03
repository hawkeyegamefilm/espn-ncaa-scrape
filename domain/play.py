from dataclasses import dataclass


@dataclass
class Play:
    game_id: int
    drive_num: int
    play_id: int
    play_num: int
    play_type: str
    clock: int
    o_team_id: int
    d_team_id: int

    down: int
    ytg: int
    yfog: int

    text: str

