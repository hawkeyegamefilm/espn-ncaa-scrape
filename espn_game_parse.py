import json

from parse_lib import parse_game_details, parse_drive_details, create_team_map, parse_play_details, \
    get_defensive_team_id

"""
Entry function for parsing ESPN PBP json, this function expects the full contents of the event API call & returns a fully populated game object
"""
def parse_espn_json(game_json):
    game = parse_game_details(game_json['gameInfo'], game_json['header'])
    print(game)
    team_map = create_team_map(game_json['boxscore']['teams'])
    teams = [int(game_json['boxscore']['teams'][0]['team']['id']), int(game_json['boxscore']['teams'][1]['team']['id'])]
    print(teams)
    # for poss_idx, poss in enumerate(period['possessions']):
    for drive_idx, drive in enumerate(game_json['drives']['previous']):
        previous_drive_end_type = ""
        drive_num = drive_idx + 1
        if 'result' in game_json['drives']['previous'][drive_idx - 1].keys(): # this is only needed to cover for bad data w/drives not having an end, end of half scenarios
            if drive_idx == 0 or game_json['drives']['previous'][drive_idx - 1]['result'] == 'END OF HALF':  # also need to flag 2nd H kickoffs
                previous_drive_end_type = "KICKOFF"
            else:
                previous_drive_end_type = game_json['drives']['previous'][drive_idx - 1]['result']
        else:
            previous_drive_end_type = "KICKOFF"
        drive_obj = parse_drive_details(game.id, drive_num, team_map, drive, previous_drive_end_type)
        game.drives.append(drive_obj)
        for play_idx, play in enumerate(drive['plays']):
            if 'type' not in play.keys():
                # box quarter start, & scoring plays
                print("type missing")
                print(play)
            else:
                play = parse_play_details(game.id, drive_obj.team_id, get_defensive_team_id(teams, drive_obj.team_id), drive_num, play_idx, play)
                drive_obj.plays.append(play)
    return game


