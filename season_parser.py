import json
from os import listdir
from os.path import isfile, join

from espn_game_parse import parse_espn_json

year = '2021'

game_path = "data/{y}/"

list_of_game_ids = [f.strip(".json") for f in listdir(game_path.format(y=year)) if isfile(join(game_path.format(y=year), f))]


# print(list_of_game_ids)
parsed_games = []

for g in list_of_game_ids:
    game_file = open("data/{y}/{g}.json".format(g=g, y=year), encoding="utf-8-sig")
    game_json = json.load(game_file)
    # print(g)
    # try:
    game_ret = parse_espn_json(game_json)
    parsed_games.append(game_ret)
    # except Exception as e:
    #     print("exception tripped")
    #     print(e.args)

    # persist the game, drives & plays to DB

print(len(parsed_games))
