import csv
from game_downloader import download_game

## open season file and parse game_id column & dl to appropirate folder

year = 2021

path_template = "game_results/{y}_games.csv"

with open(path_template.format(y=year), encoding="utf-8-sig") as csv_season:
    reader = csv.DictReader(csv_season)
    for row in reader:
        download_game(year, row['id'])

csv_season.close()

