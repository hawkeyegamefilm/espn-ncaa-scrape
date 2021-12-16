from dataclasses import dataclass


@dataclass
class Drive:
    game_id: int
    drive_id: int
    team_id: int
    opponent_id: int
    drive_num: int
    start_time: int
    start_period: int
    start_spot: int
    start_type: str
    end_time: int
    end_period: int
    end_spot: int
    end_type: str
    play_count: int
    yards: int
    top: int
    plays: []
