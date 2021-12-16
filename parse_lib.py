from domain.drive import Drive
from domain.game import Game
from domain.play import Play


def parse_game_details(game_info_block, header):
    site = 'team'
    broadcast = ""
    venue = 0
    if header['competitions'][0]['broadcasts']:
        broadcast = header['competitions'][0]['broadcasts'][0]['media']['shortName']
    if header['competitions'][0]['neutralSite']:
        site = "neutral"
    if 'venue' in game_info_block.keys():
        venue = int(game_info_block['venue']['id'])
    return Game(int(header['id']),
                header['competitions'][0]['date'],
                header['season']['year'],
                header['week'],
                venue,
                broadcast,
                game_info_block['attendance'],
                [],
                site)


def parse_drive_details(game_id, drive_idx, team_map, drive, previous_end_type):

    end_time_value = 0
    start_time_value = 0
    end_period = 4
    end_yard_line = 0
    drive_result = "END OF GAME"  # defaulting drive result due to some old formats that seem to require it
    time_elapsed = 0
    o_team_id = team_map[drive['team']['name']]
    if 'timeElapsed' in drive.keys():
        time_elapsed = parse_clock_str(drive['timeElapsed']['displayValue'])
    if 'end' in drive.keys() and 'clock' in drive['end'].keys():
        # scenario where drive ends a period, if the value is present, parse it, else 0
        end_time_value = parse_clock_str(drive['end']['clock']['displayValue'])
        end_period = drive['end']['period']['number']
        end_yard_line = drive['end']['yardLine']
        drive_result = drive['result']
    if 'clock' in drive['start'].keys():
        start_time_value = parse_clock_str(drive['start']['clock']['displayValue'])
    return Drive(game_id,
                 int(drive['id']),
                 o_team_id,
                 get_defensive_team_id(team_map, o_team_id),
                 drive_idx,
                 start_time_value,
                 drive['start']['period']['number'],
                 drive['start']['yardLine'],
                 previous_end_type,
                 end_time_value,
                 end_period,
                 end_yard_line,
                 drive_result,
                 len(drive['plays']),
                 drive['yards'],
                 time_elapsed,
                 [])


def parse_play_details(game_id,  o_team_id, d_team_id, drive_num, play_idx, play):
    play_type = "uncategorized"
    if 'type' in play.keys():
        play_type = play['type']['text']
    else:
        print(str(game_id) + "|" + play['text'])
    text = ""  # defaulting text to handle bad data, several instances of missing text on play json
    if 'text' in play.keys():
        text = play['text']
    return Play(game_id,
                drive_num,
                play['id'],
                play_idx,
                play_type,
                parse_clock_str(play['clock']['displayValue']),
                o_team_id,
                d_team_id,
                play['start']['down'],
                play['start']['distance'],
                (100 - play['start']['yardsToEndzone']),
                text)


def create_team_map(teams):
    team_map = {}
    for team in teams:
        team_map[team['team']['name']] = int(team['team']['id'])
    return team_map


def parse_clock_str(clock_str):
    colon_idx = clock_str.index(':')

    minutes = int(clock_str[:colon_idx])
    seconds = int(clock_str[colon_idx + 1:])

    return (minutes * 60) + seconds


def get_defensive_team_id(teams, o_team_id):
    if teams.index(o_team_id) == 1:
        return teams[0]
    return teams[1]
