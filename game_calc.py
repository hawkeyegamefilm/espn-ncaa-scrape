import json

from espn_game_parse import parse_espn_json

# Utility file to manually validate rusher data against game totals, fill in the y = year, g = game_id, & rusher = "Sims"

carries = 0
yards = 0
carry_list = []

y = 2021
g = 401282052
rusher = "Sims"  # fill me in

game_file = open("data/{y}/{g}.json".format(y=y, g=g), encoding="utf-8-sig")
game_json = json.load(game_file)
game_obj = parse_espn_json(game_json)
for dr in game_obj.drives:
    for pl in dr.plays:
        if pl.play_type == 'Rush' and rusher + ' rush' in pl.text:
            yds = 0
            print(pl.text)
            if "no gain" in pl.text:
                yds = 0
            elif "loss of" in pl.text:
                idx_of_loss_of = pl.text.index("loss of") + 7
                idx_of_yard = pl.text.index("yard") - 1
                yds = -int(pl.text[idx_of_loss_of: idx_of_yard])
            else:
                idx_of_for = pl.text.index("for") + 4
                idx_of_yard = pl.text.index("yard") - 1
                yds = int(pl.text[idx_of_for: idx_of_yard])
            carries += 1
            yards += yds
            carry_list.append(yds)

print(carries)
print(yards)
print(carry_list)