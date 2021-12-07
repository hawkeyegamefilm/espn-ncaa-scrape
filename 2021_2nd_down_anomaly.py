import json

from espn_game_parse import parse_espn_json

# Utility file to manually validate rushing data against season totals
# This is the main executable for spitting out carries for a player


games_2021 = [401282723,401282754,401282755,401282756,401282759,401282758,401282760,401282763,401282757,401282762,401282721,401282761,401331447]


year = "2021"
rusher = "Goodson"
carries = 0
yards = 0
carry_list = []
total_inc = 0
inc_flag = 0
inc_count = 0
for g in games_2021:
    game_file = open("data/{y}/{g}.json".format(g=g, y=year), encoding="utf-8-sig")
    game_json = json.load(game_file)
    game_ret = parse_espn_json(game_json)
    for dr in game_ret.drives:
        for pl in dr.plays:
            if inc_flag == 1 and pl.down == 2 and (pl.play_type == 'Rush' or pl.play_type == 'Rushing Touchdown') and pl.o_team_id == 2294:
                carries += 1
                print(pl)
                inc_flag = 0
            elif inc_flag == 1 and pl.o_team_id == 2294:
                print(pl)
                inc_flag = 0
            if pl.o_team_id == 2294 and pl.down == 1 and pl.play_type == 'Pass Incompletion':
                inc_flag = 1
                print(pl)
                total_inc += 1


            # if pl.game_id == 401282723 and pl.o_team_id == 2294 and pl.down == 1 and pl.ytg == 10 and pl.play_type == 'Pass Incompletion':
            #     inc_flag = 1
            #     print(pl)
            #     total_inc += 1


print(carries)
print(total_inc)