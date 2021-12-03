# espn-ncaa-scrape
Some basic python snippets hacked together for scraping & parsing ESPNs API for PBP data

###Scraping notes

####Game Scrape
http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={gameId}

####Conference key map

`{"80" : "FBS", "1" : "ACC", "151" : "American", "4" : "Big 12", "5" : "Big Ten", "12" : "Conf USA", "18" : "FBS Ind", "15" : "MAC", "17" : "Mt. West", "9" : "Pac 12", "8" : "SEC", "37" : "Sun Belt"}`

#### All FBS Teams
http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams?limit=1000&groups=80

####Roster by Team id
https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/{teamId}/roster

####Stats by Team id
https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/{teamId}/statistics

####Schedule by Team id
https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/{teamId}/schedule

####Scoreboard for FBS
http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?groups=80

####Historical schedule by year
https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/{teamId}/schedule?season={year in YYYY}
