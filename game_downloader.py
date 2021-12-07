import http.client
import io
import urllib.request


url_template = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={id}"
write_path_template = "data/{year}/{id}.json"


def download_game(year, id):
    with urllib.request.urlopen(url_template.format(id=id)) as url:
        with io.open(write_path_template.format(year=year, id=id), 'w', encoding='utf-8') as file:
            try:
                file.write(url.read().decode())
            except http.client.IncompleteRead as e:
                print('incomplete read for: ' + id + " " + e)
            file.close()


# download_game(2021, 401282757)

# 2002 Iowa games
# list_2002 = [222432294, 222500193,222572294, 222642294, 222710213, 222782294, 222852294, 222920084, 222990130, 223062294, 223132294, 223200135, 230020030]
# 2008 Iowa games
# list_2008 = [282432294, 290012294,282502294,282572294,282640221,282712294,282780127, 282850084, 282922294,283060356, 283132294,283202294,283270135]
# 2011 Iowa games
# list_2011 = [312462294,312530066,312602294,312672294,312810213,312882294,312952294,313020135,313092294,313162294,313232509,313290158,313640201]
# 2005 Iowa games
# list_2005 = [252462294,252530066,252602294,252670194,252742294,252812509,252882294,252952294,253090077,253160275,253232294,260020057]
# 2006 Iowa games
# list_2006 = [262452294,263642294,262520183,262592294,262660356,262732294,262802294,262870084,262940130,263012294,263082294,263152294,263220135]
# 2007 Iowa games
# list_2007 = [272442459,272512294,272580066,272650275,272722294,272790213,272862294,272932509,273002294,273070077,273142294,273212294]
list= [401331447]

y = 2021
for game_id in list:
    download_game(y, game_id)
