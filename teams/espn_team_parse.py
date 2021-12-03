import json

from domain.team import Team

teams_file = open("2021-teams.json", encoding="utf8")
teams_json = json.load(teams_file)


def parse_teams():
    teams = teams_json['sports'][0]['leagues'][0]['teams']
    teams_list = []
    for team in teams:
        team_data = team['team']
        teams_list.append(Team(team_data['id'], team_data['name'], team_data['abbreviation'], team_data['nickname']))

    return teams_list


for t in parse_teams():
    print(t)


