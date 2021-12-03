import json

from espn_game_parse import parse_espn_json

# Utility file to manually validate rushing data against season totals
# This is the main executable for spitting out carries for a player


games_2008 = [282432294,282502294,282572294,282640221,282712294,282780127,282850084, 282922294,283060356, 283132294, 283202294, 283270135, 290012294]
games_2011 = [312462294,312530066,312602294,312672294,312810213,312882294,312952294,313020135,313092294,313162294,313232509,313290158,313640201]
games_2005 = [252462294,252530066,252602294,252670194,252742294,252812509,252882294,252952294,253090077,253160275,253232294]
games_2006 = [262452294,263642294,262520183,262592294,262660356,262732294,262802294,262870084,262940130,263012294,263082294,263152294,263220135]
games_2007 = [272442459,272512294,272580066,272650275,272722294,272790213,272862294,272932509,273002294,273070077,273142294,273212294]

year = "2007"
rusher = "Sims"
carries = 0
yards = 0
carry_list = []
for g in games_2007:
    game_file = open("data/{y}/{g}.json".format(g=g, y=year), encoding="utf8")
    game_json = json.load(game_file)
    game_ret = parse_espn_json(game_json)
    for dr in game_ret.drives:
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

